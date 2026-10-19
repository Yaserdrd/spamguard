# SpamGuard web uygulaması

React + Vite + CSS. İngilizce SMS sınıflandırma ve yerel analiz kaydı yönetimi.

## Kurulum ve aynı public sürümü üretme
Proje kökünden:
```bash
pip install -r requirements.txt
python train.py
python sanitize_web_release.py
cd web
npm ci
npm test
npm run dev
npm run build
```
Node.js 20.19+ veya 22.12+ kullanın. Model dosyası eğitimle üretilir; ham SMS ve öğrenilmiş sözlük public depoya dahil edilmez. Netlify build öncesi model dosyası yerelde üretilmelidir; otomatik Git bağlantısıyla eksik model üretmeye çalışmayın. Hazır dist/ statik olarak yüklenebilir.

Canlı Netlify: https://resplendent-mochi-e81047.netlify.app/
Netlify yayın klasörü dist. Sayısal tokenları filtreleyen public sürüm 4.651 terim kullanır. Accuracy %98,84, precision %96,03, recall %94,53, F1 %95,28; FP=5, FN=7. ML raporundaki filtrelenmemiş deney ayrı tutulur. Ayrıntı: NETLIFY_YAYIN.md.

## Yönergedeki dört işlem
- Ekle: mesajı analiz et, başlık ver ve Analizi kaydet düğmesini kullan.
- Listele: Analiz geçmişi ekranını aç.
- Güncelle: geçmişten Düzenle, metni değiştir, yeniden analiz et ve Kaydı güncelle.
- Sil: geçmişte Sil ve silme onayını kullan.

LocalStorage kayıtları sayfa yenilendiğinde korur. Tarayıcı verileri silinirse kayıtlar kaybolabilir. Gerçek kullanıcı verisi veya bulut eşitlemesi gerekmiyor.

## Model ve açıklama
public/model.json gerçek eğitimden dışa aktarılmış TF-IDF ve Logistic Regression parametrelerini içerir. src/inference.js aynı tokenlaştırma, alt doğrusal TF ve L2 normalizasyonu uygular. tests/model-parity.mjs Python çıktılarıyla 28 örneği karşılaştırır. Model yalnızca İngilizce SMS verisinde değerlendirilmiştir. Skor kalibre edilmiş olasılık olarak sunulmaz.

## Ekran görüntüsü ve teslim
Güncel Netlify ekran görüntüsü formun ayrı dosya alanına `Yaser_Durdu_Web_Netlify_Ekran.png` adıyla yüklenir. Kaynak kod bağlantısı: https://github.com/Yaserdrd/spamguard. Ekran görüntüsü ve sunum gibi ikili dosyalar ayrı teslimde bulunur.

Netlify üzerinde ekleme, listeleme, güncelleme, silme ve sayfa yenilenince kalıcılık doğrulandı; deneme kaydı kaldırıldı. Mobil cihaz testi yapılmadı.

## Kaynak düzeni
src/main.jsx React başlangıcı; src/pages/Workspace.jsx ekranlar; src/components/Icon.jsx ortak simge; src/utils/records.js kayıt güncelleme; src/inference.js gerçek model hesabı.

Tekrar kaydetmek aynı kaydı günceller. Yeni analiz için Temizle veya örnek mesaj düğmesini kullanın. Netlify yapılandırması netlify.toml içinde hazırdır. Public GitHub ve herkese açık canlı yayın bağlantıları yukarıdadır.
