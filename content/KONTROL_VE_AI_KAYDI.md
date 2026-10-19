# İçerik kontrolü ve AI kullanım kaydı

## Araçlar ve üretim
- ChatGPT/Codex: marka stratejisi, persona, blog, sosyal medya metinleri, video senaryosu ve kod taslağı. Metinler kullanıcı talebi ve dört yönergeye göre hazırlandı.
- ImageGen yerleşik araç: aynı yeşil/kırık beyaz/turuncu paletle üç özgün kampanya görseli üretildi. Tam promptlar Gorsel_Promptlari.md içinde.
- FFmpeg/libflite (slt sesi): voiceover.txt içeriğinden gerçek sentetik konuşma üretildi. İngilizce seslendirme kullanıldı. Dosya 18 saniye, konuşma yaklaşık 13,3 saniyede tamamlanır.
- FFmpeg: üç AI görseli altışar saniyelik sahneler halinde sesle birleştirildi. Video 1080×1080, H.264/AAC ve 18 saniye. Bu bir görsel tabanlı tanıtım videosudur; metinden hareketli sahne üreten bir video modeli kullanılmadı.
- Python/scikit-learn: model eğitimi ve ölçümler. Grafik ve sayılar gerçek test çıktılarından alındı.
- Artifact Tool: sunum ve Excel takvimi. ReportLab: raporlar.

## Blog için CO-STAR prompt kaydı
Context: SpamGuard, İngilizce SMS verisiyle eğitilen ve karar katkılarını gösteren bir eğitim prototipi.
Objective: spam mesaj analizi konusunu, model skorunu ve kelime katkılarını anlatan bir SEO blogu yaz.
Style: kısa paragraflar, anlaşılır teknik açıklama, özgün anlatım.
Tone: sakin ve ölçülü. Kesin koruma veya her dilde başarı iddiası yok.
Audience: İngilizce SMS örnekleriyle çalışan üniversite öğrencileri ve dijital okuryazarlığa ilgi duyan kullanıcılar.
Response: başlık, meta açıklama, anahtar ifade, alt başlıklı blog ve veri kaynağı. Çıktı: Blog.md.

## Video ve ses promptu / kurgu
Görev: SpamGuard için 15–20 saniyelik, sakin sesle okunabilen İngilizce tanıtım metni yaz. Metin girişi, model skoru, kelime katkıları ve yerel kaydı anlat. Güvenlik garantisi verme.
Çıktı: voiceover.txt. Sesin gerçek süresi dosyadan ölçüldü. Görsel sırası: Mesajı incele (0–6s), Kararı anla (6–12s), Analizini kaydet (12–18s).

## Kontrol sonuçları
- Marka renkleri üç görselde tutarlı. Görsel başlıkları ve marka yazımı görsel olarak incelendi.
- Metinlerde kesin tespit, her dilde başarı veya doğrulanmamış tasarruf iddiası yok.
- Ürün kurgusal, persona kurgusal olarak işaretlendi. Gerçek kullanıcı araştırması yapılmış gibi yazılmadı.
- Rakip özellikleri Google, Microsoft ve Apache'nin resmi sayfalarıyla sınırlandırıldı. Kıyaslamalı performans üstünlüğü iddia edilmedi.
- Veri kaynağı ve CC BY 4.0 atfı rapor/veri sözlüğünde mevcut.
- Üçüncü taraf logo veya adı verilen sanatçı tarzı istenmedi. Görseller AI üretimidir; özgünlük veya marka tescili garantisi verilmez.
- Ses gerçek bir kişinin taklidi değildir. libflite slt sentetik sesi kullanılmıştır.
- Video ve ses dosyalarının süresi 18 saniye olarak ffprobe ile kontrol edildi. Konuşmanın sonu kesilmedi.
- İçerikler yayına otomatik gönderilmedi. İçerik takvimindeki bütün durumlar Planlandı.
- Kullanıcının son içerik/sunum incelemesi bekliyor. Canva paylaşım linki henüz yok.

## Sınırlar
Kapsamlı otomasyon, otomatik sosyal medya paylaşımı ve etkileşim raporu üretilmedi; yönergede isteğe bağlıdır. AI kullanımının gizlendiği bir süreç anlatılmadı. Blog ve gönderi metinleri AI yardımıyla üretilmiştir.

## 9 Ekim ders kaydı sonrası
Marka sesi, prompt belgeleri ve son kontrolün insanda kalması vurgusu incelendi. Otomasyon_Tasarimi.md eklenmiştir; bu dosya tasarım olup çalışan Make/Zapier otomasyonu veya dış gönderim kanıtı değildir. Yazılı yönergedeki isteğe bağlılık korunur.

## Yazılı yönerge sonrası format bazlı kontrol
| Format | Kontrol edilen | Sonuç / açık iş |
|---|---|---|
| Blog | Marka tonu, ürün işleyişi, model sınırı, kaynak | Kaynak koduyla uyumlu; Türkçe/AI yazarlığı başarısı vaat edilmez |
| 3 gönderi | RTF, tek CTA, ton, görsel eşlemesi | Üç prompt ve çıktı mevcut; yayın yapılmadı |
| 3 görsel | Başlık, marka, palet, üçüncü taraf logo | Görsel inceleme yapıldı; ana renk aileleri tutarlı |
| Video | Süre, görsel sırası, yanıltıcı iddia | ffprobe: 18 saniye, 1080×1080 H.264/AAC; gerçek kare önizlemesi eklendi |
| Ses | TTS kaynağı, süre, metin tutarlılığı | 18 saniye WAV; ~13,3 saniye konuşma; dosyadan dalga biçimi çıkarıldı. İnsan son dinlemesi bekliyor |
| Teslim | Strateji, takvim, içerik kanıtları | Tek sayfa rehber ve 5 sayfa önizleme PDF eklendi. Gerekirse oynatıcı ekran görüntüsü son aşamada eklenmeli |

Araçla yapılan kontrol, kullanıcının son dinleme/izleme ve onayını yapılmış gibi göstermez. Kontrol tablosu kısa temel belgedir; otomatik fact-check sistemi kurulmadı.
