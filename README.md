# TEFAS → Claude (Cloud / No Installation)

Bu sürüm iş bilgisayarına Python veya başka bir program kurmadan çalışır.

## Nasıl çalışır?
1. GitHub Actions bulutta `update_tefas.py` dosyasını çalıştırır.
2. TEFAS verisini çeker.
3. `TEFAS_DAILY_DATA.csv` dosyasını günceller.
4. Güncel dosyayı aynı GitHub reposuna commit eder.
5. Claude'un GitHub connector'ı üzerinden bu dosyayı Investment Analyst projesine bağlayabilirsin.

## İlk kurulum — sadece tarayıcı
1. GitHub'da yeni bir PRIVATE repository oluştur. Önerilen isim: `tefas-investment-data`.
2. Bu ZIP içeriğini repository'nin kök dizinine yükle.
   - `.github/workflows/update-tefas.yml` yolunun aynen korunması gerekir.
3. Repository > Actions > "Update TEFAS data" > Run workflow ile ilk çalışmayı başlat.
4. İlk çalışma birkaç dakika sürebilir.
5. Başarılı olduğunda repository kökünde:
   - `TEFAS_DAILY_DATA.csv`
   - `TEFAS_UPDATE_STATUS.json`
   - `data/tefas_history.csv.gz`
   oluşur.

## Günlük otomasyon
Workflow hafta içi Türkiye saatiyle yaklaşık 09:17'de çalışacak şekilde ayarlanmıştır.
GitHub scheduled workflows yoğunluk durumunda gecikebilir.

## Claude bağlantısı
Claude > Customize > Connectors bölümünden GitHub'ı bağla.

Investment Analyst project:
1. Project Knowledge / Files alanındaki `+` butonuna bas.
2. GitHub seç.
3. `tefas-investment-data` reposunu seç.
4. En az şu dosyaları ekle:
   - `TEFAS_DAILY_DATA.csv`
   - `TEFAS_UPDATE_STATUS.json`
   - `CLAUDE_DATA_RULE.txt`
5. Günlük analizden önce gerekirse GitHub içeriklerinde Sync kullan.

## Claude'a günlük komut
"Günlük analizimi yap. Önce GitHub'daki TEFAS_DAILY_DATA.csv dosyasının
generated_at_local ve dataset_latest_date alanlarını kontrol et. Dosya güncel değilse
bunu açıkça söyle. Güncelse tüm veri setini nicel olarak tara, ardından kısa listeyi
KAP/TEFAS/fon yönetim şirketi ve güncel web kaynaklarıyla doğrula."

## Güvenlik
Repository'yi PRIVATE tutabilirsin. Bu veri setinde kişisel portföy bilgilerini
saklamana gerek yok. Sadece halka açık TEFAS verileri bulunur.
