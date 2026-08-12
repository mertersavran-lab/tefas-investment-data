# TEFAS DAILY QUANTITATIVE SCREEN

- Dataset latest date: **2026-08-12**
- Source dataset generated at: **2026-08-12 07:22:58**
- Total funds in source dataset: **2056**
- RETAIL_CANDIDATE: **607**
- VERIFY_ELIGIBILITY: **1296**
- EXCLUDE: **153**
- Current retail funds with >= 80 observations before completeness filter: **576**
- Quantitatively screenable retail funds after required-data filter: **576**
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
|1|RCV|AZİMUT PORTFÖY BİRİNCİ ÇOKLU VARLIK KATILIM FONU|Katılım|EARLY_MOMENTUM + TREND_CONTINUATION|79.45|3.38%|1.70%|6.24%|0.42%|8.46%|10.40%|-2.04%|0.00%|TR Hisse %15.7|
|2|THF|TERA PORTFÖY HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|77.20|4.60%|2.47%|9.35%|-6.50%|1.21%|19.32%|-11.60%|0.00%|TR Hisse %66.8|
|3|EVM|DENİZ PORTFÖY ENERJİ VE MADENCİLİK SEKTÖRÜ DEĞİŞKEN FON|Enerji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|76.97|4.18%|1.92%|7.39%|-3.64%|1.85%|14.36%|-7.61%|-0.02%|Yabancı ETF %36.4|
|4|TGE|İŞ PORTFÖY EMTİA YABANCI BYF FON SEPETİ FONU|Yabancı Varlıklar|REVERSAL + EARLY_MOMENTUM|76.63|4.86%|0.39%|8.12%|-3.75%|-0.74%|16.00%|-11.76%|-1.55%|Yabancı ETF %94.2|
|5|MKG|AKTİF PORTFÖY ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|76.32|7.90%|0.93%|9.03%|-4.91%|-1.80%|15.55%|-11.71%|-1.81%|Yabancı ETF %18.2|
|6|ICZ|AK PORTFÖY TEKNOLOJİ ŞİRKETLERİ HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Teknoloji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|76.32|2.43%|1.31%|8.87%|-1.97%|7.20%|24.24%|-9.55%|0.00%||
|7|YKT|YAPI KREDİ PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|76.27|8.21%|0.64%|9.05%|-5.28%|-2.40%|16.39%|-12.46%|-2.40%|Kıymetli Maden %23.3|
|8|TUA|TEB PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|75.62|8.19%|0.60%|8.98%|-5.04%|-2.90%|16.33%|-12.92%|-2.90%|Kıymetli Maden %31.7|
|9|KNJ|KUVEYT TÜRK PORTFÖY ENERJİ KATILIM FONU|Enerji|EARLY_MOMENTUM + TREND_CONTINUATION|75.26|3.38%|2.00%|6.28%|0.50%|5.27%|12.87%|-6.67%|0.00%|Yabancı Hisse %69.0|
|10|PTN|PHİLLİP PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|75.00|7.74%|0.69%|8.71%|-5.06%|-1.63%|17.06%|-11.07%|-1.63%|Kıymetli Maden %54.5|
|11|OJK|QNB PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|75.00|7.80%|0.67%|8.83%|-4.52%|-1.66%|16.13%|-11.86%|-1.66%|Kıymetli Maden %36.0|
|12|UP1|ÜNLÜ PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|75.00|7.28%|0.44%|8.28%|-4.24%|-1.71%|14.12%|-10.83%|-1.71%|Kıymetli Maden %64.7|
|13|NJF|NUROL PORTFÖY ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.97|6.62%|0.62%|7.61%|-3.69%|-0.87%|13.95%|-9.97%|-0.87%|Kıymetli Maden %66.5|
|14|KMF|AZİMUT PORTFÖY ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.85|7.32%|0.50%|8.26%|-4.23%|-1.92%|13.96%|-11.17%|-2.06%|Kıymetli Maden %22.4|
|15|HBF|HSBC PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.84|7.68%|0.75%|8.81%|-4.95%|-2.23%|15.68%|-11.83%|-2.23%|Kıymetli Maden %60.9|
|16|FAL|ONE PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.81|7.89%|0.76%|8.43%|-4.85%|-2.26%|15.45%|-11.69%|-2.39%||
|17|KCL|KARE PORTFÖY ÇOKLU VARLIK KATILIM FONU|Katılım|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|74.70|4.18%|-1.04%|5.95%|-3.94%|2.88%|11.89%|-4.69%|0.00%|TR Hisse %48.8|
|18|KZU|KUVEYT TÜRK PORTFÖY İKİNCİ ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.68|8.22%|0.44%|8.73%|-5.03%|-2.06%|18.12%|-11.80%|-2.06%|Kıymetli Maden %85.3|
|19|IPB|İSTANBUL PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|74.65|2.01%|0.29%|4.52%|-1.56%|4.80%|9.75%|-6.76%|0.00%|TR Hisse %56.6|
|20|TTA|İŞ PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.52|7.63%|0.40%|8.28%|-5.51%|-2.43%|16.15%|-11.63%|-2.43%|Kıymetli Maden %60.1|
|21|OVD|QNB PORTFÖY EMTİA FON SEPETİ FONU|Fon Sepeti|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|74.52|4.15%|0.54%|7.87%|-0.42%|0.00%|14.01%|-12.02%|-0.83%|Yabancı Hisse %77.5|
|22|FIB|FİBA PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.50|8.17%|0.83%|8.73%|-5.13%|-2.90%|16.33%|-12.71%|-2.90%|TR Hisse %4.5|
|23|GTA|GARANTİ PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.48|8.06%|0.61%|8.81%|-5.13%|-2.92%|16.73%|-12.89%|-2.92%|Kıymetli Maden %39.4|
|24|HAM|HEDEF PORTFÖY ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.46|7.85%|0.64%|8.77%|-5.42%|-3.59%|16.26%|-13.49%|-3.59%|Kıymetli Maden %87.3|
|25|OIL|OSMANLI PORTFÖY ALTIN FON SEPETİ FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.44|7.53%|0.85%|8.73%|-5.17%|-2.37%|16.57%|-11.84%|-2.37%|Yatırım Fonu %91.8|
|26|AFO|AK PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.44|8.07%|0.61%|8.83%|-5.04%|-2.98%|16.45%|-13.08%|-2.98%||
|27|RJG|RE-PIE PORTFÖY ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.44|7.94%|0.63%|8.83%|-4.85%|-2.48%|16.40%|-12.60%|-2.48%|Kıymetli Maden %37.8|
|28|KUD|KUVEYT TÜRK PORTFÖY DİNAMİK KATILIM FONU|Katılım|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|74.39|2.36%|0.87%|4.04%|-0.39%|7.70%|8.75%|-2.24%|0.00%|TR Hisse %40.1|
|29|PAF|PARDUS PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.34|7.71%|0.78%|9.19%|-4.80%|-2.57%|16.57%|-12.90%|-2.57%|Kıymetli Maden %89.0|
|30|DBA|DENİZ PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.22|7.75%|0.61%|8.66%|-4.79%|-2.44%|16.08%|-12.36%|-2.44%|Kıymetli Maden %35.7|

## CLAUDE RESEARCH INSTRUCTION

Use this shortlist as STAGE 1 only. For STAGE 2, investigate the highest-ranked candidates using current web research and primary sources where possible.
Verify retail investability, current fund strategy, KAP disclosures, meaningful portfolio exposures, catalysts, major risks, and whether the quantitative move is supported by current market conditions.
Do not recommend a fund solely because it appears in this report.