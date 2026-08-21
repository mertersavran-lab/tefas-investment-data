# TEFAS DAILY QUANTITATIVE SCREEN

- Dataset latest date: **2026-08-21**
- Source dataset generated at: **2026-08-21 07:09:01**
- Total funds in source dataset: **2062**
- RETAIL_CANDIDATE: **611**
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
|1|GZG|GARANTİ PORTFÖY SAĞLIK VE GENETİK TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|84.56|4.18%|2.88%|8.64%|3.11%|23.62%|13.29%|-3.07%|0.00%|Yabancı Hisse %65.5|
|2|RPM|ROTA PORTFÖY İLAÇ VE MEDİKAL TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|TREND_CONTINUATION|81.31|3.75%|3.55%|9.78%|4.03%|21.03%|12.55%|-1.72%|0.00%|Yabancı Hisse %60.4|
|3|IKL|İŞ PORTFÖY SAĞLIK ŞİRKETLERİ KARMA FON|Sağlık|EARLY_MOMENTUM + TREND_CONTINUATION|80.07|2.73%|1.43%|7.31%|3.21%|13.71%|12.07%|-2.33%|0.00%|Yabancı Hisse %68.2|
|4|ICH|PARDUS PORTFÖY İKİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|79.53|2.68%|1.23%|7.77%|5.47%|21.19%|8.17%|-1.05%|0.00%|TR Hisse %55.6|
|5|SSK|DENİZ PORTFÖY SAĞLIK SEKTÖRÜ DEĞİŞKEN FON|Sağlık|TREND_CONTINUATION|77.10|2.70%|2.42%|8.20%|4.42%|16.98%|10.13%|-2.11%|0.00%|Yabancı Hisse %36.7|
|6|CVL|A1 CAPİTAL PORTFÖY ÇOKLU VARLIK KATILIM FONU|Katılım|EARLY_MOMENTUM + TREND_CONTINUATION|75.55|5.38%|1.73%|5.77%|4.36%|10.49%|14.38%|-3.08%|0.00%|TR Hisse %30.9|
|7|DNF|A1 CAPİTAL PORTFÖY DİNAMİK FON SEPETİ FONU|Fon Sepeti|TREND_CONTINUATION|75.46|1.65%|1.09%|6.64%|-0.16%|8.99%|12.78%|-3.31%|0.00%|Yatırım Fonu %90.8|
|8|KUD|KUVEYT TÜRK PORTFÖY DİNAMİK KATILIM FONU|Katılım|TREND_CONTINUATION|75.26|2.31%|1.93%|5.03%|1.32%|10.58%|8.30%|-2.24%|-0.05%|TR Hisse %43.1|
|9|FNO|QNB PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|74.65|1.99%|1.19%|4.80%|0.30%|9.14%|8.38%|-1.15%|-0.03%|TR Hisse %29.8|
|10|TBT|TEB PORTFÖY BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|73.66|1.17%|0.69%|4.54%|-1.29%|11.85%|6.25%|-3.48%|0.00%|DİBS %94.3|
|11|FIT|FİBA PORTFÖY BORÇLANMA ARAÇLARI (TL) FONU|Borçlanma Araçları|TREND_CONTINUATION|73.39|1.17%|0.74%|4.56%|-1.24%|11.69%|6.13%|-3.48%|0.00%|DİBS %92.5|
|12|ECA|GLOBAL MD PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|73.35|2.14%|1.65%|5.61%|2.24%|19.31%|15.80%|-4.34%|0.00%|TR Hisse %57.0|
|13|RGD|RE-PIE PORTFÖY AGRESİF DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|73.26|2.22%|1.82%|6.38%|-1.93%|9.07%|14.60%|-6.08%|-0.98%|TR Hisse %75.3|
|14|DUV|DENİZ PORTFÖY UZUN VADELİ BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|73.09|1.17%|0.73%|4.35%|-0.67%|12.16%|4.85%|-2.80%|0.00%|DİBS %99.1|
|15|NKT|NUROL PORTFÖY BİRİNCİ KATILIM HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|72.69|4.98%|0.19%|4.99%|4.46%|12.22%|14.76%|-4.53%|0.00%|TR Hisse %93.7|
|16|FD1|ONE PORTFÖY BİRİNCİ DEĞİŞKEN FON|Değişken|EARLY_MOMENTUM + TREND_CONTINUATION|72.54|2.60%|0.56%|4.35%|0.48%|11.20%|11.41%|-2.76%|-0.26%|TR Hisse %50.1|
|17|GUV|GARANTİ PORTFÖY UZUN VADELİ BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|72.17|1.08%|0.77%|4.39%|-0.82%|12.18%|5.87%|-2.94%|0.00%|DİBS %99.8|
|18|ACC|İSTANBUL PORTFÖY DÖRDÜNCÜ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN)|Hisse Senedi|REVERSAL + EARLY_MOMENTUM + TREND_CONTINUATION|71.99|2.53%|1.28%|5.32%|-6.31%|3.78%|13.52%|-9.98%|-3.12%|TR Hisse %81.1|
|19|YVB|YAPI KREDİ PORTFÖY UZUN VADELİ BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|71.93|1.20%|0.69%|4.21%|0.19%|12.38%|5.22%|-2.18%|0.00%|DİBS %90.1|
|20|PHI|PİRAMİT PORTFÖY HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|71.33|2.77%|0.04%|3.87%|1.03%|9.02%|14.32%|-5.37%|0.00%|TR Hisse %92.2|
|21|OBI|OYAK PORTFÖY İKİNCİ BORÇLANMA ARAÇLARI (TL) FONU|Borçlanma Araçları|TREND_CONTINUATION|71.29|1.17%|0.67%|4.20%|0.96%|10.41%|4.31%|-0.82%|0.00%||
|22|PGD|ASTRA PORTFÖY AGRESİF DEĞİŞKEN FON|Değişken|TREND_CONTINUATION|71.23|1.68%|1.00%|3.56%|0.57%|10.29%|5.84%|-2.60%|0.00%|TR Hisse %56.8|
|23|MTH|MT PORTFÖY BİRİNCİ HİSSE SENEDİ FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|TREND_CONTINUATION|70.61|3.81%|3.46%|6.73%|3.60%|23.52%|21.03%|-5.80%|0.00%|TR Hisse %90.5|
|24|JET|ATA PORTFÖY HAVACILIK VE SAVUNMA TEKNOLOJİLERİ DEĞİŞKEN FON|Teknoloji|EARLY_MOMENTUM + TREND_CONTINUATION|70.57|1.88%|0.16%|7.06%|3.81%|13.18%|22.01%|-6.57%|-1.70%|Yabancı Hisse %67.8|
|25|YOT|YAPI KREDİ PORTFÖY BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|70.35|1.10%|0.69%|4.07%|0.84%|11.69%|4.04%|-1.32%|0.00%|DİBS %90.2|
|26|AK2|AK PORTFÖY UZUN VADELİ BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|69.99|1.06%|0.87%|4.27%|-0.35%|10.68%|4.86%|-2.36%|0.00%||
|27|APT|AK PORTFÖY ORTA VADELI BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|69.93|1.14%|0.76%|4.21%|0.91%|11.51%|4.34%|-1.43%|0.00%||
|28|GA1|GARANTİ PORTFÖY BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|69.92|1.13%|0.78%|3.99%|1.10%|12.07%|3.64%|-0.75%|0.00%|DİBS %93.1|
|29|FI3|QNB PORTFÖY BORÇLANMA ARAÇLARI FONU|Borçlanma Araçları|TREND_CONTINUATION|69.77|1.04%|0.76%|4.13%|0.34%|9.94%|4.44%|-1.80%|0.00%|DİBS %89.3|
|30|KPC|KUVEYT TÜRK PORTFÖY KATILIM HİSSE SENEDİ (TL) FONU (HİSSE SENEDİ YOĞUN FON)|Hisse Senedi|EARLY_MOMENTUM + TREND_CONTINUATION|69.34|4.03%|2.37%|4.40%|2.51%|8.06%|16.16%|-5.14%|-0.34%|TR Hisse %87.7|

## CLAUDE RESEARCH INSTRUCTION

Use this shortlist as STAGE 1 only. For STAGE 2, investigate the highest-ranked candidates using current web research and primary sources where possible.
Verify retail investability, current fund strategy, KAP disclosures, meaningful portfolio exposures, catalysts, major risks, and whether the quantitative move is supported by current market conditions.
Do not recommend a fund solely because it appears in this report.