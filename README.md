# SpamGuard

Yaser Durdu | Software Persona Yapay Zeka Mesleki Gelişim Programı | 19.10.2026

İngilizce SMS mesajlarını spam/normal olarak sınıflandıran, model kararına katkı veren kelimeleri gösteren eğitim projesi. Dört ders için ayrı çıktılar hazırlanmıştır.

- Canlı uygulama: https://resplendent-mochi-e81047.netlify.app/
- Kaynak kod: https://github.com/Yaserdrd/spamguard
- Python notebook: [Google Colab](https://colab.research.google.com/github/Yaserdrd/spamguard/blob/main/python/SpamGuard_Python.ipynb)
- ML notebook: [Google Colab](https://colab.research.google.com/github/Yaserdrd/spamguard/blob/main/ml/SpamGuard_ML.ipynb)

## Derslere göre dosyalar
| Ders | Konum | Teslim |
|---|---|---|
| Basitleştirilmiş Python | python/ ve reports/ | Notebook, bir sayfa Word raporu, beş slayt sunum |
| Web Geliştirme ve Yapay Zeka | web/ | Public GitHub, canlı site ve ekran görüntüsü |
| Yapay Zeka ile İçerik Üretimi | content/ ve reports/ | İki sayfa strateji, 7 günlük Excel takvimi, içerik kanıtları ve medya |
| Makine ve Derin Öğrenme | ml/ ve reports/SpamGuard_ML_Rapor.pdf | Notebook bağlantısı içeren beş sayfa PDF |

## Webi çalıştırma
Önce model dosyasını yerelde üretin; sözlükte veri kaynaklı tokenlar bulunduğu için model.json public depoya dahil edilmez.
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
React/Vite ve CSS kullanılır. Mesaj metni analiz için sunucuya gönderilmez. Analiz ekle/listele/güncelle/sil işlemleri LocalStorage ile yapılır. Netlify için web/ kök klasörü, `npm run build` komutu ve `dist` yayın klasörü seçilebilir.

## Modelleri yeniden üretme
Python 3.12 ve scikit-learn 1.8.0 ile doğrulandı.
```bash
pip install -r requirements.txt
python train.py
python python/mini_app.py
```
Notebook'lar yerel ham veriyi kullanır; Colab'da bulunamazsa UCI verisini indirir. Mini araçtan `/q` ile çıkılır. Joblib dosyaları eğitimle yeniden oluşturulur.

## Veri ve yöntem
Almeida, T. ve Hidalgo, J. (2011). SMS Spam Collection. UCI Machine Learning Repository. https://doi.org/10.24432/C5CC84. CC BY 4.0. Ham veri teslim paketinde korunmuş, sayısal özellikler türetilmiştir. Public GitHub deposuna ham mesajlar veya metin içeren CSV dosyaları yüklenmez. Notebook çıktıları temizlenmiştir; veri resmî UCI kaynağından indirilerek sonuçlar yeniden üretilebilir.

5.574 ham satırdan normalize edilmiş 415 tam tekrar çıkarıldı. 5.159 temiz mesaj: 4.517 normal, 642 spam. Ayrım: 3.095 eğitim / 1.032 doğrulama / 1.032 test. Sözlük yalnızca eğitimde öğrenilir; hiperparametreler doğrulama F1 ile seçilir.

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Çoğunluk temel modeli | %87,60 | %0 | %0 | %0 |
| Decision Tree | %96,51 | %81,08 | %93,75 | %86,96 |
| TF-IDF + Logistic Regression | %98,93 | %96,06 | %95,31 | %95,69 |
| TF-IDF + Naive Bayes | %98,06 | %96,55 | %87,50 | %91,80 |

Pozitif sınıf spamdır. LR testinde 5 yanlış pozitif ve 6 yanlış negatif vardır.

Ham veri ve öğrenilmiş model sözlüğü public depoda bulunmaz. Web teslim paketinde çalışır model dosyası vardır.

## Kontroller
19.10.2026: iki notebook'un bütün kod hücreleri (input örnek mesajla), train.py, web testleri ve üretim derlemesi başarıyla çalıştırıldı. Güncel filtreli web sürümünde 28 örnekte Python/JavaScript model skorları arasındaki en büyük fark 2,08e-17. Netlify üzerinde ekle/listele/güncelle/sil ve yenileme sonrası kalıcılık gerçek tarayıcıda doğrulandı. Mobil cihaz üzerinde ayrı test yapılmadı.

## Public web sürümü
Netlify yayını veri kaynaklı sayısal tokenları içermeyen 4.651 terimlik filtreli sözlük kullanır. Orijinal ML raporu değiştirilmedi. Web test doğruluğu %98,84, precision %96,03, recall %94,53, F1 %95,28; 5 yanlış pozitif ve 7 yanlış negatif. Üretim ve yeniden hesaplama için `python train.py` ardından `python sanitize_web_release.py` çalıştırın.

## Sınırlılıklar
Model İngilizce SMS içindir. Türkçe, e-posta, phishing veya AI yazarlığı tespiti için doğrulanmadı. Benzer mesaj şablonları sonuçları iyimserleştirebilir. Skorlar kalibre edilmedi; normal tahmini güvenlik garantisi değildir. Ortak cihazda analiz kayıtlarını temizleyin.

İçerik çalışması kurgusal markaya aittir. AI kullanım kaydı content/KONTROL_VE_AI_KAYDI.md içindedir. Büyük görsel, video ve ses dosyaları ayrı içerik teslim paketinde bulunur; GitHub'da metinler ve küçük kanıt görselleri yer alır. Hiçbir teslim formu gönderilmedi.

## Ekran görüntüsü ve raporlar
Ekran görüntüsü, Word/PDF raporlar, sunum ve medya dosyaları ayrı teslim paketlerindedir. Public depoda kaynak kod ve veri çıktıları temizlenmiş notebook'lar tutulur.
