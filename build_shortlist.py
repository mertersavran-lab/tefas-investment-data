from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT = BASE_DIR / "TEFAS_DAILY_DATA.csv"
SHORTLIST_CSV = BASE_DIR / "TEFAS_SHORTLIST.csv"
REPORT_MD = BASE_DIR / "TEFAS_SCREENING_REPORT.md"
STATUS_JSON = BASE_DIR / "TEFAS_SCREEN_STATUS.json"

TOP_N = 30
MIN_HISTORY = 80

BREAKDOWN_LABELS = {
    "stock_pct": "TR Hisse",
    "foreign_stock_pct": "Yabancı Hisse",
    "foreign_security_pct": "Yabancı Menkul",
    "foreign_etf_pct": "Yabancı ETF",
    "precious_metals_pct": "Kıymetli Maden",
    "eurobond_pct": "Eurobond",
    "government_bond_pct": "DİBS",
    "private_sector_bond_pct": "Özel Sektör Borçlanma",
    "investment_fund_pct": "Yatırım Fonu",
    "etf_pct": "ETF",
    "term_deposit_pct": "Vadeli Mevduat",
    "repo_pct": "Repo",
    "reverse_repo_pct": "Ters Repo",
    "derivative_pct": "Türev",
}

REQUIRED_METRICS = [
    "return_5d_pct",
    "previous_5d_pct",
    "acceleration_5d_pp",
    "return_20d_pct",
    "previous_20d_pct",
    "acceleration_20d_pp",
    "return_60d_pct",
    "volatility_20d_ann_pct",
    "max_drawdown_60d_pct",
    "distance_from_60d_high_pct",
]


def bool_series(s: pd.Series) -> pd.Series:
    if s.dtype == bool:
        return s
    return s.astype(str).str.strip().str.lower().isin(["true", "1", "yes"])


def pct_rank(s: pd.Series, higher_is_better: bool = True) -> pd.Series:
    x = pd.to_numeric(s, errors="coerce")
    x = x.fillna(x.median())
    return x.rank(pct=True, ascending=True) if higher_is_better else (-x).rank(pct=True, ascending=True)


def primary_exposure(row: pd.Series) -> str:
    pairs = []
    for col, label in BREAKDOWN_LABELS.items():
        if col in row.index and pd.notna(row[col]):
            pairs.append((float(row[col]), label))
    if not pairs:
        return ""
    value, label = max(pairs)
    return f"{label} %{value:.1f}"


def fmt(v, nd=2):
    if pd.isna(v):
        return "n/a"
    return f"{float(v):.{nd}f}"


def build() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"{INPUT.name} bulunamadı.")

    df = pd.read_csv(INPUT)
    df["is_current_bool"] = bool_series(df["is_current"])

    numeric_cols = REQUIRED_METRICS + [
        "return_126d_pct",
        "return_252d_pct",
        "portfolio_size_try",
        "investor_count",
        "history_observations",
    ] + list(BREAKDOWN_LABELS)

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    counts = df["investability_hint"].value_counts(dropna=False).to_dict()
    dataset_latest_date = (
        str(df["dataset_latest_date"].dropna().iloc[0])
        if "dataset_latest_date" in df and df["dataset_latest_date"].notna().any()
        else ""
    )
    source_generated = (
        str(df["generated_at_local"].dropna().iloc[0])
        if "generated_at_local" in df and df["generated_at_local"].notna().any()
        else ""
    )

    universe = df[
        (df["investability_hint"] == "RETAIL_CANDIDATE")
        & df["is_current_bool"]
        & (df["history_observations"].fillna(0) >= MIN_HISTORY)
    ].copy()

    before_complete = len(universe)
    universe = universe.dropna(subset=REQUIRED_METRICS).copy()

    universe["rank_acc20"] = pct_rank(universe["acceleration_20d_pp"])
    universe["rank_acc5"] = pct_rank(universe["acceleration_5d_pp"])
    universe["rank_r20"] = pct_rank(universe["return_20d_pct"])
    universe["rank_r60"] = pct_rank(universe["return_60d_pct"])
    universe["rank_r5"] = pct_rank(universe["return_5d_pct"])
    universe["rank_r126"] = pct_rank(universe["return_126d_pct"])
    universe["rank_low_vol"] = pct_rank(universe["volatility_20d_ann_pct"], higher_is_better=False)
    universe["rank_low_dd"] = pct_rank(universe["max_drawdown_60d_pct"], higher_is_better=True)

    # Momentum ağırlıklı ama risk ve aşırı uzamayı da hesaba katan nicel skor.
    universe["raw_score"] = 100 * (
        0.25 * universe["rank_acc20"]
        + 0.20 * universe["rank_acc5"]
        + 0.15 * universe["rank_r20"]
        + 0.10 * universe["rank_r60"]
        + 0.10 * universe["rank_r5"]
        + 0.05 * universe["rank_r126"]
        + 0.075 * universe["rank_low_vol"]
        + 0.075 * universe["rank_low_dd"]
    )

    # Performans kovalamayı azaltmak için yumuşak cezalar.
    penalty = pd.Series(0.0, index=universe.index)
    penalty += np.where(universe["return_5d_pct"] > 9, 8.0, 0.0)
    penalty += np.where(universe["return_20d_pct"] > 10, 5.0, 0.0)
    penalty += np.where(universe["return_60d_pct"] > 30, 7.0, 0.0)
    penalty += np.where(
        (universe["distance_from_60d_high_pct"] > -1.0)
        & (universe["return_5d_pct"] > 7),
        4.0,
        0.0,
    )

    # Çok küçük fonlar tamamen dışlanmaz; sadece skoru düşürülür.
    penalty += np.where(universe["portfolio_size_try"].fillna(0) < 20_000_000, 5.0, 0.0)
    penalty += np.where(universe["investor_count"].fillna(0) < 50, 3.0, 0.0)

    universe["penalty"] = penalty
    universe["quant_score"] = (universe["raw_score"] - universe["penalty"]).round(2)

    universe["early_momentum"] = (
        (universe["acceleration_5d_pp"] > 1)
        & (universe["acceleration_20d_pp"] > 1)
        & (universe["return_5d_pct"] > 0)
        & (universe["return_20d_pct"] > -1)
        & (universe["return_20d_pct"] < 10)
        & (universe["return_60d_pct"] < 25)
        & (universe["max_drawdown_60d_pct"] > -20)
    )

    universe["reversal"] = (
        (universe["previous_20d_pct"] < 0)
        & (universe["acceleration_20d_pp"] > 3)
        & (universe["return_5d_pct"] > 0)
        & (universe["acceleration_5d_pp"] > 1)
        & (universe["return_60d_pct"] < 20)
    )

    universe["trend_continuation"] = (
        (universe["return_5d_pct"] > 0)
        & (universe["return_20d_pct"] > 0)
        & (universe["return_60d_pct"] > 0)
        & (universe["acceleration_20d_pp"] > 0)
        & (universe["return_5d_pct"] < 10)
        & (universe["return_20d_pct"] < 12)
        & (universe["return_60d_pct"] < 35)
    )

    candidate = universe[
        universe["early_momentum"]
        | universe["reversal"]
        | universe["trend_continuation"]
    ].copy()

    def bucket(row):
        labels = []
        if row["reversal"]:
            labels.append("REVERSAL")
        if row["early_momentum"]:
            labels.append("EARLY_MOMENTUM")
        if row["trend_continuation"]:
            labels.append("TREND_CONTINUATION")
        return " + ".join(labels)

    candidate["screen_bucket"] = candidate.apply(bucket, axis=1)
    candidate["primary_exposure"] = candidate.apply(primary_exposure, axis=1)

    candidate["overextension_flag"] = np.where(
        (candidate["return_5d_pct"] > 9)
        | (candidate["return_20d_pct"] > 10)
        | (candidate["return_60d_pct"] > 30),
        "YES",
        "NO",
    )

    candidate["small_fund_flag"] = np.where(
        (candidate["portfolio_size_try"].fillna(0) < 20_000_000)
        | (candidate["investor_count"].fillna(0) < 50),
        "YES",
        "NO",
    )

    candidate = candidate.sort_values(
        ["quant_score", "acceleration_20d_pp", "acceleration_5d_pp"],
        ascending=[False, False, False],
    ).head(TOP_N).copy()

    candidate.insert(0, "rank", range(1, len(candidate) + 1))

    export_cols = [
        "rank",
        "fund_code",
        "fund_name",
        "theme_hint",
        "screen_bucket",
        "quant_score",
        "latest_nav_date",
        "latest_price",
        "return_5d_pct",
        "previous_5d_pct",
        "acceleration_5d_pp",
        "return_20d_pct",
        "previous_20d_pct",
        "acceleration_20d_pp",
        "return_60d_pct",
        "return_126d_pct",
        "return_252d_pct",
        "volatility_20d_ann_pct",
        "max_drawdown_60d_pct",
        "distance_from_60d_high_pct",
        "portfolio_size_try",
        "investor_count",
        "primary_exposure",
        "overextension_flag",
        "small_fund_flag",
        "investability_hint",
    ]

    export_cols = [c for c in export_cols if c in candidate.columns]
    candidate[export_cols].to_csv(SHORTLIST_CSV, index=False, encoding="utf-8-sig")

    lines = [
        "# TEFAS DAILY QUANTITATIVE SCREEN",
        "",
        f"- Dataset latest date: **{dataset_latest_date}**",
        f"- Source dataset generated at: **{source_generated}**",
        f"- Total funds in source dataset: **{len(df)}**",
        f"- RETAIL_CANDIDATE: **{int(counts.get('RETAIL_CANDIDATE', 0))}**",
        f"- VERIFY_ELIGIBILITY: **{int(counts.get('VERIFY_ELIGIBILITY', 0))}**",
        f"- EXCLUDE: **{int(counts.get('EXCLUDE', 0))}**",
        f"- Current retail funds with >= {MIN_HISTORY} observations before completeness filter: **{before_complete}**",
        f"- Quantitatively screenable retail funds after required-data filter: **{len(universe)}**",
        f"- Final shortlist size: **{len(candidate)}**",
        "",
        "## IMPORTANT",
        "",
        "This is a quantitative pre-screen, NOT an investment recommendation.",
        "Claude should research KAP/TEFAS/fund-manager disclosures and current macro/market conditions before turning any candidate into an actionable recommendation.",
        "The score is heuristic and prioritizes improving momentum while penalizing obvious short-term overextension and weak risk characteristics.",
        "",
        "## SCREEN LOGIC",
        "",
        "- EARLY_MOMENTUM: positive short- and medium-window acceleration with moderate 20d/60d returns.",
        "- REVERSAL: previous 20d period was negative, but current momentum has improved materially.",
        "- TREND_CONTINUATION: positive 5d/20d/60d trend with positive 20d acceleration, subject to extension limits.",
        "- Score emphasizes 20d and 5d acceleration; volatility and drawdown are explicit risk controls.",
        "- `theme_hint` and `primary_exposure` are screening aids, not substitutes for official KAP/TEFAS classification.",
        "",
        "## TOP QUANTITATIVE CANDIDATES",
        "",
        "|#|Kod|Fon|Tema|Bucket|Skor|5G|Önceki 5G|20G|Önceki 20G|60G|Vol 20G|Max DD 60G|60G Zirve Uzaklık|Ana Pozisyon|",
        "|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]

    for _, row in candidate.iterrows():
        name = str(row["fund_name"]).replace("|", "/")
        theme = str(row.get("theme_hint", "")).replace("|", "/")
        exposure = str(row.get("primary_exposure", "")).replace("|", "/")
        lines.append(
            f"|{int(row['rank'])}|{row['fund_code']}|{name}|{theme}|{row['screen_bucket']}|"
            f"{fmt(row['quant_score'])}|{fmt(row['return_5d_pct'])}%|{fmt(row['previous_5d_pct'])}%|"
            f"{fmt(row['return_20d_pct'])}%|{fmt(row['previous_20d_pct'])}%|{fmt(row['return_60d_pct'])}%|"
            f"{fmt(row['volatility_20d_ann_pct'])}%|{fmt(row['max_drawdown_60d_pct'])}%|"
            f"{fmt(row['distance_from_60d_high_pct'])}%|{exposure}|"
        )

    lines += [
        "",
        "## CLAUDE RESEARCH INSTRUCTION",
        "",
        "Use this shortlist as STAGE 1 only. For STAGE 2, investigate the highest-ranked candidates using current web research and primary sources where possible.",
        "Verify retail investability, current fund strategy, KAP disclosures, meaningful portfolio exposures, catalysts, major risks, and whether the quantitative move is supported by current market conditions.",
        "Do not recommend a fund solely because it appears in this report.",
    ]

    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")

    status = {
        "success": True,
        "dataset_latest_date": dataset_latest_date,
        "source_generated_at_local": source_generated,
        "source_fund_count": int(len(df)),
        "classification_counts": {
            "RETAIL_CANDIDATE": int(counts.get("RETAIL_CANDIDATE", 0)),
            "VERIFY_ELIGIBILITY": int(counts.get("VERIFY_ELIGIBILITY", 0)),
            "EXCLUDE": int(counts.get("EXCLUDE", 0)),
        },
        "screenable_retail_count": int(len(universe)),
        "shortlist_count": int(len(candidate)),
        "shortlist_file": SHORTLIST_CSV.name,
        "report_file": REPORT_MD.name,
    }

    STATUS_JSON.write_text(
        json.dumps(status, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Created {SHORTLIST_CSV.name}: {len(candidate)} rows")
    print(f"Created {REPORT_MD.name}")
    print(f"Created {STATUS_JSON.name}")


if __name__ == "__main__":
    build()
