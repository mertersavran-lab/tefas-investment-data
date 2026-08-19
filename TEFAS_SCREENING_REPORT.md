# TEFAS DAILY QUANTITATIVE SCREEN

- Dataset latest date: **2026-08-19**
- Source dataset generated at: **2026-08-19 08:09:03**
- Total funds in source dataset: **2058**
- RETAIL_CANDIDATE: **608**
- VERIFY_ELIGIBILITY: **1297**
- EXCLUDE: **153**
- Current retail funds with >= 80 observations before completeness filter: **577**
- Quantitatively screenable retail funds after required-data filter: **577**
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
|1|THF|TERA PORTFÖY HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL|78.53|6.70%|4.60%|12.67%|-2.88%|12.59%|19.52%|-7.85%|0.00%|TR Hisse %75.9|
|2|YDP|YAPI KREDİ PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|78.10|3.70%|0.55%|5.57%|-3.75%|9.01%|16.23%|-6.27%|-0.84%|TR Hisse %61.0|
|3|RGD|RE-PIE PORTFÖY AGRESİF DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|77.72|3.52%|-1.53%|4.75%|-2.68%|7.20%|11.50%|-6.08%|0.00%|TR Hisse %78.9|
|4|YAY|YAPI KREDİ PORTFÖY YABANCI TEKNOLOJİ SEKTÖRÜ HİSSE SENEDİ FONU|Teknoloji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|77.16|3.20%|-0.96%|4.55%|-6.90%|10.64%|38.55%|-14.42%|-3.28%|Yabancı Hisse %96.4|
|5|YHB|YAPI KREDİ PORTFÖY BIST 100 DIŞI ŞİRKETLER HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|77.14|5.42%|2.19%|7.85%|-1.68%|8.06%|17.35%|-8.93%|-0.91%|TR Hisse %88.7|
|6|DNF|A1 CAPİTAL PORTFÖY DİNAMİK FON SEPETİ FONU|Fon Sepeti|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|75.21|1.22%|-0.62%|6.46%|-2.40%|8.22%|12.76%|-3.31%|0.00%|Yatırım Fonu %94.7|
|7|YZC|YAPI KREDİ PORTFÖY FİNTECH VE BLOCKCHAİN TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|74.91|3.40%|0.48%|4.62%|-4.03%|8.65%|21.96%|-9.54%|-2.16%|Yabancı Hisse %65.0|
|8|HJB|HEDEF PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|73.83|1.58%|-1.70%|7.65%|-1.87%|4.85%|15.29%|-7.73%|-0.15%|TR Hisse %57.0|
|9|NTI|NEO PORTFÖY TEKNOLOJİ VE İNOVASYON DEĞİŞKEN FON|Teknoloji|REVERSAL + TREND_CONTINUATION|73.19|3.30%|1.59%|5.51%|-14.08%|6.98%|35.49%|-20.97%|-9.35%|Yabancı Hisse %78.9|
|10|MTH|MT PORTFÖY BİRİNCİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|73.01|3.72%|-1.22%|3.33%|-0.08%|18.15%|19.77%|-5.80%|-1.29%|TR Hisse %81.5|
|11|PBI|PARDUS PORTFÖY BİRİNCİ FON SEPETİ FONU|Fon Sepeti|EARLY_MOMENTUM + TREND_CONTINUATION|72.92|1.85%|0.81%|4.54%|1.23%|11.38%|8.80%|-3.07%|0.00%|Yatırım Fonu %87.7|
|12|GZZ|GARANTİ PORTFÖY FİNANSAL TEKNOLOJİLER DEĞİŞKEN FON|Teknoloji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|70.81|1.34%|-0.92%|3.38%|-2.82%|8.46%|12.92%|-4.38%|-1.03%|Yabancı Hisse %56.8|
|13|ICH|PARDUS PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|70.49|1.42%|1.02%|6.64%|4.29%|17.89%|7.51%|-2.36%|0.00%|TR Hisse %53.3|
|14|AED|ATA PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|69.73|3.10%|1.95%|4.86%|-0.37%|6.93%|13.91%|-4.74%|0.00%|TR Hisse %55.9|
|15|CKF|ALBARAKA PORTFÖY ÇOKLU VARLIK KATILIM FONU|Katılım|TREND_CONTINUATION|69.14|1.94%|1.47%|4.01%|-1.35%|8.36%|14.76%|-4.88%|-0.91%|Yabancı Hisse %38.7|
|16|BON|A1 CAPİTAL PORTFÖY BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|68.55|0.95%|1.79%|8.40%|0.46%|13.38%|11.24%|-1.48%|0.00%|DİBS %75.6|
|17|FSU|TERA PORTFÖY FON SEPETİ FONU|Fon Sepeti|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|68.06|5.03%|2.96%|6.41%|-4.70%|0.14%|18.49%|-11.21%|-0.61%|Yatırım Fonu %45.5|
|18|FNO|QNB PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|67.51|1.78%|0.67%|3.30%|0.01%|7.33%|7.53%|-1.15%|-0.23%|TR Hisse %29.6|
|19|KTI|AZİMUT PORTFÖY KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|67.48|3.23%|1.68%|3.47%|-0.47%|7.21%|16.94%|-5.11%|-0.50%|TR Hisse %86.2|
|20|OHK|OYAK PORTFÖY KATILIM HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|67.22|4.04%|1.95%|3.33%|0.82%|7.31%|15.68%|-4.87%|0.00%|TR Hisse %74.0|
|21|AN1|STRATEJİ PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|67.15|2.47%|-0.27%|1.96%|0.42%|12.80%|8.57%|-3.87%|0.00%|TR Hisse %47.8|
|22|YPV|YAPI KREDİ PORTFÖY ÜÇÜNCÜ FON SEPETİ FONU|Fon Sepeti|TREND_CONTINUATION|66.85|2.31%|1.50%|4.16%|-3.01%|3.66%|13.75%|-5.73%|-0.77%|Yatırım Fonu %94.2|
|23|TE3|TEB PORTFÖY MUTLAK GETİRİ HEDEFLİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|66.69|1.90%|1.64%|3.56%|-2.00%|4.64%|8.38%|-3.89%|0.00%|Ters Repo %39.2|
|24|YEF|YAPI KREDİ PORTFÖY BIST 30 ENDEKSİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|66.01|4.07%|0.06%|2.65%|-5.62%|3.14%|18.30%|-10.57%|-3.73%|TR Hisse %92.3|
|25|OPB|OSMANLI PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|65.92|1.84%|1.80%|3.62%|-0.23%|7.27%|7.75%|-2.40%|0.00%|ETF %39.2|
|26|FFH|QNB PORTFÖY ÇOKLU VARLIK KATILIM FONU|Katılım|TREND_CONTINUATION|65.65|1.80%|1.22%|3.46%|0.98%|7.02%|5.24%|-1.76%|-0.04%|TR Hisse %28.6|
|27|YAC|YAPI KREDİ PORTFÖY İKİNCİ FON SEPETİ FONU|Fon Sepeti|TREND_CONTINUATION|65.64|1.70%|1.50%|3.96%|-1.37%|5.37%|9.38%|-3.24%|-0.49%|Yatırım Fonu %97.3|
|28|KUD|KUVEYT TÜRK PORTFÖY DİNAMİK KATILIM FONU|Katılım|TREND_CONTINUATION|65.14|1.87%|2.36%|4.23%|0.70%|9.91%|8.78%|-2.24%|-0.14%|TR Hisse %40.8|
|29|FI3|QNB PORTFÖY BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|65.07|1.06%|0.36%|3.23%|0.29%|8.41%|4.67%|-1.80%|-0.07%|DİBS %88.7|
|30|KDE|KUVEYT TÜRK PORTFÖY DENGELİ KATILIM FONU|Katılım|TREND_CONTINUATION|64.66|1.45%|1.69%|3.70%|1.08%|10.95%|4.78%|-1.31%|0.00%|TR Hisse %17.7|

## CLAUDE RESEARCH INSTRUCTION

Use this shortlist as STAGE 1 only. For STAGE 2, investigate the highest-ranked candidates using current web research and primary sources where possible.
Verify retail investability, current fund strategy, KAP disclosures, meaningful portfolio exposures, catalysts, major risks, and whether the quantitative move is supported by current market conditions.
Do not recommend a fund solely because it appears in this report.