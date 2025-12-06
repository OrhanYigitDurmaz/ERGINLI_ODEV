# Edge Cases - Kişi Rehberi Uygulaması

Bu dokümanda `main.py` dosyasındaki edge case'ler (sınır durumları) detaylı olarak açıklanmıştır.

---

## 1. Boş Girdi Kontrolleri

### 1.1 İsim Boş Girilirse
```
İsim: [Enter tuşuna basılır]
❌ İsim boş olamaz!
```
**Davranış:** Fonksiyon erken döner, kayıt yapılmaz.

### 1.2 Telefon Boş Girilirse
```
İsim: Ahmet
Telefon: [Enter tuşuna basılır]
❌ Telefon boş olamaz!
```
**Davranış:** Fonksiyon erken döner, kayıt yapılmaz.

### 1.3 Email Boş Girilirse
```
İsim: Ahmet
Telefon: 05551234567
Email: [Enter tuşuna basılır]
❌ Email boş olamaz!
```
**Davranış:** Fonksiyon erken döner, kayıt yapılmaz.

### 1.4 Arama Terimi Boş Girilirse
```
Aramak istediğin isim: [Enter tuşuna basılır]
❌ Arama terimi boş olamaz!
```
**Davranış:** Arama yapılmaz, fonksiyon erken döner.

### 1.5 Silme Numarası Boş Girilirse
```
Silmek istediğin kişinin numarası: [Enter tuşuna basılır]
❌ Numara boş olamaz!
```
**Davranış:** Silme işlemi yapılmaz.

---

## 2. Dosya Durumları

### 2.1 `rehber.txt` Dosyası Mevcut Değil
**Senaryo:** Program ilk kez çalıştırılıyor veya dosya silinmiş.

| İşlem | Sonuç |
|-------|-------|
| Kişi Ekle | Dosya otomatik oluşturulur, kişi eklenir |
| Kişileri Listele | "Henüz kayıtlı kişi yok." mesajı |
| Kişi Ara | "Henüz kayıtlı kişi yok." mesajı |
| Kişi Sil | "Henüz kayıtlı kişi yok." mesajı |

### 2.2 Dosya Boş
**Senaryo:** Dosya var ama içinde hiç kayıt yok.

| İşlem | Sonuç |
|-------|-------|
| Kişileri Listele | "Rehber boş." mesajı |
| Kişi Sil | "Rehber zaten boş." mesajı |

### 2.3 Dosyada Sadece Boş Satırlar Var
**Senaryo:** Dosyada yalnızca `\n` karakterleri var.

**Davranış:** Boş satırlar filtrelenir, "Rehber boş." mesajı gösterilir.

---

## 3. Özel Karakter Durumları

### 3.1 Pipe (`|`) Karakteri Girilirse
**Senaryo:** Kullanıcı isim, telefon veya email'e `|` karakteri girer.

```
İsim: Ali|Veli
```

**Davranış:** `|` karakteri otomatik olarak kaldırılır → `AliVeli` olarak kaydedilir.

**Sebep:** `|` karakteri veri ayırıcı olarak kullanıldığından, veri bütünlüğünü korumak için kaldırılır.

### 3.2 Türkçe Karakterler
**Senaryo:** İsimde Türkçe karakterler kullanılır (İ, ı, Ş, ş, Ğ, ğ, Ü, ü, Ö, ö, Ç, ç).

```
İsim: Şükrü Öztürk
```

**Davranış:** UTF-8 kodlaması sayesinde doğru şekilde kaydedilir ve gösterilir.

### 3.3 Türkçe Karakter ile Arama
**Senaryo:** Büyük/küçük harf farkı olmadan arama yapmak.

```
Kayıtlı isim: İbrahim
Aranan: ibrahim veya İBRAHİM veya iBrAhİm
```

**Davranış:** `turkish_lower()` fonksiyonu sayesinde tüm varyasyonlar eşleşir.

---

## 4. Hatalı Veri Durumları

### 4.1 Dosyada Bozuk Veri Formatı
**Senaryo:** `rehber.txt` dosyasında eksik veya fazla `|` karakteri olan satır var.

```
Ahmet|05551234567
Ali|123|ali@mail.com|fazla
```

**Davranış:**
- **Listeleme:** `[HATALI VERİ]` olarak işaretlenir
- **Arama:** Bu satırlar atlanır (skip)
- **Silme:** İsim kısmı gösterilir (ilk parça)

### 4.2 Manuel Düzenleme Sonrası Bozulma
**Senaryo:** Kullanıcı `rehber.txt` dosyasını manuel olarak düzenler ve format bozulur.

**Davranış:** Program çökmez, hatalı veriler işaretlenir veya atlanır.

---

## 5. Silme İşlemi Edge Case'leri

### 5.1 Geçersiz Numara Girilirse
```
1. Ahmet
2. Mehmet
Silmek istediğin kişinin numarası: 5
Geçersiz numara!
```

### 5.2 Negatif Numara Girilirse
```
Silmek istediğin kişinin numarası: -1
Geçersiz numara!
```

### 5.3 Sayı Olmayan Değer Girilirse
```
Silmek istediğin kişinin numarası: abc
Lütfen geçerli bir numara gir!
```

### 5.4 Ondalıklı Sayı Girilirse
```
Silmek istediğin kişinin numarası: 1.5
Lütfen geçerli bir numara gir!
```

---

## 6. Menü Edge Case'leri

### 6.1 Geçersiz Menü Seçimi
```
Seçiminiz: 9
Geçersiz seçim!
```

### 6.2 Harf ile Seçim
```
Seçiminiz: a
Geçersiz seçim!
```

### 6.3 Boş Seçim
```
Seçiminiz: [Enter]
Geçersiz seçim!
```

---

## 7. Arama Edge Case'leri

### 7.1 Kısmi Eşleşme
**Senaryo:** İsmin bir kısmı ile arama yapmak.

```
Kayıtlı isimler: Ahmet Yılmaz, Mehmet Yılmaz
Aranan: Yılmaz
```

**Davranış:** Her iki kişi de listelenir (kısmi eşleşme desteklenir).

### 7.2 Eşleşme Bulunamadığında
```
Aranan: XYZ
Kişi bulunamadı!
```

### 7.3 Tek Karakterlik Arama
```
Aranan: a
```

**Davranış:** İsminde "a" harfi geçen tüm kişiler listelenir.

---

## 8. Whitespace (Boşluk) Durumları

### 8.1 Başta/Sonda Boşluk
```
İsim:    Ahmet    
```

**Davranış:** `strip()` ile boşluklar temizlenir → `Ahmet` olarak kaydedilir.

### 8.2 Sadece Boşluk Karakteri
```
İsim:      [sadece boşluklar]
❌ İsim boş olamaz!
```

**Davranış:** `strip()` sonrası boş string olur, reddedilir.

---

## 9. Sınır Değerler

### 9.1 Çok Uzun Girdi
**Senaryo:** Kullanıcı çok uzun bir isim/telefon/email girer.

**Davranış:** Python string limitleri dahilinde kabul edilir (pratik bir limit yok).

### 9.2 Tek Kayıt Silme
**Senaryo:** Rehberde tek kişi var ve silinirse.

**Davranış:** Dosya boşaltılır, sonraki listelemede "Rehber boş." mesajı gösterilir.

### 9.3 Büyük Veri Seti
**Senaryo:** Binlerce kayıt var.

**Davranış:** Tüm veriler belleğe yüklenir (`readlines()`). Çok büyük dosyalarda performans sorunu olabilir.

---

## 10. Eşzamanlılık (Concurrency)

### 10.1 Aynı Anda İki Program Çalıştırılırsa
**Senaryo:** İki terminal'de aynı anda program çalıştırılır ve ikisi de aynı dosyaya yazar.

**Davranış:** Race condition oluşabilir, veri kaybı veya bozulma riski vardır.

> ⚠️ **Not:** Bu program dosya kilitleme (file locking) mekanizması içermez. Tek kullanıcılı senaryo için tasarlanmıştır.

---

## Özet Tablo

| Edge Case | Kontrol Var mı? | Davranış |
|-----------|-----------------|----------|
| Boş girdi | ✅ Evet | Hata mesajı, işlem iptal |
| Dosya yok | ✅ Evet | FileNotFoundError yakalanır |
| Pipe karakteri | ✅ Evet | Otomatik kaldırılır |
| Türkçe karakterler | ✅ Evet | UTF-8 ile desteklenir |
| Bozuk veri formatı | ✅ Evet | İşaretlenir/atlanır |
| Geçersiz numara | ✅ Evet | Hata mesajı |
| Sayı olmayan girdi | ✅ Evet | ValueError yakalanır |
| Whitespace | ✅ Evet | strip() ile temizlenir |
| Dosya kilitleme | ❌ Hayır | Race condition riski |
| Girdi validasyonu (email/tel) | ❌ Hayır | Format kontrolü yok |