# TEFAS DAILY QUANTITATIVE SCREEN

- Dataset latest date: **2026-08-13**
- Source dataset generated at: **2026-08-13 07:19:45**
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
|1|TTE|İŞ PORTFÖY BIST TEKNOLOJİ AĞIRLIK SINIRLAMALI ENDEKSİ HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Teknoloji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|82.35|5.79%|3.12%|9.14%|-2.64%|13.13%|27.27%|-9.75%|0.00%|TR Hisse %87.2|
|2|BON|A1 CAPİTAL PORTFÖY BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|80.72|3.59%|3.27%|8.15%|0.91%|11.89%|11.31%|-1.48%|0.00%|DİBS %66.4|
|3|YHZ|YAPI KREDİ PORTFÖY BIST TEKNOLOJİ AĞIRLIK SINIRLAMALI ENDEKSİ HİSSE SENEDİ FONU ( HİSSE SENEDİ YOĞUN FON)|Teknoloji|REVERSAL|79.58|6.41%|4.07%|12.44%|-3.10%|15.57%|30.17%|-9.34%|0.00%|TR Hisse %89.9|
|4|RCV|AZİMUT PORTFÖY BİRİNCİ ÇOKLU VARLIK KATILIM FONU|Katılım|TREND_CONTINUATION|79.42|3.65%|2.84%|6.89%|0.80%|9.21%|10.71%|-2.04%|0.00%|TR Hisse %16.4|
|5|DGF|A1 CAPİTAL PORTFÖY DEĞİŞKEN FON|Değişken|REVERSAL + TREND_CONTINUATION|78.01|4.63%|3.15%|11.04%|-4.00%|6.92%|13.04%|-5.86%|0.00%|Özel Sektör Borçlanma %0.0|
|6|ICZ|AK PORTFÖY TEKNOLOJİ ŞİRKETLERİ HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Teknoloji|REVERSAL + TREND_CONTINUATION|77.96|4.97%|2.80%|11.30%|-3.49%|11.83%|24.72%|-9.55%|0.00%||
|7|IPB|İSTANBUL PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|76.97|2.35%|1.29%|5.01%|-1.82%|7.07%|9.96%|-6.37%|0.00%|TR Hisse %56.5|
|8|BLT|BULLS PORTFÖY ALTIN FONU|Altın|EARLY_MOMENTUM + TREND_CONTINUATION|76.64|5.03%|2.18%|9.81%|0.37%|6.03%|15.34%|-11.40%|0.00%|Kıymetli Maden %86.0|
|9|IJB|İŞ PORTFÖY DİJİTAL OYUN SEKTÖRÜ KARMA FON|Diğer / Belirsiz|EARLY_MOMENTUM + TREND_CONTINUATION|76.58|2.56%|-0.04%|8.10%|2.73%|10.42%|17.54%|-4.45%|-0.74%|Yabancı Hisse %59.9|
|10|NJF|NUROL PORTFÖY ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|75.27|5.11%|3.26%|9.41%|-5.39%|0.32%|13.28%|-9.69%|0.00%|Kıymetli Maden %66.5|
|11|KMF|AZİMUT PORTFÖY ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|75.19|5.69%|3.20%|9.74%|-5.74%|-1.27%|13.56%|-11.17%|-1.27%|Kıymetli Maden %23.0|
|12|KOT|AZİMUT PORTFÖY KOÇ TOPLULUĞU ŞİRKETLERİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|75.18|5.91%|1.43%|6.98%|-1.90%|4.38%|26.22%|-7.84%|0.00%|TR Hisse %97.5|
|13|THF|TERA PORTFÖY HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + TREND_CONTINUATION|74.61|6.46%|3.60%|10.36%|-6.01%|4.06%|19.85%|-11.60%|0.00%|TR Hisse %60.7|
|14|TGE|İŞ PORTFÖY EMTİA YABANCI BYF FON SEPETİ FONU|Yabancı Varlıklar|REVERSAL + EARLY_MOMENTUM|74.48|5.22%|-0.22%|6.18%|-0.69%|-1.08%|14.33%|-11.76%|-1.08%|Yabancı ETF %94.0|
|15|UP1|ÜNLÜ PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.34|5.49%|3.51%|9.70%|-5.42%|-0.70%|13.86%|-10.69%|-0.70%|Kıymetli Maden %64.2|
|16|OPL|OSMANLI PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|74.25|3.24%|2.43%|5.98%|-2.03%|2.28%|8.09%|-5.76%|0.00%|ETF %17.9|
|17|TRO|TRIVE PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|73.64|5.41%|3.44%|9.79%|-6.15%|-1.22%|15.04%|-11.21%|-1.24%||
|18|BTE|BV PORTFÖY OYUN VE TEKNOLOJİ DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|73.50|3.14%|4.22%|7.61%|0.43%|17.11%|13.16%|-7.18%|-0.33%|Yabancı Hisse %70.6|
|19|OHK|OYAK PORTFÖY KATILIM HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|73.09|2.88%|0.80%|4.54%|-2.71%|3.23%|18.86%|-7.46%|0.00%||
|20|YHB|YAPI KREDİ PORTFÖY BIST 100 DIŞI ŞİRKETLER HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|73.06|3.47%|2.75%|5.99%|-3.85%|1.32%|15.40%|-9.15%|-1.47%|TR Hisse %94.8|
|21|FAL|ONE PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|72.07|5.76%|4.09%|9.47%|-6.05%|-1.77%|15.22%|-11.69%|-1.77%|Kıymetli Maden %44.2|
|22|KTI|AZİMUT PORTFÖY KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|71.91|2.77%|2.37%|6.18%|-2.17%|3.45%|19.82%|-7.61%|0.00%|TR Hisse %84.7|
|23|RPM|ROTA PORTFÖY İLAÇ VE MEDİKAL TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|71.78|3.48%|1.35%|6.99%|5.82%|15.72%|11.51%|-3.06%|0.00%|Yabancı Hisse %61.0|
|24|NUH|NEO PORTFÖY ÜÇÜNCÜ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|71.73|3.53%|0.79%|4.10%|-2.98%|4.16%|22.23%|-10.36%|-1.01%|TR Hisse %92.7|
|25|PGD|ASTRA PORTFÖY AGRESİF DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|71.67|1.42%|-1.28%|3.04%|-0.60%|9.90%|5.75%|-2.60%|-0.08%|TR Hisse %59.7|
|26|PTN|PHİLLİP PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|71.64|5.34%|4.29%|9.73%|-5.47%|-0.65%|17.00%|-10.92%|-0.65%|Kıymetli Maden %54.6|
|27|AFS|AK PORTFÖY SAĞLIK SEKTÖRÜ YABANCI HİSSE SENEDİ FONU|Sağlık|EARLY_MOMENTUM + TREND_CONTINUATION|71.54|3.71%|-0.77%|7.49%|4.81%|13.97%|18.39%|-4.39%|-1.20%||
|28|NAU|NEO PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|71.51|5.18%|3.32%|9.57%|-6.82%|-2.94%|14.56%|-12.67%|-3.00%|Kıymetli Maden %73.2|
|29|KCL|KARE PORTFÖY ÇOKLU VARLIK KATILIM FONU|Katılım|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|71.45|2.80%|0.99%|4.94%|-3.00%|3.85%|11.78%|-4.62%|-0.11%|TR Hisse %48.7|
|30|OJK|QNB PORTFÖY ALTIN FONU|Altın|REVERSAL|71.36|6.04%|3.55%|10.89%|-6.63%|-0.55%|15.26%|-11.64%|-0.57%|Kıymetli Maden %35.6|

## CLAUDE RESEARCH INSTRUCTION

Use this shortlist as STAGE 1 only. For STAGE 2, investigate the highest-ranked candidates using current web research and primary sources where possible.
Verify retail investability, current fund strategy, KAP disclosures, meaningful portfolio exposures, catalysts, major risks, and whether the quantitative move is supported by current market conditions.
Do not recommend a fund solely because it appears in this report.