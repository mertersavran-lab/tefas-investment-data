# TEFAS DAILY QUANTITATIVE SCREEN

- Dataset latest date: **2026-08-17**
- Source dataset generated at: **2026-08-17 08:27:45**
- Total funds in source dataset: **2057**
- RETAIL_CANDIDATE: **607**
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
|1|ICZ|AK PORTFÖY TEKNOLOJİ ŞİRKETLERİ HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Teknoloji|REVERSAL|78.66|6.87%|3.29%|12.37%|-2.97%|13.10%|24.99%|-8.35%|-0.12%|TR Hisse %89.3|
|2|YDP|YAPI KREDİ PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|78.39|4.32%|2.69%|8.05%|-4.51%|7.73%|16.22%|-6.27%|0.00%|TR Hisse %61.0|
|3|YZC|YAPI KREDİ PORTFÖY FİNTECH VE BLOCKCHAİN TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|77.89|4.37%|3.11%|8.65%|-6.26%|8.97%|20.57%|-9.54%|-0.25%|Yabancı Hisse %65.3|
|4|GUH|GARANTİ PORTFÖY YABANCI TEKNOLOJİ HİSSE SENEDİ FONU|Teknoloji|TREND_CONTINUATION|77.59|3.54%|3.47%|9.73%|-8.36%|12.60%|33.77%|-13.11%|-0.94%|Yabancı Hisse %96.3|
|5|IJP|İŞ PORTFÖY BLOCKCHAİN TEKNOLOJİLERİ KARMA FON|Teknoloji|TREND_CONTINUATION|77.00|2.03%|1.81%|7.24%|-4.50%|10.20%|16.07%|-6.00%|0.00%|Yabancı Hisse %66.7|
|6|YAY|YAPI KREDİ PORTFÖY YABANCI TEKNOLOJİ SEKTÖRÜ HİSSE SENEDİ FONU|Teknoloji|REVERSAL + TREND_CONTINUATION|76.89|4.92%|3.80%|11.72%|-10.41%|12.01%|37.53%|-14.42%|-1.07%|Yabancı Hisse %96.4|
|7|ZFB|AK PORTFÖY FİNTEK VE BLOKZİNCİRİ TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|76.86|4.27%|2.49%|9.94%|-5.86%|3.83%|24.35%|-9.15%|-0.11%|Yabancı Hisse %66.7|
|8|TTE|İŞ PORTFÖY BIST TEKNOLOJİ AĞIRLIK SINIRLAMALI ENDEKSİ HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Teknoloji|REVERSAL + TREND_CONTINUATION|75.78|6.58%|3.81%|10.11%|-1.63%|13.12%|27.07%|-8.69%|0.00%|TR Hisse %86.9|
|9|YHZ|YAPI KREDİ PORTFÖY BIST TEKNOLOJİ AĞIRLIK SINIRLAMALI ENDEKSİ HİSSE SENEDİ FONU ( HİSSE SENEDİ YOĞUN FON)|Teknoloji|REVERSAL|75.61|7.17%|4.65%|13.37%|-2.51%|15.34%|29.96%|-8.18%|0.00%|TR Hisse %84.7|
|10|GZZ|GARANTİ PORTFÖY FİNANSAL TEKNOLOJİLER DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|75.29|2.35%|1.61%|5.87%|-3.17%|9.41%|12.77%|-4.38%|0.00%|Yabancı Hisse %56.4|
|11|YHB|YAPI KREDİ PORTFÖY BIST 100 DIŞI ŞİRKETLER HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|75.23|6.96%|2.33%|9.07%|-2.37%|4.98%|17.22%|-8.93%|0.00%|TR Hisse %87.4|
|12|NTI|NEO PORTFÖY TEKNOLOJİ VE İNOVASYON DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|75.19|5.93%|5.82%|7.57%|-13.27%|7.94%|33.67%|-20.97%|-8.02%|Yabancı Hisse %77.5|
|13|THF|TERA PORTFÖY HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|74.31|6.24%|5.33%|11.73%|-5.56%|6.45%|19.51%|-10.30%|0.00%|TR Hisse %68.8|
|14|IDY|TEB PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|74.22|2.49%|0.25%|3.78%|-2.19%|7.96%|9.93%|-3.11%|0.00%|Ters Repo %53.6|
|15|BAG|BULLS PORTFÖY ATAK DEĞIŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|73.89|3.41%|0.88%|5.35%|0.30%|9.67%|13.83%|-5.01%|0.00%|TR Hisse %58.5|
|16|KNJ|KUVEYT TÜRK PORTFÖY ENERJİ KATILIM FONU|Enerji|EARLY_MOMENTUM + TREND_CONTINUATION|73.64|4.38%|2.08%|7.34%|1.83%|6.41%|14.39%|-6.67%|0.00%|Yabancı Hisse %68.2|
|17|MTH|MT PORTFÖY BİRİNCİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|73.36|4.65%|1.87%|5.21%|-0.78%|14.97%|19.05%|-7.62%|0.00%|TR Hisse %91.4|
|18|YTD|YAPI KREDİ PORTFÖY YABANCI FON SEPETİ FONU|Yabancı Varlıklar|TREND_CONTINUATION|72.86|3.45%|4.39%|9.50%|-8.78%|12.12%|14.90%|-11.13%|-2.05%|Yabancı ETF %90.2|
|19|CPT|ROTA PORTFÖY ÇİP TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|72.31|3.84%|3.17%|4.77%|-10.73%|7.56%|29.41%|-16.92%|-7.28%|Yabancı Hisse %67.4|
|20|GBG|INVEO PORTFÖY G-20 ÜLKELERİ YABANCI HİSSE SENEDİ FONU|Yabancı Varlıklar|TREND_CONTINUATION|71.66|2.34%|3.23%|7.58%|-3.70%|12.19%|13.68%|-4.97%|0.00%|Yabancı Hisse %83.8|
|21|IJB|İŞ PORTFÖY DİJİTAL OYUN SEKTÖRÜ KARMA FON|Diğer / Belirsiz|TREND_CONTINUATION|70.19|2.70%|2.84%|9.83%|3.50%|13.17%|18.16%|-4.45%|0.00%|Yabancı Hisse %61.5|
|22|YPV|YAPI KREDİ PORTFÖY ÜÇÜNCÜ FON SEPETİ FONU|Fon Sepeti|TREND_CONTINUATION|70.17|2.70%|2.62%|6.11%|-4.81%|2.42%|13.62%|-5.73%|0.00%|Yatırım Fonu %94.1|
|23|BON|A1 CAPİTAL PORTFÖY BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|69.89|2.32%|3.38%|8.27%|0.66%|12.53%|11.29%|-1.48%|0.00%|DİBS %53.2|
|24|FUA|AK PORTFÖY İHRACATÇI ŞİRKETLER HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|69.31|5.43%|1.41%|5.69%|-3.51%|0.12%|18.65%|-8.20%|0.00%|TR Hisse %86.0|
|25|KCL|KARE PORTFÖY ÇOKLU VARLIK KATILIM FONU|Katılım|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|68.25|3.13%|1.73%|5.39%|-1.17%|5.28%|12.57%|-3.94%|0.00%|TR Hisse %49.4|
|26|FNO|QNB PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|68.05|2.01%|1.06%|3.70%|-0.59%|6.58%|7.46%|-1.15%|0.00%|TR Hisse %30.1|
|27|YAC|YAPI KREDİ PORTFÖY İKİNCİ FON SEPETİ FONU|Fon Sepeti|TREND_CONTINUATION|67.83|2.07%|2.15%|5.39%|-2.73%|4.37%|9.32%|-3.24%|0.00%|Yatırım Fonu %97.2|
|28|GRT|GARANTİ PORTFÖY TEKNOLOJİ ŞİRKETLERİ HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Teknoloji|REVERSAL + EARLY_MOMENTUM|67.81|4.42%|3.09%|5.05%|-9.65%|-2.26%|24.92%|-18.81%|-10.07%|TR Hisse %96.4|
|29|BDY|AK PORTFÖY BIST 100 DIŞI ŞİRKETLER HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|67.40|3.43%|1.10%|3.44%|-2.17%|3.75%|13.52%|-6.37%|0.00%|TR Hisse %88.4|
|30|RGD|RE-PIE PORTFÖY AGRESİF DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|67.21|2.58%|0.05%|3.07%|-1.98%|6.86%|12.42%|-6.08%|0.00%|TR Hisse %79.2|

## CLAUDE RESEARCH INSTRUCTION

Use this shortlist as STAGE 1 only. For STAGE 2, investigate the highest-ranked candidates using current web research and primary sources where possible.
Verify retail investability, current fund strategy, KAP disclosures, meaningful portfolio exposures, catalysts, major risks, and whether the quantitative move is supported by current market conditions.
Do not recommend a fund solely because it appears in this report.