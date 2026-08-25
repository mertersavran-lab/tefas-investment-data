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

MIN_HISTORY = 80
LANE_TOP_N = 15
REPORT_TOP_N = 10
MAX_SHORTLIST = 45

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

FOREIGN_KEYWORDS = [
    "YABANCI",
    "AMERİKA",
    "AMERIKA",
    "GLOBAL",
    "DÜNYA",
    "DUNYA",
    "AVRUPA",
    "ASYA",
    "JAPON",
    "ÇİN",
    "CIN",
    "NASDAQ",
    "S&P",
    "ABD",
]


def bool_series(s: pd.Series) -> pd.Series:
    if s.dtype == bool:
        return s
    return s.astype(str).str.strip().str.lower().isin(["true", "1", "yes"])


def pct_rank(s: pd.Series, higher_is_better: bool = True) -> pd.Series:
    x = pd.to_numeric(s, errors="coerce")
    if x.notna().any():
        x = x.fillna(x.median())
    else:
        x = pd.Series(0.0, index=s.index)
    if higher_is_better:
        return x.rank(pct=True, ascending=True)
    return (-x).rank(pct=True, ascending=True)


def primary_exposure(row: pd.Series) -> str:
    pairs = []
    for col, label in BREAKDOWN_LABELS.items():
        if col in row.index and pd.notna(row[col]):
            pairs.append((float(row[col]), label))
    if not pairs:
        return ""
    value, label = max(pairs)
    return f"{label} %{value:.1f}"


def fmt(v, nd: int = 2) -> str:
    if pd.isna(v):
        return "n/a"
    return f"{float(v):.{nd}f}"


def clean_text(v) -> str:
    return str(v).replace("|", "/") if pd.notna(v) else ""


def add_missing_numeric_columns(df: pd.DataFrame, cols: list[str]) -> None:
    for col in cols:
        if col not in df.columns:
            df[col] = np.nan
        df[col] = pd.to_numeric(df[col], errors="coerce")


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
    add_missing_numeric_columns(df, numeric_cols)

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

    # ------------------------------------------------------------------
    # COMMON RANKS
    # ------------------------------------------------------------------
    universe["rank_acc20"] = pct_rank(universe["acceleration_20d_pp"])
    universe["rank_acc5"] = pct_rank(universe["acceleration_5d_pp"])
    universe["rank_r5"] = pct_rank(universe["return_5d_pct"])
    universe["rank_r20"] = pct_rank(universe["return_20d_pct"])
    universe["rank_r60"] = pct_rank(universe["return_60d_pct"])
    universe["rank_r126"] = pct_rank(universe["return_126d_pct"])
    universe["rank_r252"] = pct_rank(universe["return_252d_pct"])
    universe["rank_low_vol"] = pct_rank(
        universe["volatility_20d_ann_pct"], higher_is_better=False
    )
    universe["rank_low_dd"] = pct_rank(
        universe["max_drawdown_60d_pct"], higher_is_better=True
    )

    size_log = np.log1p(universe["portfolio_size_try"].fillna(0).clip(lower=0))
    investor_log = np.log1p(universe["investor_count"].fillna(0).clip(lower=0))
    universe["rank_size"] = pct_rank(size_log)
    universe["rank_investors"] = pct_rank(investor_log)

    positive_horizons = pd.DataFrame(
        {
            "20d": universe["return_20d_pct"] > 0,
            "60d": universe["return_60d_pct"] > 0,
            "126d": universe["return_126d_pct"] > 0,
            "252d": universe["return_252d_pct"] > 0,
        },
        index=universe.index,
    ).mean(axis=1)
    universe["rank_consistency"] = pct_rank(positive_horizons)

    # ------------------------------------------------------------------
    # EXPOSURE PROXIES FOR DISCOVERY
    # These are screening aids only. Claude must verify actual holdings in Stage 2.
    # ------------------------------------------------------------------
    foreign_equity_proxy = universe[
        ["foreign_stock_pct", "foreign_security_pct", "foreign_etf_pct"]
    ].max(axis=1, skipna=True).fillna(0)

    text = (
        universe["fund_name"].fillna("").astype(str)
        + " "
        + universe.get("theme_hint", pd.Series("", index=universe.index)).fillna("").astype(str)
    ).str.upper()
    foreign_theme_flag = pd.Series(0.0, index=universe.index)
    for keyword in FOREIGN_KEYWORDS:
        foreign_theme_flag = np.maximum(
            foreign_theme_flag,
            text.str.contains(keyword, regex=False).astype(float) * 100.0,
        )

    universe["non_domestic_exposure_proxy"] = (
        np.maximum(foreign_equity_proxy, foreign_theme_flag)
        + universe["eurobond_pct"].fillna(0)
    ).clip(0, 100)
    universe["rank_non_domestic"] = pct_rank(universe["non_domestic_exposure_proxy"])

    domestic_equity = universe["stock_pct"].fillna(0)
    precious = universe["precious_metals_pct"].fillna(0)
    bonds = (
        universe["eurobond_pct"].fillna(0)
        + universe["government_bond_pct"].fillna(0)
        + universe["private_sector_bond_pct"].fillna(0)
    ).clip(0, 100)
    cash_like = (
        universe["term_deposit_pct"].fillna(0)
        + universe["repo_pct"].fillna(0)
        + universe["reverse_repo_pct"].fillna(0)
    ).clip(0, 100)
    fund_of_funds = (
        universe["investment_fund_pct"].fillna(0)
        + universe["etf_pct"].fillna(0)
    ).clip(0, 100)

    breadth = pd.concat(
        [
            domestic_equity,
            foreign_equity_proxy,
            precious,
            bonds,
            cash_like,
            fund_of_funds,
        ],
        axis=1,
    ).gt(10).sum(axis=1)
    universe["rank_exposure_breadth"] = pct_rank(breadth)

    risky_exposure_proxy = (
        np.maximum(domestic_equity, foreign_equity_proxy) + precious
    ).clip(0, 100)
    universe["rank_low_risky_exposure"] = pct_rank(
        risky_exposure_proxy, higher_is_better=False
    )

    # ------------------------------------------------------------------
    # LANE 1 — TACTICAL
    # Early momentum / reversal / trend continuation.
    # ------------------------------------------------------------------
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

    tactical_raw = 100 * (
        0.22 * universe["rank_acc20"]
        + 0.18 * universe["rank_acc5"]
        + 0.15 * universe["rank_r20"]
        + 0.10 * universe["rank_r60"]
        + 0.10 * universe["rank_r5"]
        + 0.05 * universe["rank_r126"]
        + 0.10 * universe["rank_low_vol"]
        + 0.10 * universe["rank_low_dd"]
    )

    tactical_penalty = pd.Series(0.0, index=universe.index)
    tactical_penalty += np.where(universe["return_5d_pct"] > 9, 8.0, 0.0)
    tactical_penalty += np.where(universe["return_20d_pct"] > 10, 5.0, 0.0)
    tactical_penalty += np.where(universe["return_60d_pct"] > 30, 7.0, 0.0)
    tactical_penalty += np.where(
        (universe["distance_from_60d_high_pct"] > -1.0)
        & (universe["return_5d_pct"] > 7),
        4.0,
        0.0,
    )
    tactical_penalty += np.where(
        universe["portfolio_size_try"].fillna(0) < 20_000_000, 5.0, 0.0
    )
    tactical_penalty += np.where(
        universe["investor_count"].fillna(0) < 50, 3.0, 0.0
    )
    universe["tactical_score"] = (tactical_raw - tactical_penalty).round(2)

    # ------------------------------------------------------------------
    # LANE 2 — CORE
    # Persistent medium/long-term performance + risk control + scale.
    # ------------------------------------------------------------------
    core_raw = 100 * (
        0.20 * universe["rank_r252"]
        + 0.20 * universe["rank_r126"]
        + 0.15 * universe["rank_r60"]
        + 0.15 * universe["rank_low_vol"]
        + 0.15 * universe["rank_low_dd"]
        + 0.05 * universe["rank_size"]
        + 0.05 * universe["rank_investors"]
        + 0.05 * universe["rank_consistency"]
    )
    core_penalty = pd.Series(0.0, index=universe.index)
    core_penalty += np.where(universe["return_5d_pct"] > 10, 4.0, 0.0)
    core_penalty += np.where(universe["return_20d_pct"] > 15, 5.0, 0.0)
    core_penalty += np.where(
        universe["portfolio_size_try"].fillna(0) < 20_000_000, 4.0, 0.0
    )
    core_penalty += np.where(
        universe["investor_count"].fillna(0) < 50, 3.0, 0.0
    )
    universe["core_score"] = (core_raw - core_penalty).round(2)

    # ------------------------------------------------------------------
    # LANE 3 — DIVERSIFICATION
    # Non-domestic / broader exposure + risk-adjusted persistence.
    # This does NOT replace portfolio-overlap research in Stage 2.
    # ------------------------------------------------------------------
    diversification_raw = 100 * (
        0.30 * universe["rank_non_domestic"]
        + 0.10 * universe["rank_exposure_breadth"]
        + 0.15 * universe["rank_r126"]
        + 0.10 * universe["rank_r252"]
        + 0.10 * universe["rank_low_vol"]
        + 0.10 * universe["rank_low_dd"]
        + 0.075 * universe["rank_size"]
        + 0.075 * universe["rank_investors"]
    )
    diversification_penalty = pd.Series(0.0, index=universe.index)
    diversification_penalty += np.where(
        universe["portfolio_size_try"].fillna(0) < 20_000_000, 4.0, 0.0
    )
    diversification_penalty += np.where(
        universe["investor_count"].fillna(0) < 50, 3.0, 0.0
    )
    diversification_penalty += np.where(universe["return_5d_pct"] > 12, 4.0, 0.0)
    universe["diversification_score"] = (
        diversification_raw - diversification_penalty
    ).round(2)

    # ------------------------------------------------------------------
    # LANE 4 — DEFENSIVE / DEPOSIT CHALLENGER
    # Low volatility / low drawdown + positive medium-term returns.
    # Deposit comparison itself remains a Stage-3 task for Claude.
    # ------------------------------------------------------------------
    defensive_raw = 100 * (
        0.30 * universe["rank_low_vol"]
        + 0.25 * universe["rank_low_dd"]
        + 0.10 * universe["rank_low_risky_exposure"]
        + 0.10 * universe["rank_r60"]
        + 0.10 * universe["rank_r126"]
        + 0.05 * universe["rank_r252"]
        + 0.05 * universe["rank_size"]
        + 0.05 * universe["rank_investors"]
    )
    defensive_penalty = pd.Series(0.0, index=universe.index)
    defensive_penalty += np.where(universe["return_60d_pct"] < 0, 8.0, 0.0)
    defensive_penalty += np.where(universe["return_126d_pct"] < 0, 6.0, 0.0)
    defensive_penalty += np.where(
        universe["portfolio_size_try"].fillna(0) < 20_000_000, 4.0, 0.0
    )
    defensive_penalty += np.where(
        universe["investor_count"].fillna(0) < 50, 3.0, 0.0
    )
    universe["defensive_score"] = (defensive_raw - defensive_penalty).round(2)

    # ------------------------------------------------------------------
    # FLAGS / LABELS
    # ------------------------------------------------------------------
    def tactical_bucket(row: pd.Series) -> str:
        labels = []
        if row["reversal"]:
            labels.append("REVERSAL")
        if row["early_momentum"]:
            labels.append("EARLY_MOMENTUM")
        if row["trend_continuation"]:
            labels.append("TREND_CONTINUATION")
        return " + ".join(labels)

    universe["tactical_bucket"] = universe.apply(tactical_bucket, axis=1)
    universe["primary_exposure"] = universe.apply(primary_exposure, axis=1)
    universe["overextension_flag"] = np.where(
        (universe["return_5d_pct"] > 9)
        | (universe["return_20d_pct"] > 10)
        | (universe["return_60d_pct"] > 30),
        "YES",
        "NO",
    )
    universe["small_fund_flag"] = np.where(
        (universe["portfolio_size_try"].fillna(0) < 20_000_000)
        | (universe["investor_count"].fillna(0) < 50),
        "YES",
        "NO",
    )

    lane_specs = {
        "TACTICAL": "tactical_score",
        "CORE": "core_score",
        "DIVERSIFICATION": "diversification_score",
        "DEFENSIVE": "defensive_score",
    }

    lane_frames: dict[str, pd.DataFrame] = {}
    lane_members: dict[str, set[str]] = {}

    for lane, score_col in lane_specs.items():
        lane_pool = universe.copy()

        if lane == "TACTICAL":
            lane_pool = lane_pool[
                lane_pool["early_momentum"]
                | lane_pool["reversal"]
                | lane_pool["trend_continuation"]
            ].copy()
        elif lane in {"CORE", "DIVERSIFICATION"}:
            lane_pool = lane_pool[lane_pool["history_observations"] >= 126].copy()

        lane_pool = lane_pool.sort_values(
            [score_col, "return_126d_pct", "portfolio_size_try"],
            ascending=[False, False, False],
        ).head(LANE_TOP_N)

        lane_frames[lane] = lane_pool
        lane_members[lane] = set(lane_pool["fund_code"].astype(str))

    selected_codes = set().union(*lane_members.values())
    candidate = universe[universe["fund_code"].astype(str).isin(selected_codes)].copy()

    def memberships(code: str) -> str:
        return " + ".join(
            lane for lane in lane_specs if str(code) in lane_members[lane]
        )

    candidate["lane_membership"] = candidate["fund_code"].map(memberships)

    # Primary lane and best score are calculated only among lanes in which
    # the fund actually qualified for the top-LANE_TOP_N list.
    def member_lane_result(row: pd.Series) -> pd.Series:
        qualified = [
            lane for lane in lane_specs
            if str(row["fund_code"]) in lane_members[lane]
        ]
        if not qualified:
            return pd.Series({"primary_lane": "", "best_lane_score": np.nan})
        primary = max(qualified, key=lambda lane: float(row[lane_specs[lane]]))
        return pd.Series(
            {
                "primary_lane": primary,
                "best_lane_score": float(row[lane_specs[primary]]),
            }
        )

    lane_result = candidate.apply(member_lane_result, axis=1)
    candidate["primary_lane"] = lane_result["primary_lane"]
    candidate["best_lane_score"] = lane_result["best_lane_score"]
    candidate = candidate.sort_values(
        ["best_lane_score", "core_score", "tactical_score"],
        ascending=[False, False, False],
    ).head(MAX_SHORTLIST).copy()
    candidate.insert(0, "rank", range(1, len(candidate) + 1))

    export_cols = [
        "rank",
        "fund_code",
        "fund_name",
        "theme_hint",
        "primary_lane",
        "lane_membership",
        "tactical_bucket",
        "best_lane_score",
        "tactical_score",
        "core_score",
        "diversification_score",
        "defensive_score",
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
        "non_domestic_exposure_proxy",
        "overextension_flag",
        "small_fund_flag",
        "investability_hint",
    ]
    export_cols = [c for c in export_cols if c in candidate.columns]
    candidate[export_cols].to_csv(SHORTLIST_CSV, index=False, encoding="utf-8-sig")

    # ------------------------------------------------------------------
    # HUMAN-READABLE REPORT FOR CLAUDE STAGE 2
    # ------------------------------------------------------------------
    lines = [
        "# TEFAS DAILY MULTI-LANE QUANTITATIVE SCREEN — V2",
        "",
        f"- Dataset latest date: **{dataset_latest_date}**",
        f"- Source dataset generated timestamp (as supplied): **{source_generated}**",
        f"- Total funds in source dataset: **{len(df)}**",
        f"- RETAIL_CANDIDATE: **{int(counts.get('RETAIL_CANDIDATE', 0))}**",
        f"- VERIFY_ELIGIBILITY: **{int(counts.get('VERIFY_ELIGIBILITY', 0))}**",
        f"- EXCLUDE: **{int(counts.get('EXCLUDE', 0))}**",
        f"- Current retail funds with >= {MIN_HISTORY} observations before completeness filter: **{before_complete}**",
        f"- Quantitatively screenable retail funds after required-data filter: **{len(universe)}**",
        f"- Combined multi-lane shortlist size: **{len(candidate)}**",
        "",
        "## IMPORTANT",
        "",
        "This is a quantitative discovery screen, NOT an investment recommendation.",
        "The same full retail universe is evaluated through four different lenses so that discovery is not limited to short-term momentum.",
        "Claude must perform fresh Stage-2 KAP/TEFAS/fund-manager research and Stage-3 portfolio-fit analysis before assigning actionable status.",
        "Diversification scores use exposure proxies and fund-name/theme hints when detailed allocation data is missing; actual holdings and overlap MUST be verified in Stage 2.",
        "Defensive scores are NOT a claim that a fund beats the user's deposit. The deposit benchmark comparison remains a Stage-3 calculation.",
        "",
        "## SCREEN LOGIC",
        "",
        "- TACTICAL: early momentum, reversal and trend continuation with overextension penalties.",
        "- CORE: medium/long-term persistence, lower volatility/drawdown, scale and consistency.",
        "- DIVERSIFICATION: non-domestic/broader exposure potential plus risk-adjusted persistence.",
        "- DEFENSIVE: lower volatility/drawdown and lower risky-asset exposure with positive medium-term performance.",
        "- Different fund codes do not automatically mean diversification; portfolio overlap must be researched separately.",
    ]

    def append_lane_section(lane: str, score_col: str) -> None:
        lines.extend(
            [
                "",
                f"## {lane} — TOP CANDIDATES",
                "",
                "|#|Kod|Fon|Tema|Skor|5G|20G|60G|126G|252G|Vol 20G|Max DD 60G|Ana Pozisyon|Tactical Bucket|",
                "|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
            ]
        )
        lane_df = lane_frames[lane].head(REPORT_TOP_N)
        for i, (_, row) in enumerate(lane_df.iterrows(), start=1):
            lines.append(
                f"|{i}|{clean_text(row['fund_code'])}|{clean_text(row['fund_name'])}|"
                f"{clean_text(row.get('theme_hint', ''))}|{fmt(row[score_col])}|"
                f"{fmt(row['return_5d_pct'])}%|{fmt(row['return_20d_pct'])}%|"
                f"{fmt(row['return_60d_pct'])}%|{fmt(row['return_126d_pct'])}%|"
                f"{fmt(row['return_252d_pct'])}%|{fmt(row['volatility_20d_ann_pct'])}%|"
                f"{fmt(row['max_drawdown_60d_pct'])}%|{clean_text(row['primary_exposure'])}|"
                f"{clean_text(row['tactical_bucket'])}|"
            )

    for lane, score_col in lane_specs.items():
        append_lane_section(lane, score_col)

    lines += [
        "",
        "## CLAUDE RESEARCH INSTRUCTION",
        "",
        "Treat this report as STAGE 1 only.",
        "Every daily analysis must separately monitor existing positions/watchlist AND inspect this fresh multi-lane screen for NEW candidates.",
        "Do not assume the existing watchlist contains the best available idea.",
        "For Stage 2, prioritize the strongest NEW or materially improving candidates across all four lanes, not only Tactical.",
        "Verify retail investability, current strategy, KAP/TEFAS disclosures, recent portfolio holdings, manager information, catalysts, risks, fees where relevant, and actual portfolio overlap.",
        "For Defensive candidates, compare against the user's deposit only after calculating the relevant same-horizon net deposit return and downside/liquidity trade-off.",
        "A fund must not become BUY/OPPORTUNITY merely because it ranks highly here.",
        "Zero new actionable opportunities is a valid result.",
    ]

    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")

    status = {
        "success": True,
        "screen_version": "V2_MULTI_LANE",
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
        "lane_top_n": LANE_TOP_N,
        "lane_counts": {
            lane: int(len(frame)) for lane, frame in lane_frames.items()
        },
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
    for lane, frame in lane_frames.items():
        print(f"{lane}: {len(frame)} candidates")


if __name__ == "__main__":
    build()
