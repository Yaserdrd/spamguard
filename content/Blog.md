# Spam mesaj analizi nasıl çalışır? SpamGuard ile model kararını okumak

SEO başlığı: Spam Mesaj Analizi Nasıl Çalışır? | SpamGuard
Meta açıklama: İngilizce SMS mesajlarının nasıl sınıflandırıldığını, model skorunun ne anlattığını ve kelime katkılarının nasıl yorumlandığını öğrenin.
Anahtar ifade: spam mesaj analizi

Telefonunuza gelen bir mesajın neden spam olarak işaretlendiğini hiç merak ettiniz mi? Bir sonuç etiketi görmek kolaydır. O sonuca hangi ifadelerin katkı verdiğini anlamak ise farklı bir adımdır. SpamGuard, İngilizce SMS örneklerini incelemek için geliştirilmiş bir eğitim prototipidir. Kullanıcının mesajı, model tahminini ve açıklamayı aynı ekranda değerlendirmesini amaçlar.

## Mesajdan sayısal özelliklere

Makine öğrenmesi modeli bir mesajı insan gibi okuyup gönderenin niyetini bilemez. Bunun yerine eğitim verisindeki metinlerle etiketler arasındaki örüntüleri öğrenir. SpamGuard’ın temel Python sürümü mesaj uzunluğu, rakam sayısı ve büyük harf oranı gibi özellikleri kullanır. Web sürümünde ise metindeki kelimeler TF-IDF adlı yöntemle sayısal değerlere çevrilir. Logistic Regression modeli bu değerlerden spam veya normal sınıfını tahmin eder.

Bu ayrım önemlidir. Model mesajın göndericisini doğrulamaz. Bağlantıyı açıp incelemez. Bir sipariş bildiriminin gerçek bir mağazadan gelip gelmediğini de belirlemez. Yaptığı işlem, mesaj metnini öğrendiği sınıflandırma örüntüleriyle karşılaştırmaktır.

## Renkli kelimeler ne anlama gelir?

Analiz ekranındaki turuncu ve yeşil vurgular, model kararına katkı veren ifadeleri gösterir. Turuncu spam yönündeki, yeşil normal yönündeki katkıyı belirtir. Hesaplama, o mesajdaki TF-IDF değeri ile öğrenilmiş model katsayısını birleştirir.

Bir kelimenin turuncu görünmesi, kelimenin her kullanımının spam olduğu anlamına gelmez. Örneğin bir ödülden bahseden gerçek bir mesaj bulunabilir. Benzer şekilde günlük konuşma dili kullanan bir mesaj da istenmeyen içerik taşıyabilir. Açıklama modelin hesabını görünür kılar; mesajın gerçek kaynağını kanıtlamaz.

## Model skorunu nasıl okumalı?

SpamGuard bir spam model skoru gösterir. Bu değer kalibre edilmiş bir güvenlik olasılığı değildir. Düşük skor, mesajın güvenli olduğunu kanıtlamaz. Yüksek skor da tek başına dolandırıcılık iddiasına temel oluşturmaz.

Eğitim verisinde çoğu mesaj normal olduğu için başarıyı yalnızca doğrulukla değerlendirmek yanıltıcı olabilir. Bu projede precision, recall ve F1 de hesaplanır. Ayrıca normal bir mesajın yanlışlıkla spam işareti aldığı örnekler incelenir. Hatalar, modelin sınırlarını anlamak için sonuçlar kadar değerlidir.

## Kayıtlar nerede tutulur?

Mesaj sınıflandırması tarayıcıda gerçekleşir. Kullanıcı kaydetmeyi seçerse analiz kaydı aynı tarayıcının yerel depolamasına yazılır. Kayıtlar düzenlenebilir veya silinebilir. Ortak bir cihaz kullanıyorsanız kayıtlarınızın başka kullanıcılar tarafından görülebileceğini hesaba katın. Bu sürüm bir e-posta hesabına veya telefon mesaj kutusuna bağlanmaz.

## Hangi metinlerle deneyebilirsiniz?

İlk sürüm İngilizce SMS verisiyle geliştirilmiştir. Türkçe metinler, uzun e-postalar ve yeni mesaj türleri için başarı ölçülmemiştir. Deneme yapmak için uygulamadaki kurgusal örnek mesajları kullanabilirsiniz. Gerçek metin kullanacaksanız telefon numarası, şifre ve kişisel bilgiler yerine örnek bilgiler yazın.

Spam mesaj analizi, bir metnin neden işaretlendiğini araştırmak için yararlı bir öğrenme konusu sunar. SpamGuard’da bir İngilizce örnek mesajla başlayın, sonucu okuyun ve kelime katkılarını inceleyin. Son kararı, modelin sınırlarını ve mesajın bağlamını birlikte değerlendirerek verin.

Kaynak: Almeida, T. & Hidalgo, J. (2011). SMS Spam Collection. UCI. https://doi.org/10.24432/C5CC84. Ürün işleyişi SpamGuard kaynak koduna dayanır. Bu blog, proje kapsamında AI yardımıyla hazırlanmıştır.
