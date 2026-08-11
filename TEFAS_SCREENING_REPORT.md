# TEFAS DAILY QUANTITATIVE SCREEN

- Dataset latest date: **2026-08-11**
- Source dataset generated at: **2026-08-11 11:18:14**
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
|1|YHZ|YAPI KREDİ PORTFÖY BIST TEKNOLOJİ AĞIRLIK SINIRLAMALI ENDEKSİ HİSSE SENEDİ FONU ( HİSSE SENEDİ YOĞUN FON)|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|79.40|5.40%|-2.23%|8.33%|0.11%|7.58%|29.46%|-10.06%|0.00%|TR Hisse %92.3|
|2|EVM|DENİZ PORTFÖY ENERJİ VE MADENCİLİK SEKTÖRÜ DEĞİŞKEN FON|Enerji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|78.99|5.50%|-0.41%|7.30%|-2.14%|2.03%|14.39%|-7.61%|0.00%|Yabancı ETF %34.1|
|3|RCV|AZİMUT PORTFÖY BİRİNCİ ÇOKLU VARLIK KATILIM FONU|Katılım|EARLY_MOMENTUM + TREND_CONTINUATION|78.17|4.16%|-0.26%|5.99%|1.44%|8.23%|10.52%|-2.04%|0.00%|TR Hisse %15.7|
|4|JET|ATA PORTFÖY HAVACILIK VE SAVUNMA TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|78.16|5.38%|0.68%|8.54%|0.29%|10.73%|18.27%|-6.57%|0.00%|Yabancı Hisse %71.8|
|5|DHT|DENİZ PORTFÖY HAVACILIK VE SAVUNMA TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|77.11|5.16%|1.29%|7.65%|1.47%|13.26%|15.12%|-5.56%|0.00%|Yabancı Hisse %42.9|
|6|BVD|BV PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|76.31|3.87%|1.52%|6.99%|2.92%|13.80%|7.25%|-0.99%|0.00%|TR Hisse %26.2|
|7|IDI|AZİMUT PORTFÖY İNŞAAT SEKTÖRÜ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM|75.52|8.31%|-2.06%|8.67%|-1.86%|-0.41%|23.94%|-10.29%|-0.41%|TR Hisse %83.1|
|8|PAF|PARDUS PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.58|8.02%|-0.65%|8.10%|-1.06%|-2.19%|17.11%|-12.90%|-2.79%|Kıymetli Maden %89.7|
|9|RPG|ROTA PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|74.22|8.60%|-0.59%|8.10%|-0.97%|-1.93%|20.38%|-11.74%|-1.93%|Kıymetli Maden %28.6|
|10|ICZ|AK PORTFÖY TEKNOLOJİ ŞİRKETLERİ HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Teknoloji|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|74.21|4.34%|-3.22%|6.92%|-0.26%|3.55%|24.11%|-11.33%|-0.12%|TR Hisse %87.2|
|11|TTE|İŞ PORTFÖY BIST TEKNOLOJİ AĞIRLIK SINIRLAMALI ENDEKSİ HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|74.02|4.89%|-2.84%|5.12%|0.73%|5.95%|26.54%|-10.37%|0.00%|TR Hisse %87.0|
|12|OIL|OSMANLI PORTFÖY ALTIN FON SEPETİ FONU|Altın|REVERSAL + EARLY_MOMENTUM|73.87|7.64%|-0.55%|7.35%|-1.04%|-2.17%|17.39%|-11.84%|-2.57%|Yatırım Fonu %92.0|
|13|YKT|YAPI KREDİ PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|73.60|7.66%|-0.57%|7.41%|-1.25%|-2.70%|16.91%|-12.46%|-3.09%|Kıymetli Maden %23.5|
|14|KZU|KUVEYT TÜRK PORTFÖY İKİNCİ ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|73.53|7.81%|-0.74%|7.33%|-1.01%|-1.69%|18.60%|-11.80%|-2.58%|Kıymetli Maden %84.5|
|15|DTZ|AK PORTFÖY ROBOTİK TEKNOLOJİLER DEĞİŞKEN FON|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|73.38|6.36%|2.72%|8.90%|1.52%|11.47%|23.43%|-13.30%|-0.48%|Yabancı Hisse %64.6|
|16|CKL|YAPI KREDİ PORTFÖY ÇOKLU VARLIK DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|73.23|6.06%|2.45%|8.32%|-0.35%|4.09%|21.10%|-5.89%|-0.08%|Ters Repo %39.5|
|17|IEV|İŞ PORTFÖY HAVACILIK VE SAVUNMA TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|73.23|3.22%|0.40%|6.06%|0.11%|13.02%|14.07%|-4.89%|0.00%|Yabancı Hisse %61.7|
|18|THF|TERA PORTFÖY HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|73.19|5.78%|1.00%|7.13%|-3.52%|0.19%|20.34%|-11.60%|-0.07%|TR Hisse %81.0|
|19|TEJ|AZİMUT PORTFÖY TEKNOLOJİ FON SEPETİ FONU|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|73.05|6.87%|-0.09%|3.69%|0.73%|10.76%|29.06%|-10.28%|-0.38%|Yabancı ETF %74.8|
|20|GBG|INVEO PORTFÖY G-20 ÜLKELERİ YABANCI HİSSE SENEDİ FONU|Yabancı Varlıklar|EARLY_MOMENTUM + TREND_CONTINUATION|73.01|4.03%|0.64%|4.74%|0.81%|9.01%|14.80%|-4.97%|-0.07%|Yabancı Hisse %83.4|
|21|RJG|RE-PIE PORTFÖY ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|72.87|7.57%|-0.56%|7.35%|-0.94%|-2.34%|17.00%|-12.60%|-2.99%|Kıymetli Maden %37.8|
|22|KZL|KUVEYT TÜRK PORTFÖY ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|72.70|7.67%|-0.65%|7.50%|-1.18%|-2.45%|18.25%|-13.09%|-3.36%|Kıymetli Maden %100.0|
|23|OJK|QNB PORTFÖY ALTIN FONU|Altın|REVERSAL + EARLY_MOMENTUM|72.51|7.32%|-0.51%|7.23%|-0.68%|-1.56%|16.73%|-11.86%|-2.28%|Kıymetli Maden %36.0|
|24|KTI|AZİMUT PORTFÖY KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|72.49|5.21%|-3.11%|4.55%|1.10%|1.10%|18.73%|-8.20%|0.00%|TR Hisse %90.1|
|25|NJF|NUROL PORTFÖY ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|72.48|6.31%|-0.34%|6.45%|-0.45%|-0.59%|14.40%|-9.97%|-1.31%|Kıymetli Maden %66.5|
|26|MKG|AKTİF PORTFÖY ALTIN KATILIM FONU|Altın|REVERSAL + EARLY_MOMENTUM|72.28|7.36%|-0.52%|7.01%|-0.74%|-2.39%|16.30%|-11.71%|-2.64%|Yabancı ETF %18.3|
|27|NUH|NEO PORTFÖY ÜÇÜNCÜ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM|72.12|6.21%|-4.51%|4.45%|-1.20%|-0.97%|22.57%|-12.23%|-1.06%|TR Hisse %92.8|
|28|RUT|BV PORTFÖY ROBOTİK VE UZAY TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|72.08|8.84%|-0.56%|4.28%|0.79%|7.11%|24.05%|-10.31%|-0.12%|Yabancı Hisse %69.2|
|29|ZCN|ZİRAAT PORTFÖY EMTİA FON SEPETİ FONU|Fon Sepeti|REVERSAL + EARLY_MOMENTUM|72.01|4.97%|-0.77%|6.32%|-2.07%|-2.62%|14.97%|-11.75%|-4.05%|Yabancı Hisse %68.6|
|30|OVD|QNB PORTFÖY EMTİA FON SEPETİ FONU|Fon Sepeti|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|72.00|3.40%|-0.94%|7.25%|-1.07%|0.08%|13.79%|-12.02%|-1.87%|Yabancı Hisse %77.7|

## CLAUDE RESEARCH INSTRUCTION

Use this shortlist as STAGE 1 only. For STAGE 2, investigate the highest-ranked candidates using current web research and primary sources where possible.
Verify retail investability, current fund strategy, KAP disclosures, meaningful portfolio exposures, catalysts, major risks, and whether the quantitative move is supported by current market conditions.
Do not recommend a fund solely because it appears in this report.