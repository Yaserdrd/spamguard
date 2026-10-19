# SpamGuard içerik akışı: isteğe bağlı otomasyon tasarımı

Durum: Tasarım. Make/Zapier üzerinde kurulmadı, dış hesap bağlanmadı, e-posta veya sosyal medya paylaşımı yapılmadı. Bu dosya çalışan otomasyon kanıtı değildir.

9 Ekim dersinde otomasyon ayrıntılı gösteriliyor. Bununla birlikte eğitmen 2:35:20–2:35:28 ve 2:41:00–2:41:10 aralıklarında teslim için ContentFlow dokümanına yönlendiriyor. Yüklenen doküman gelişmiş otomasyonu isteğe bağlı sayıyor. Bu tasarımı temel içerik dosyalarının üzerine ek bir öneri olarak hazırladık.

## Senaryo
Tetikleyici: Editör, içerik takvimindeki bir satırı üretime hazır olarak işaretler. Otomatik yayın değil, taslak üretimi başlar.

1. Takvim satırını oku: konu, kanal, format ve hedef kitle alanları boşsa durdur.
2. Marka sesi rehberini metin üretim isteğine ekle. RTF veya CO-STAR biçimi kullan.
3. Metin taslağı ve görsel promptu üret. Her çıktıda kullanılan araç/sürüm ve zaman kaydı tut.
4. Görseli marka paletiyle üret. İsteniyorsa video senaryosu ve TTS metni hazırla.
5. Kontrol: ölçülmemiş başarı yüzdesi, her dilde destek, kesin koruma veya gerçek kişiye ait veri varsa taslağı işaretle. Bu kontrol, doğruluk garantisi değildir.
6. İnsan editör içerikleri ve telif/kaynakları inceler. Onay olmadan yayın aşamasına geçme.
7. Onaylı dosyaları teslim klasörüne kaydet. Yayın entegrasyonu ayrıca açıkça yetkilendirilirse kurulur.

## Hata durumları
- API kotası: sınırlı yeniden deneme; ardından işi Hata durumuna al ve taslağı koru.
- Eksik dosya veya bozuk medya: onayı engelle, hatalı adımı kaydet.
- Marka sesi tutarsızlığı: promptu revize et, yeni sürümü eski sürümün üzerine yazma.
- Kaynak doğrulanamıyor: iddiayı kaldır veya doğrulanmış kaynakla değiştir.

## Kayıt alanları
content_id, plan_day, channel, format, prompt_version, tool, generated_at, review_status, reviewer_note, output_path, error_message.

Bu tasarım çalıştırılırsa başarıyı göstermek için gerçek çalışma geçmişi ve örnek çıktı kanıtı gerekir. Bu pakette uydurma run ID, onay kaydı veya e-posta ekranı yoktur.
