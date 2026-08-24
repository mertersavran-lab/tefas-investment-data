# TEFAS DAILY QUANTITATIVE SCREEN

- Dataset latest date: **2026-08-24**
- Source dataset generated at: **2026-08-24 09:36:26**
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
|1|RPM|ROTA PORTFÖY İLAÇ VE MEDİKAL TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|80.30|4.76%|1.84%|11.15%|2.45%|20.11%|11.40%|-1.72%|0.00%|Yabancı Hisse %62.7|
|2|GZG|GARANTİ PORTFÖY SAĞLIK VE GENETİK TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|80.20|4.53%|0.63%|7.69%|2.98%|23.38%|13.66%|-3.07%|-0.48%|Yabancı Hisse %65.3|
|3|DNF|A1 CAPİTAL PORTFÖY DİNAMİK FON SEPETİ FONU|Fon Sepeti|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|75.12|2.40%|0.87%|8.13%|-0.21%|9.60%|12.64%|-3.31%|0.00%|Yatırım Fonu %90.2|
|4|NKT|NUROL PORTFÖY BİRİNCİ KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|74.72|4.93%|0.86%|7.21%|3.79%|12.47%|14.00%|-4.53%|0.00%|TR Hisse %90.5|
|5|OHK|OYAK PORTFÖY KATILIM HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|73.84|5.61%|1.85%|7.44%|3.76%|10.65%|17.32%|-4.87%|0.00%||
|6|FNO|QNB PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|73.25|2.98%|2.01%|6.54%|0.08%|10.13%|8.25%|-1.15%|0.00%|TR Hisse %29.8|
|7|BV1|BV PORTFÖY BİRİNCİ HİSSE SENEDİ (TL) FON (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|72.45|3.74%|0.20%|8.10%|1.99%|12.69%|25.89%|-6.86%|0.00%||
|8|YPR|AZİMUT PORTFÖY YILDIZ PAZAR ŞİRKETLERİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|71.71|4.23%|0.14%|5.84%|-0.54%|8.27%|16.92%|-7.23%|0.00%|TR Hisse %90.4|
|9|ECA|GLOBAL MD PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|71.71|2.89%|1.84%|7.45%|2.10%|19.61%|15.98%|-4.34%|0.00%|TR Hisse %56.2|
|10|OPL|OSMANLI PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|70.91|3.30%|1.16%|8.54%|2.90%|6.91%|8.06%|-4.70%|0.00%|ETF %18.7|
|11|ICH|PARDUS PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|70.85|2.39%|1.53%|8.36%|4.84%|19.97%|7.78%|-1.05%|0.00%|TR Hisse %53.5|
|12|FD1|ONE PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|70.50|3.40%|0.75%|6.12%|0.22%|11.85%|11.22%|-2.76%|0.00%|TR Hisse %54.9|
|13|SSK|DENİZ PORTFÖY SAĞLIK SEKTÖRÜ DEĞİŞKEN FON|Sağlık|EARLY_MOMENTUM + TREND_CONTINUATION|70.23|2.89%|1.21%|7.20%|4.20%|16.43%|10.23%|-2.11%|-0.18%|Yabancı Hisse %35.1|
|14|EVM|DENİZ PORTFÖY ENERJİ VE MADENCİLİK SEKTÖRÜ DEĞİŞKEN FON|Enerji|EARLY_MOMENTUM + TREND_CONTINUATION|70.02|3.75%|0.90%|8.61%|3.92%|7.63%|13.46%|-7.61%|0.00%|Yabancı ETF %35.7|
|15|IDI|AZİMUT PORTFÖY İNŞAAT SEKTÖRÜ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|69.48|5.05%|3.29%|10.22%|2.46%|12.31%|27.27%|-7.66%|0.00%|TR Hisse %85.7|
|16|GSP|AZİMUT PYŞ KAR PAYI ÖDEYEN HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|69.14|5.08%|-0.08%|4.93%|0.08%|6.56%|16.79%|-5.68%|0.00%|TR Hisse %96.2|
|17|CVL|A1 CAPİTAL PORTFÖY ÇOKLU VARLIK KATILIM FONU|Katılım|EARLY_MOMENTUM + TREND_CONTINUATION|68.19|9.13%|0.87%|9.18%|4.30%|14.10%|17.81%|-3.08%|0.00%|TR Hisse %32.8|
|18|DPT|DENİZ PORTFÖY BİST TEMETTÜ 25 ENDEKSİ HİSSE SENEDİ FONU ( HİSSE SENEDİ YOĞUN FON )|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|68.06|4.65%|1.20%|5.89%|2.06%|10.23%|17.87%|-5.19%|0.00%|TR Hisse %96.8|
|19|KH1|AK PORTFÖY KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|67.31|5.54%|2.08%|7.01%|3.64%|7.72%|17.35%|-6.22%|0.00%||
|20|MTD|BV PORTFÖY MALZEME TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|REVERSAL|66.91|4.51%|0.23%|13.38%|-2.32%|2.59%|30.82%|-17.52%|-3.09%|Yabancı Hisse %68.1|
|21|ZCK|ZİRAAT PORTFÖY AGRESİF KATILIM FONU|Katılım|EARLY_MOMENTUM + TREND_CONTINUATION|66.84|5.19%|2.16%|7.06%|4.61%|8.47%|15.64%|-5.35%|0.00%|TR Hisse %83.9|
|22|GL1|AZİMUT PYŞ BİRİNCİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|66.80|4.50%|1.28%|6.14%|2.05%|10.96%|22.59%|-7.03%|0.00%|TR Hisse %92.2|
|23|RBH|ALBARAKA PORTFÖY KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|66.80|5.16%|1.52%|5.50%|2.68%|9.33%|17.42%|-5.89%|0.00%|TR Hisse %97.9|
|24|FSU|TERA PORTFÖY FON SEPETİ FONU|Fon Sepeti|EARLY_MOMENTUM + TREND_CONTINUATION|66.63|5.72%|4.39%|9.25%|0.17%|4.38%|18.71%|-11.21%|0.00%|Yatırım Fonu %57.6|
|25|OMG|AZİMUT PORTFÖY İKİNCİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|66.46|3.22%|1.35%|5.56%|-1.99%|7.54%|16.99%|-8.11%|-0.07%|TR Hisse %89.6|
|26|KPC|KUVEYT TÜRK PORTFÖY KATILIM HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|66.30|3.96%|2.67%|6.42%|2.34%|8.77%|15.55%|-5.14%|0.00%|TR Hisse %87.1|
|27|SPT|AKTİF PORTFÖY KATILIM FON SEPETİ FONU|Fon Sepeti|EARLY_MOMENTUM + TREND_CONTINUATION|66.27|2.32%|1.12%|6.24%|1.89%|7.69%|8.16%|-3.12%|0.00%|Yatırım Fonu %79.8|
|28|IKL|İŞ PORTFÖY SAĞLIK ŞİRKETLERİ KARMA FON|Sağlık|EARLY_MOMENTUM + TREND_CONTINUATION|65.92|2.79%|1.06%|5.92%|3.55%|13.23%|11.98%|-2.33%|-0.27%|Yabancı Hisse %67.2|
|29|AFS|AK PORTFÖY SAĞLIK SEKTÖRÜ YABANCI HİSSE SENEDİ FONU|Sağlık|TREND_CONTINUATION|65.87|2.29%|1.73%|9.67%|4.70%|15.67%|18.69%|-4.39%|-1.08%||
|30|KPA|KUVEYT TÜRK PORTFÖY KAR PAYI ÖDEYEN KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|65.70|4.66%|3.97%|6.07%|2.50%|14.62%|15.89%|-5.47%|0.00%|TR Hisse %86.8|

## CLAUDE RESEARCH INSTRUCTION

Use this shortlist as STAGE 1 only. For STAGE 2, investigate the highest-ranked candidates using current web research and primary sources where possible.
Verify retail investability, current fund strategy, KAP disclosures, meaningful portfolio exposures, catalysts, major risks, and whether the quantitative move is supported by current market conditions.
Do not recommend a fund solely because it appears in this report.