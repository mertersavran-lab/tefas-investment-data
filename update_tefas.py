from __future__ import annotations

import json
import math
import sys
import traceback
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from pytefas import Crawler

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

RAW_PATH = DATA_DIR / "tefas_history.csv.gz"
DAILY_PATH = BASE_DIR / "TEFAS_DAILY_DATA.csv"
STATUS_PATH = BASE_DIR / "TEFAS_UPDATE_STATUS.json"

# İlk kurulumda 1 yıllık performans + güvenlik payı için yeterli tarihçe.
INITIAL_CALENDAR_DAYS = 430

# Son çalıştırmalarda son günleri yeniden çekmek; revizyon / tatil / eksik günleri kapatır.
REFRESH_LOOKBACK_DAYS = 14

BREAKDOWN_COLUMNS = [
    "stock_pct",
    "foreign_stock_pct",
    "foreign_security_pct",
    "foreign_etf_pct",
    "precious_metals_pct",
    "eurobond_pct",
    "government_bond_pct",
    "private_sector_bond_pct",
    "investment_fund_pct",
    "etf_pct",
    "term_deposit_pct",
    "repo_pct",
    "reverse_repo_pct",
    "derivative_pct",
]

def normalize_text(s: str) -> str:
    return (
        str(s).upper()
        .replace("İ", "I")
        .replace("Ş", "S")
        .replace("Ğ", "G")
        .replace("Ü", "U")
        .replace("Ö", "O")
        .replace("Ç", "C")
    )

def theme_hint(name: str) -> str:
    n = normalize_text(name)
    rules = [
        (("ROBOT", "YARI ILETKEN"), "Robotik / Yarı İletken"),
        (("YAPAY ZEKA",), "Yapay Zeka"),
        (("TEKNOLOJI",), "Teknoloji"),
        (("ALTIN",), "Altın"),
        (("GUMUS",), "Gümüş"),
        (("KIYMETLI MADEN",), "Kıymetli Madenler"),
        (("ENERJI",), "Enerji"),
        (("PETROL",), "Petrol / Enerji"),
        (("SAGLIK",), "Sağlık"),
        (("BANK",), "Bankacılık / Finans"),
        (("YABANCI",), "Yabancı Varlıklar"),
        (("EUROBOND",), "Eurobond"),
        (("BORCLANMA",), "Borçlanma Araçları"),
        (("HISSE SENEDI",), "Hisse Senedi"),
        (("DEGISKEN",), "Değişken"),
        (("FON SEPETI",), "Fon Sepeti"),
        (("KATILIM",), "Katılım"),
    ]
    for needles, label in rules:
        if all(x in n for x in needles):
            return label
    return "Diğer / Belirsiz"

def investability_hint(name: str) -> tuple[str, str]:
    n = normalize_text(name)
    if "PARA PIYASASI" in n:
        return "EXCLUDE", "Para piyasası fonu"
    if "SERBEST" in n:
        return "VERIFY_ELIGIBILITY", "Serbest fon; nitelikli yatırımcı / dağıtım kısıtı olabilir"
    if "OZEL FON" in n or "OZEL" in n and "FON" in n:
        return "VERIFY_ELIGIBILITY", "Özel fon; erişim kısıtı olabilir"
    return "RETAIL_CANDIDATE", ""

def pct_return(prices: pd.Series, intervals: int) -> float:
    # intervals işlem aralığıdır; 5 günlük getiri için 6 fiyat gözlemi gerekir.
    if len(prices) < intervals + 1:
        return np.nan
    start = prices.iloc[-(intervals + 1)]
    end = prices.iloc[-1]
    if pd.isna(start) or pd.isna(end) or start == 0:
        return np.nan
    return (end / start - 1.0) * 100.0

def prev_pct_return(prices: pd.Series, intervals: int) -> float:
    # Son dönemin hemen öncesindeki, çakışmayan aynı uzunluktaki pencere.
    need = 2 * intervals + 1
    if len(prices) < need:
        return np.nan
    start = prices.iloc[-(2 * intervals + 1)]
    end = prices.iloc[-(intervals + 1)]
    if pd.isna(start) or pd.isna(end) or start == 0:
        return np.nan
    return (end / start - 1.0) * 100.0

def annualized_volatility(prices: pd.Series, trading_days: int = 20) -> float:
    if len(prices) < trading_days + 1:
        return np.nan
    r = prices.pct_change().dropna().iloc[-trading_days:]
    if len(r) < max(5, trading_days // 2):
        return np.nan
    return float(r.std(ddof=1) * math.sqrt(252) * 100.0)

def max_drawdown(prices: pd.Series, trading_days: int = 60) -> float:
    if len(prices) < 2:
        return np.nan
    p = prices.iloc[-(trading_days + 1):] if len(prices) > trading_days else prices
    running_max = p.cummax()
    dd = p / running_max - 1.0
    return float(dd.min() * 100.0)

def distance_from_high(prices: pd.Series, trading_days: int = 60) -> float:
    if len(prices) < 2:
        return np.nan
    p = prices.iloc[-(trading_days + 1):] if len(prices) > trading_days else prices
    high = p.max()
    if high == 0 or pd.isna(high):
        return np.nan
    return float((p.iloc[-1] / high - 1.0) * 100.0)

def load_existing() -> pd.DataFrame:
    if not RAW_PATH.exists():
        return pd.DataFrame()
    df = pd.read_csv(RAW_PATH, compression="gzip", parse_dates=["date"])
    return df

def fetch_history(existing: pd.DataFrame) -> pd.DataFrame:
    today = date.today()
    if existing.empty:
        start = today - timedelta(days=INITIAL_CALENDAR_DAYS)
        print(f"İlk kurulum: TEFAS YAT fon tarihçesi çekiliyor: {start} -> {today}")
    else:
        last_date = pd.to_datetime(existing["date"]).max().date()
        start = min(last_date - timedelta(days=REFRESH_LOOKBACK_DAYS), today)
        print(f"Güncelleme: TEFAS verisi yeniden çekiliyor: {start} -> {today}")

    tefas = Crawler(timeout=60, max_retry=5)
    fresh = tefas.fetch(start, today, kind="YAT", columns="info")

    if fresh is None or fresh.empty:
        if existing.empty:
            raise RuntimeError("TEFAS'tan hiç veri alınamadı.")
        print("Yeni veri alınamadı; mevcut tarihçe korunuyor.")
        return existing

    fresh = fresh.copy()
    fresh["date"] = pd.to_datetime(fresh["date"])
    fresh["fund_code"] = fresh["fund_code"].astype(str).str.upper().str.strip()
    fresh["fund_name"] = fresh["fund_name"].astype(str).str.strip()
    fresh["price"] = pd.to_numeric(fresh["price"], errors="coerce")
    fresh["portfolio_size"] = pd.to_numeric(fresh.get("portfolio_size"), errors="coerce")
    fresh["investor_count"] = pd.to_numeric(fresh.get("investor_count"), errors="coerce")

    combined = pd.concat([existing, fresh], ignore_index=True, sort=False)
    combined["date"] = pd.to_datetime(combined["date"])
    combined["fund_code"] = combined["fund_code"].astype(str).str.upper().str.strip()
    combined = combined.dropna(subset=["fund_code", "date", "price"])
    combined = combined.drop_duplicates(["fund_code", "date"], keep="last")
    combined = combined.sort_values(["fund_code", "date"]).reset_index(drop=True)

    # Dosyayı kontrol altında tut; 1Y hesabı için yeterli güvenlik payı bırak.
    cutoff = pd.Timestamp(today - timedelta(days=500))
    combined = combined.loc[combined["date"] >= cutoff].copy()

    combined.to_csv(
        RAW_PATH,
        index=False,
        compression="gzip",
        encoding="utf-8-sig",
        date_format="%Y-%m-%d",
    )
    return combined

def fetch_latest_breakdown(latest_date: pd.Timestamp) -> tuple[pd.DataFrame, str | None]:
    tefas = Crawler(timeout=60, max_retry=5)
    # Bazı günlerde dağılım verisi aynı tarih için boş olabilir; geriye doğru dene.
    for back in range(0, 8):
        d = (latest_date - pd.Timedelta(days=back)).date()
        try:
            df = tefas.fetch(d, kind="YAT", columns="breakdown")
        except Exception as exc:
            print(f"Dağılım verisi {d} için alınamadı: {exc}")
            continue
        if df is not None and not df.empty:
            df = df.copy()
            df["fund_code"] = df["fund_code"].astype(str).str.upper().str.strip()
            available = ["fund_code"] + [c for c in BREAKDOWN_COLUMNS if c in df.columns]
            return df[available].drop_duplicates("fund_code", keep="last"), str(d)
    return pd.DataFrame(), None

def build_summary(hist: pd.DataFrame) -> tuple[pd.DataFrame, pd.Timestamp]:
    if hist.empty:
        raise RuntimeError("Tarihçe boş; özet üretilemiyor.")

    hist = hist.sort_values(["fund_code", "date"]).copy()
    global_latest = hist["date"].max()

    rows = []
    for fund_code, g in hist.groupby("fund_code", sort=False):
        g = g.dropna(subset=["price"]).sort_values("date")
        if g.empty:
            continue

        prices = g["price"].astype(float).reset_index(drop=True)
        last = g.iloc[-1]
        name = str(last["fund_name"])

        r5 = pct_return(prices, 5)
        p5 = prev_pct_return(prices, 5)
        r20 = pct_return(prices, 20)
        p20 = prev_pct_return(prices, 20)

        hint, reason = investability_hint(name)

        rows.append({
            "fund_code": fund_code,
            "fund_name": name,
            "latest_nav_date": pd.to_datetime(last["date"]).date().isoformat(),
            "latest_price": float(last["price"]),
            "portfolio_size_try": float(last["portfolio_size"]) if pd.notna(last.get("portfolio_size")) else np.nan,
            "investor_count": float(last["investor_count"]) if pd.notna(last.get("investor_count")) else np.nan,
            "theme_hint": theme_hint(name),
            "investability_hint": hint,
            "investability_note": reason,
            "is_current": (global_latest - pd.to_datetime(last["date"])).days <= 5,
            "return_5d_pct": r5,
            "previous_5d_pct": p5,
            "acceleration_5d_pp": (r5 - p5) if pd.notna(r5) and pd.notna(p5) else np.nan,
            "return_20d_pct": r20,
            "previous_20d_pct": p20,
            "acceleration_20d_pp": (r20 - p20) if pd.notna(r20) and pd.notna(p20) else np.nan,
            "return_60d_pct": pct_return(prices, 60),
            "return_126d_pct": pct_return(prices, 126),
            "return_252d_pct": pct_return(prices, 252),
            "volatility_20d_ann_pct": annualized_volatility(prices, 20),
            "max_drawdown_60d_pct": max_drawdown(prices, 60),
            "distance_from_60d_high_pct": distance_from_high(prices, 60),
            "history_observations": int(len(prices)),
        })

    summary = pd.DataFrame(rows)
    return summary, global_latest

def main() -> None:
    started = pd.Timestamp.now()
    status = {
        "started_at": started.isoformat(),
        "success": False,
        "output_file": str(DAILY_PATH),
    }

    try:
        existing = load_existing()
        hist = fetch_history(existing)
        summary, global_latest = build_summary(hist)

        breakdown, breakdown_date = fetch_latest_breakdown(global_latest)
        if not breakdown.empty:
            summary = summary.merge(breakdown, how="left", on="fund_code")

        summary["dataset_latest_date"] = global_latest.date().isoformat()
        summary["breakdown_date"] = breakdown_date or ""
        summary["generated_at_local"] = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")

        ordered = [
            "fund_code", "fund_name", "theme_hint",
            "investability_hint", "investability_note", "is_current",
            "latest_nav_date", "latest_price",
            "return_5d_pct", "previous_5d_pct", "acceleration_5d_pp",
            "return_20d_pct", "previous_20d_pct", "acceleration_20d_pp",
            "return_60d_pct", "return_126d_pct", "return_252d_pct",
            "volatility_20d_ann_pct", "max_drawdown_60d_pct",
            "distance_from_60d_high_pct",
            "portfolio_size_try", "investor_count", "history_observations",
        ] + [c for c in BREAKDOWN_COLUMNS if c in summary.columns] + [
            "dataset_latest_date", "breakdown_date", "generated_at_local"
        ]
        summary = summary[[c for c in ordered if c in summary.columns]].copy()

        numeric_cols = summary.select_dtypes(include=[np.number]).columns
        summary[numeric_cols] = summary[numeric_cols].round(4)

        summary = summary.sort_values(
            ["is_current", "investability_hint", "fund_code"],
            ascending=[False, True, True],
        )

        summary.to_csv(DAILY_PATH, index=False, encoding="utf-8-sig")

        status.update({
            "success": True,
            "finished_at": pd.Timestamp.now().isoformat(),
            "dataset_latest_date": global_latest.date().isoformat(),
            "fund_count": int(len(summary)),
            "breakdown_date": breakdown_date,
            "message": "TEFAS_DAILY_DATA.csv başarıyla güncellendi.",
        })
        print("\nBAŞARILI")
        print(f"Fon sayısı: {len(summary)}")
        print(f"Veri setindeki en güncel NAV tarihi: {global_latest.date()}")
        print(f"Çıktı: {DAILY_PATH}")

    except Exception as exc:
        status.update({
            "success": False,
            "finished_at": pd.Timestamp.now().isoformat(),
            "error": str(exc),
            "traceback": traceback.format_exc(),
        })
        print("\nHATA:", exc)
        traceback.print_exc()
        raise
    finally:
        STATUS_PATH.write_text(
            json.dumps(status, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

if __name__ == "__main__":
    main()
