# Netlify yayını

Canlı yayın: https://resplendent-mochi-e81047.netlify.app/
GitHub: https://github.com/Yaserdrd/spamguard
19.10.2026: Public yayın doğrulandı. Ekle/listele/güncelle/sil ve sayfa yenilemede kalıcılık canlı tarayıcıda geçti.
Public web sözlüğünden sayı içeren tokenlar çıkarıldı. Web test doğruluğu %98,84, F1 %95,28.
ML raporundaki özgün karşılaştırma modeli: doğruluk %98,93, F1 %95,69; ayrı deneydir.

Yeniden üretim: proje kökünde `python train.py`, ardından `python sanitize_web_release.py`; sonra web klasöründe `npm test` ve `npm run build`. Public sürüm özgün LR katsayılarını korur, yalnızca harflerden oluşan sözlük sütunlarını seçip TF-IDF vektörünü yeniden normalize eder; metrikler bu dönüşüm sonrasında ölçülür.
