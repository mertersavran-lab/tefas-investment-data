# TEFAS DAILY QUANTITATIVE SCREEN

- Dataset latest date: **2026-08-14**
- Source dataset generated at: **2026-08-14 09:48:11**
- Total funds in source dataset: **2057**
- RETAIL_CANDIDATE: **607**
- VERIFY_ELIGIBILITY: **1297**
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
|1|RCV|AZİMUT PORTFÖY BİRİNCİ ÇOKLU VARLIK KATILIM FONU|Katılım|TREND_CONTINUATION|80.68|3.24%|2.64%|6.29%|0.98%|8.48%|11.05%|-2.04%|-0.45%|TR Hisse %15.7|
|2|DGF|A1 CAPİTAL PORTFÖY DEĞİŞKEN FON|Değişken|REVERSAL + TREND_CONTINUATION|79.04|4.16%|2.92%|10.82%|-3.60%|6.55%|13.11%|-5.86%|0.00%|Özel Sektör Borçlanma %0.0|
|3|TTE|İŞ PORTFÖY BIST TEKNOLOJİ AĞIRLIK SINIRLAMALI ENDEKSİ HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Teknoloji|TREND_CONTINUATION|76.58|6.59%|6.91%|9.12%|-1.81%|11.26%|27.26%|-9.75%|0.00%|TR Hisse %87.4|
|4|IJB|İŞ PORTFÖY DİJİTAL OYUN SEKTÖRÜ KARMA FON|Diğer / Belirsiz|EARLY_MOMENTUM + TREND_CONTINUATION|75.77|2.23%|0.35%|7.02%|3.22%|10.49%|17.52%|-4.45%|-0.85%|Yabancı Hisse %60.7|
|5|YHB|YAPI KREDİ PORTFÖY BIST 100 DIŞI ŞİRKETLER HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|75.66|5.81%|2.59%|6.75%|-1.25%|1.54%|16.28%|-9.15%|0.00%|TR Hisse %90.5|
|6|PGD|ASTRA PORTFÖY AGRESİF DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|74.13|1.00%|-0.25%|3.06%|-0.35%|9.92%|5.75%|-2.60%|0.00%|TR Hisse %58.9|
|7|BON|A1 CAPİTAL PORTFÖY BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|74.08|2.91%|4.10%|8.12%|0.83%|12.38%|11.32%|-1.48%|0.00%|DİBS %56.7|
|8|RGD|RE-PIE PORTFÖY AGRESİF DEĞİŞKEN FON|Değişken|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|73.13|1.82%|0.26%|4.71%|-2.39%|4.81%|14.17%|-6.08%|0.00%|TR Hisse %78.5|
|9|THF|TERA PORTFÖY HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|72.73|6.82%|6.32%|10.31%|-3.46%|4.04%|19.81%|-11.60%|0.00%|TR Hisse %66.2|
|10|OVD|QNB PORTFÖY EMTİA FON SEPETİ FONU|Fon Sepeti|EARLY_MOMENTUM + TREND_CONTINUATION|72.70|3.79%|-0.21%|5.97%|1.47%|0.11%|12.97%|-11.30%|-0.26%|Yabancı Hisse %76.9|
|11|ZCN|ZİRAAT PORTFÖY EMTİA FON SEPETİ FONU|Fon Sepeti|REVERSAL + EARLY_MOMENTUM|72.10|3.03%|1.08%|6.24%|-2.52%|-1.86%|14.71%|-10.34%|-1.86%|Yabancı Hisse %64.4|
|12|YTD|YAPI KREDİ PORTFÖY YABANCI FON SEPETİ FONU|Yabancı Varlıklar|TREND_CONTINUATION|71.26|3.72%|4.49%|6.21%|-5.08%|8.29%|17.81%|-11.13%|-2.74%|Yabancı ETF %90.1|
|13|ARE|İSTANBUL PORTFÖY YABANCI HİSSE SENEDİ FONU|Yabancı Varlıklar|TREND_CONTINUATION|71.15|1.68%|1.91%|6.71%|2.25%|8.83%|16.83%|-4.02%|-0.30%|Yabancı Hisse %79.7|
|14|TGE|İŞ PORTFÖY EMTİA YABANCI BYF FON SEPETİ FONU|Yabancı Varlıklar|REVERSAL + EARLY_MOMENTUM|71.02|3.29%|-0.25%|4.78%|-0.73%|-1.40%|15.18%|-11.38%|-1.75%|Yabancı ETF %94.0|
|15|CPT|ROTA PORTFÖY ÇİP TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|71.00|4.42%|4.12%|3.28%|-5.93%|5.81%|30.50%|-16.92%|-6.52%|Yabancı Hisse %67.6|
|16|KUD|KUVEYT TÜRK PORTFÖY DİNAMİK KATILIM FONU|Katılım|TREND_CONTINUATION|70.38|1.93%|2.31%|3.62%|0.66%|8.10%|8.72%|-2.24%|-0.11%|TR Hisse %38.9|
|17|SGT|GARANTİ PORTFÖY SİBER GÜVENLİK TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|70.35|5.85%|6.04%|7.95%|6.35%|25.00%|23.74%|-7.73%|0.00%|Yabancı Hisse %57.9|
|18|BTE|BV PORTFÖY OYUN VE TEKNOLOJİ DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|69.10|2.36%|4.34%|7.63%|0.83%|16.80%|13.15%|-7.18%|-0.39%|Yabancı Hisse %70.2|
|19|KCL|KARE PORTFÖY ÇOKLU VARLIK KATILIM FONU|Katılım|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|69.05|2.30%|1.27%|4.03%|-1.64%|2.81%|11.59%|-4.62%|-0.14%|TR Hisse %48.7|
|20|GUH|GARANTİ PORTFÖY YABANCI TEKNOLOJİ HİSSE SENEDİ FONU|Teknoloji|TREND_CONTINUATION|68.95|4.51%|5.47%|5.23%|-3.79%|10.81%|36.96%|-13.11%|-1.32%|Yabancı Hisse %96.2|
|21|DID|DENİZ PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|68.76|1.83%|2.96%|5.66%|0.19%|7.24%|7.90%|-2.68%|0.00%|Ters Repo %43.5|
|22|EKF|ASTRA PORTFÖY KİRA SERTİFİKASI KATILIM (TL) FONU|Katılım|TREND_CONTINUATION|68.45|0.75%|0.77%|3.11%|-0.84%|6.24%|1.42%|-3.86%|-0.55%|Özel Sektör Borçlanma %0.0|
|23|HPO|HSBC PORTFÖY ÇOKLU VARLIK BİRİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|68.18|1.02%|1.22%|3.23%|1.23%|8.59%|2.50%|-0.35%|0.00%|Ters Repo %29.1|
|24|IDY|TEB PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|68.00|2.08%|1.15%|2.16%|-0.77%|5.49%|10.12%|-3.11%|-0.00%|Ters Repo %54.8|
|25|IJZ|İŞ PORTFÖY SİBER GÜVENLİK TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|67.77|5.12%|6.40%|7.80%|4.50%|23.41%|22.79%|-7.95%|0.00%|Yabancı Hisse %66.3|
|26|KTJ|KUVEYT TÜRK PORTFÖY TEKNOLOJİ KATILIM FONU|Teknoloji|TREND_CONTINUATION|67.68|3.85%|5.58%|7.28%|-2.39%|14.53%|26.63%|-9.76%|0.00%|Yabancı Hisse %76.3|
|27|ZFB|AK PORTFÖY FİNTEK VE BLOKZİNCİRİ TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|67.55|4.05%|4.99%|6.70%|-2.78%|2.06%|26.88%|-9.15%|-0.34%|Yabancı Hisse %66.8|
|28|GLS|AZİMUT PORTFÖY  KİRA SERTİFİKALARI (SUKUK) KATILIM FONU|Katılım|TREND_CONTINUATION|67.29|0.98%|0.69%|3.13%|2.74%|9.42%|1.83%|0.00%|0.00%|Yatırım Fonu %6.4|
|29|YAC|YAPI KREDİ PORTFÖY İKİNCİ FON SEPETİ FONU|Fon Sepeti|TREND_CONTINUATION|67.24|2.12%|2.77%|4.12%|-1.37%|3.12%|10.09%|-3.24%|0.00%|Yatırım Fonu %97.2|
|30|PTO|PARDUS PORTFÖY TEMETTÜ ÖDEYEN ŞİRKETLER HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|67.23|0.67%|0.66%|9.44%|8.61%|24.83%|14.57%|-1.98%|-0.47%|TR Hisse %87.5|

## CLAUDE RESEARCH INSTRUCTION

Use this shortlist as STAGE 1 only. For STAGE 2, investigate the highest-ranked candidates using current web research and primary sources where possible.
Verify retail investability, current fund strategy, KAP disclosures, meaningful portfolio exposures, catalysts, major risks, and whether the quantitative move is supported by current market conditions.
Do not recommend a fund solely because it appears in this report.