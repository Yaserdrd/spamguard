# Veri sözlüğü

Kaynak: Almeida, T. & Hidalgo, J. (2011). SMS Spam Collection. UCI Machine Learning Repository. https://doi.org/10.24432/C5CC84. Lisans: CC BY 4.0. Kaynak veriye sütun/özellik eklenmiştir; ham dosya korunur.

| Sütun | Tip | Açıklama |
|---|---|---|
| id | tamsayı | Temizlik sonrası yerel örnek numarası |
| text | metin | İngilizce SMS içeriği |
| label | kategori | ham: normal, spam: istenmeyen mesaj |
| target | tamsayı | ham=0, spam=1 |
| character_count | tamsayı | Boşluk ve noktalama dahil karakter sayısı |
| word_count | tamsayı | Boşluktan ayrılan parçaların sayısı |
| digit_count | tamsayı | Rakam karakterlerinin sayısı |
| exclamation_count | tamsayı | Ünlem karakterlerinin sayısı |
| uppercase_ratio | ondalık | Büyük harf sayısı / harf sayısı; harf yoksa 0 |
| url_count | tamsayı | http://, https:// veya www. örüntülerinin sayısı |
| split | kategori | train, validation veya test |

5.574 ham satırdan küçük harfe çevirip boşlukları birleştirerek belirlenen 415 tekrar çıkarıldı. Çelişen etiketli anahtar ve boş/geçersiz satır bulunmadı. 5.159 mesaj kaldı. 4.517 ham, 642 spam. Sınıf oranları korunarak %60/%20/%20 ayrım yapıldı; random_state=42. Benzer ama aynı olmayan mesaj şablonları kalabilir. Veri güncel SMS trafiğini veya Türkçe mesajları temsil etmez.

Temizlikte etiketi bilinmeyen kullanıcı mesajı kullanılmadı. Eksik değer olmadığı için doldurma yapılmadı. Mesaj uzunluğu uç değerleri otomatik atılmadı. Aynı kaynak corpus içindeki rastgele ayrım, dış veri genellemesini ölçmez.
