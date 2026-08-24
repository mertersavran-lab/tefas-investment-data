# TEFAS DAILY QUANTITATIVE SCREEN

- Dataset latest date: **2026-08-24**
- Source dataset generated at: **2026-08-24 06:27:44**
- Total funds in source dataset: **2063**
- RETAIL_CANDIDATE: **612**
- VERIFY_ELIGIBILITY: **1298**
- EXCLUDE: **153**
- Current retail funds with >= 80 observations before completeness filter: **579**
- Quantitatively screenable retail funds after required-data filter: **579**
- Final shortlist size: **30**

## IMPORTANT

This is a quantitative pre-screen, NOT an investment recommendation.
Claude should research KAP/TEFAS/fund-manager disclosures and current macro/market conditions before turning any candidate into an actionable recommendation.
The score is heuristic and prioritizes improving momentum while penalizing obvious short-term overextension and weak risk characteristics.

## SCREEN LOGIC

- EARLY_MOMENTUM: positive short- and medium-window acceleration with moderate 20d/60d returns.
- REVERSAL: previous 20d period was negative, but current momentum has improved materially.
- TREND_CONTINUATION: positive 5d/20d/60d trend with positive 20d acceleration, subject to extension limits.
- Score emphasizes 20d and 5d acceleration; volatility and drawdown are explicit risk controls.
- `theme_hint` and `primary_exposure` are screening aids, not substitutes for official KAP/TEFAS classification.

## TOP QUANTITATIVE CANDIDATES

|#|Kod|Fon|Tema|Bucket|Skor|5G|Önceki 5G|20G|Önceki 20G|60G|Vol 20G|Max DD 60G|60G Zirve Uzaklık|Ana Pozisyon|
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
|1|RPM|ROTA PORTFÖY İLAÇ VE MEDİKAL TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|83.32|4.76%|1.84%|11.15%|2.45%|20.11%|11.40%|-1.72%|0.00%||
|2|NKT|NUROL PORTFÖY BİRİNCİ KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|79.65|4.93%|0.86%|7.21%|3.79%|12.47%|14.00%|-4.53%|0.00%|TR Hisse %90.5|
|3|OHK|OYAK PORTFÖY KATILIM HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|78.87|5.61%|1.85%|7.44%|3.76%|10.65%|17.32%|-4.87%|0.00%||
|4|BV1|BV PORTFÖY BİRİNCİ HİSSE SENEDİ (TL) FON (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|77.82|3.74%|0.20%|8.10%|1.99%|12.69%|25.89%|-6.86%|0.00%||
|5|YPR|AZİMUT PORTFÖY YILDIZ PAZAR ŞİRKETLERİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|77.38|4.23%|0.14%|5.84%|-0.54%|8.27%|16.92%|-7.23%|0.00%||
|6|DNF|A1 CAPİTAL PORTFÖY DİNAMİK FON SEPETİ FONU|Fon Sepeti|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|77.36|2.09%|0.87%|7.80%|-0.21%|9.27%|12.53%|-3.31%|0.00%|Yatırım Fonu %90.2|
|7|ECA|GLOBAL MD PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|76.81|2.89%|1.84%|7.45%|2.10%|19.61%|15.98%|-4.34%|0.00%|TR Hisse %56.2|
|8|OPL|OSMANLI PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|76.25|3.30%|1.16%|8.54%|2.90%|6.91%|8.06%|-4.70%|0.00%|ETF %18.7|
|9|EVM|DENİZ PORTFÖY ENERJİ VE MADENCİLİK SEKTÖRÜ DEĞİŞKEN FON|Enerji|EARLY_MOMENTUM + TREND_CONTINUATION|75.69|3.75%|0.90%|8.61%|3.92%|7.63%|13.46%|-7.61%|0.00%|Yabancı ETF %35.7|
|10|ICH|PARDUS PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|75.64|2.39%|1.53%|8.36%|4.84%|19.97%|7.78%|-1.05%|0.00%|TR Hisse %53.5|
|11|FNO|QNB PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|75.63|2.68%|2.01%|6.22%|0.08%|9.81%|8.02%|-1.15%|0.00%|TR Hisse %29.9|
|12|FD1|ONE PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|75.36|3.40%|0.75%|6.12%|0.22%|11.85%|11.22%|-2.76%|0.00%||
|13|SSK|DENİZ PORTFÖY SAĞLIK SEKTÖRÜ DEĞİŞKEN FON|Sağlık|EARLY_MOMENTUM + TREND_CONTINUATION|75.28|2.89%|1.21%|7.19%|4.20%|16.42%|10.24%|-2.11%|-0.18%|Yabancı Hisse %36.2|
|14|GSP|AZİMUT PYŞ KAR PAYI ÖDEYEN HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|74.89|5.08%|-0.08%|4.93%|0.08%|6.56%|16.79%|-5.68%|0.00%||
|15|DPT|DENİZ PORTFÖY BİST TEMETTÜ 25 ENDEKSİ HİSSE SENEDİ FONU ( HİSSE SENEDİ YOĞUN FON )|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|74.12|4.65%|1.20%|5.89%|2.06%|10.23%|17.87%|-5.19%|0.00%|TR Hisse %96.8|
|16|IDI|AZİMUT PORTFÖY İNŞAAT SEKTÖRÜ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|74.05|5.05%|3.29%|10.22%|2.46%|12.31%|27.27%|-7.66%|0.00%||
|17|KH1|AK PORTFÖY KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|73.27|5.54%|2.08%|7.01%|3.64%|7.72%|17.35%|-6.22%|0.00%||
|18|ZCK|ZİRAAT PORTFÖY AGRESİF KATILIM FONU|Katılım|EARLY_MOMENTUM + TREND_CONTINUATION|73.04|5.19%|2.16%|7.06%|4.61%|8.47%|15.64%|-5.35%|0.00%|TR Hisse %83.9|
|19|RBH|ALBARAKA PORTFÖY KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|72.98|5.16%|1.52%|5.50%|2.68%|9.33%|17.42%|-5.89%|0.00%|TR Hisse %97.9|
|20|GL1|AZİMUT PYŞ BİRİNCİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|72.85|4.50%|1.28%|6.14%|2.05%|10.96%|22.59%|-7.03%|0.00%||
|21|OMG|AZİMUT PORTFÖY İKİNCİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|72.52|3.22%|1.35%|5.56%|-1.99%|7.54%|16.99%|-8.11%|-0.07%||
|22|MTD|BV PORTFÖY MALZEME TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|REVERSAL|72.10|4.48%|0.23%|13.36%|-2.32%|2.57%|30.78%|-17.52%|-3.12%||
|23|IKL|İŞ PORTFÖY SAĞLIK ŞİRKETLERİ KARMA FON|Sağlık|EARLY_MOMENTUM + TREND_CONTINUATION|71.92|2.79%|1.06%|5.92%|3.55%|13.23%|11.98%|-2.33%|-0.27%||
|24|CVL|A1 CAPİTAL PORTFÖY ÇOKLU VARLIK KATILIM FONU|Katılım|EARLY_MOMENTUM + TREND_CONTINUATION|71.86|9.13%|0.87%|9.18%|4.30%|14.10%|17.81%|-3.08%|0.00%|TR Hisse %32.8|
|25|AFS|AK PORTFÖY SAĞLIK SEKTÖRÜ YABANCI HİSSE SENEDİ FONU|Sağlık|TREND_CONTINUATION|71.71|2.29%|1.73%|9.67%|4.70%|15.67%|18.69%|-4.39%|-1.08%||
|26|GMA|AZİMUT PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|71.35|3.76%|0.92%|5.17%|4.27%|9.97%|8.78%|-2.21%|0.00%||
|27|KTI|AZİMUT PORTFÖY KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|71.23|4.11%|1.73%|6.34%|3.96%|10.53%|18.71%|-5.11%|0.00%||
|28|OHB|OYAK PORTFÖY BİRİNCİ HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|70.77|3.96%|1.96%|5.58%|-0.44%|8.00%|17.92%|-8.58%|0.00%||
|29|YEF|YAPI KREDİ PORTFÖY BIST 30 ENDEKSİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|70.75|4.11%|3.33%|6.56%|-3.09%|8.34%|20.22%|-10.57%|0.00%|TR Hisse %93.2|
|30|ACD|İSTANBUL PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|70.73|2.45%|0.52%|3.32%|-1.10%|11.47%|10.82%|-3.92%|0.00%||

## CLAUDE RESEARCH INSTRUCTION

Use this shortlist as STAGE 1 only. For STAGE 2, investigate the highest-ranked candidates using current web research and primary sources where possible.
Verify retail investability, current fund strategy, KAP disclosures, meaningful portfolio exposures, catalysts, major risks, and whether the quantitative move is supported by current market conditions.
Do not recommend a fund solely because it appears in this report.