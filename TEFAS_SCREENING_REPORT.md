# TEFAS DAILY QUANTITATIVE SCREEN

- Dataset latest date: **2026-08-20**
- Source dataset generated at: **2026-08-20 06:24:53**
- Total funds in source dataset: **2060**
- RETAIL_CANDIDATE: **609**
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
|1|YHB|YAPI KREDİ PORTFÖY BIST 100 DIŞI ŞİRKETLER HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|85.03|5.92%|3.47%|8.87%|-0.59%|15.91%|17.73%|-8.93%|0.00%|TR Hisse %90.1|
|2|JET|ATA PORTFÖY HAVACILIK VE SAVUNMA TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|83.31|2.63%|0.05%|9.29%|-0.23%|15.83%|22.42%|-6.57%|-1.39%|Yabancı Hisse %67.9|
|3|ARE|İSTANBUL PORTFÖY YABANCI HİSSE SENEDİ FONU|Yabancı Varlıklar|EARLY_MOMENTUM + TREND_CONTINUATION|82.83|2.42%|-0.82%|8.69%|3.44%|11.97%|18.01%|-4.02%|0.00%||
|4|RGD|RE-PIE PORTFÖY AGRESİF DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|82.37|3.41%|1.00%|7.81%|-2.43%|8.85%|13.78%|-6.08%|0.00%|TR Hisse %75.6|
|5|IDI|AZİMUT PORTFÖY İNŞAAT SEKTÖRÜ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|79.23|4.95%|2.79%|7.13%|2.19%|15.41%|26.45%|-7.66%|0.00%||
|6|ICH|PARDUS PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|77.08|2.25%|1.23%|7.29%|5.67%|22.21%|8.10%|-1.05%|0.00%|TR Hisse %52.7|
|7|IKL|İŞ PORTFÖY SAĞLIK ŞİRKETLERİ KARMA FON|Sağlık|EARLY_MOMENTUM + TREND_CONTINUATION|76.97|3.05%|1.02%|6.61%|4.57%|15.35%|12.39%|-2.33%|0.00%||
|8|HJB|HEDEF PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|76.16|1.21%|0.03%|6.27%|1.35%|14.52%|14.00%|-4.71%|0.00%|TR Hisse %63.4|
|9|OHK|OYAK PORTFÖY KATILIM HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|75.56|4.65%|2.88%|5.02%|2.63%|15.19%|17.45%|-4.87%|0.00%||
|10|SOS|HEDEF PORTFÖY SAĞLIK SEKTÖRÜ DEĞİŞKEN FON|Sağlık|TREND_CONTINUATION|74.77|5.96%|3.53%|11.35%|7.41%|23.76%|17.12%|-2.60%|0.00%|Yabancı Hisse %61.4|
|11|FD1|ONE PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|74.50|3.22%|0.49%|4.14%|0.83%|12.54%|11.54%|-2.76%|0.00%|TR Hisse %49.0|
|12|NKT|NUROL PORTFÖY BİRİNCİ KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|74.27|4.34%|1.29%|4.46%|3.69%|16.50%|14.92%|-4.53%|0.00%|TR Hisse %92.0|
|13|DNF|A1 CAPİTAL PORTFÖY DİNAMİK FON SEPETİ FONU|Fon Sepeti|TREND_CONTINUATION|73.77|1.17%|0.96%|6.03%|-0.72%|9.83%|12.82%|-3.31%|0.00%|Yatırım Fonu %83.5|
|14|KPC|KUVEYT TÜRK PORTFÖY KATILIM HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|73.49|4.42%|2.67%|4.05%|1.82%|12.87%|16.35%|-5.14%|0.00%|TR Hisse %87.9|
|15|MTH|MT PORTFÖY BİRİNCİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|73.00|3.73%|2.36%|5.02%|2.39%|26.69%|21.18%|-5.80%|0.00%|TR Hisse %91.2|
|16|BHF|PARDUS PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|72.72|3.64%|0.46%|3.57%|-0.67%|7.05%|16.42%|-6.34%|-0.46%|TR Hisse %46.5|
|17|SSK|DENİZ PORTFÖY SAĞLIK SEKTÖRÜ DEĞİŞKEN FON|Sağlık|TREND_CONTINUATION|72.68|2.93%|2.47%|7.45%|6.07%|18.27%|10.58%|-2.11%|0.00%|Yabancı Hisse %37.7|
|18|KTI|AZİMUT PORTFÖY KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|72.64|3.44%|2.77%|5.06%|2.11%|14.90%|18.53%|-5.11%|0.00%||
|19|AAV|ATA PORTFÖY İKİNCİ HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|72.38|2.94%|0.73%|3.51%|-2.31%|8.63%|15.52%|-7.72%|-1.08%|TR Hisse %87.8|
|20|ZCK|ZİRAAT PORTFÖY AGRESİF KATILIM FONU|Katılım|TREND_CONTINUATION|72.23|4.87%|1.69%|4.62%|3.93%|13.45%|16.19%|-5.35%|0.00%|TR Hisse %85.2|
|21|AFS|AK PORTFÖY SAĞLIK SEKTÖRÜ YABANCI HİSSE SENEDİ FONU|Sağlık|TREND_CONTINUATION|72.18|3.99%|3.71%|11.30%|5.92%|18.50%|19.34%|-4.39%|0.00%||
|22|RPM|ROTA PORTFÖY İLAÇ VE MEDİKAL TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|71.99|3.24%|3.72%|10.15%|4.84%|22.18%|12.59%|-1.72%|0.00%|Yabancı Hisse %61.0|
|23|RBH|ALBARAKA PORTFÖY KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|71.99|5.67%|0.32%|3.42%|2.16%|14.47%|18.02%|-5.89%|0.00%|TR Hisse %98.1|
|24|YEF|YAPI KREDİ PORTFÖY BIST 30 ENDEKSİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|71.71|3.66%|3.20%|4.19%|-3.35%|12.42%|20.22%|-10.57%|-1.06%|TR Hisse %93.0|
|25|BON|A1 CAPİTAL PORTFÖY BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|71.51|0.86%|3.59%|8.62%|0.69%|13.43%|11.16%|-1.48%|0.00%|DİBS %86.8|
|26|GZZ|GARANTİ PORTFÖY FİNANSAL TEKNOLOJİLER DEĞİŞKEN FON|Teknoloji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|71.46|1.01%|-0.97%|3.27%|-0.53%|10.67%|12.90%|-4.38%|-0.75%|Yabancı Hisse %56.3|
|27|TLZ|ATA PORTFÖY KATILIM HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|71.44|4.79%|1.74%|4.07%|3.21%|13.05%|15.65%|-7.06%|0.00%|TR Hisse %89.8|
|28|KUD|KUVEYT TÜRK PORTFÖY DİNAMİK KATILIM FONU|Katılım|TREND_CONTINUATION|71.30|2.24%|2.22%|4.35%|1.88%|12.78%|8.91%|-2.24%|0.00%|TR Hisse %43.9|
|29|GKV|GARANTİ PORTFÖY KATILIM HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|71.07|4.46%|2.36%|3.53%|1.51%|11.75%|19.06%|-7.10%|0.00%|TR Hisse %92.0|
|30|TZD|ZİRAAT PORTFÖY HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|70.97|2.01%|1.43%|4.02%|-2.43%|14.69%|16.52%|-7.97%|-0.52%|TR Hisse %89.7|

## CLAUDE RESEARCH INSTRUCTION

Use this shortlist as STAGE 1 only. For STAGE 2, investigate the highest-ranked candidates using current web research and primary sources where possible.
Verify retail investability, current fund strategy, KAP disclosures, meaningful portfolio exposures, catalysts, major risks, and whether the quantitative move is supported by current market conditions.
Do not recommend a fund solely because it appears in this report.