# SpamGuard web uygulaması

React + Vite + CSS. İngilizce SMS sınıflandırma ve yerel analiz kaydı yönetimi.

## Kurulum
Node.js 20.19+ veya 22.12+ ile:

```bash
npm install
npm run test
npm run dev
npm run build
```

Yayın klasörü: dist. Netlify build komutu: npm run build. Publish directory: dist. Netlify şart değildir; bu klasörü sunabilen muadil bir statik yayın hizmeti kullanılabilir. Canlı yayın herkese açıktır: https://spamguard-yaser.vocalcoati8.chatgpt.site

## Yönergedeki dört işlem
- Ekle: mesajı analiz et, başlık ver ve Analizi kaydet düğmesini kullan.
- Listele: Analiz geçmişi ekranını aç.
- Güncelle: geçmişten Düzenle, metni değiştir, yeniden analiz et ve Kaydı güncelle.
- Sil: geçmişte Sil ve silme onayını kullan.

LocalStorage kayıtları sayfa yenilendiğinde korur. Tarayıcı verileri silinirse kayıtlar kaybolabilir. Gerçek kullanıcı verisi veya bulut eşitlemesi gerekmiyor.

## Model ve açıklama
public/model.json gerçek eğitimden dışa aktarılmış TF-IDF ve Logistic Regression parametrelerini içerir. src/inference.js aynı tokenlaştırma, alt doğrusal TF ve L2 normalizasyonu uygular. tests/model-parity.mjs Python çıktılarıyla 28 örneği karşılaştırır. Model yalnızca İngilizce SMS verisinde değerlendirilmiştir. Skor kalibre edilmiş olasılık olarak sunulmaz.

## Ekran görüntüsü ve teslim
Ekran görüntüsü: ../reports/SpamGuard_Web_Ekran.png. GitHub'a proje kökünü yüklerseniz bu dosyayı aynı konumda koruyun. Yalnızca web klasörünü yükleyecekseniz görüntüyü ayrıca ekleyin.

2 Ekim kaydında 1:54:56–1:57:32 aralığında açıklanan çerçeve, CRUD, public GitHub, yayın ve ekran görüntüsü şartları için hazırlanmıştır. Public GitHub: https://github.com/Yaserdrd/spamguard

## Ekran görüntüsü
Ekran görüntüsü web teslim ZIP dosyasındaki public/SpamGuard_Web_Ekran.png içindedir.

Görsel önceki yayın sürümünden; güncel sürümde düzenleme başlığı ve boş filtre açıklaması iyileştirildi.

## Kaynak düzeni
src/main.jsx React başlangıcı; src/pages/Workspace.jsx ekranlar; src/components/Icon.jsx ortak simge; src/utils/records.js kayıt güncelleme; src/inference.js gerçek model hesabı.

Tekrar kaydetmek aynı kaydı günceller. Yeni analiz için Temizle veya örnek mesaj düğmesini kullanın. Netlify yapılandırması netlify.toml içinde hazırdır. Public GitHub ve herkese açık canlı yayın bağlantıları yukarıdadır.
