import os

# python dosyası nerede çalıştırılırsa çalıştırılsınrehber.txt nin main.pynin
# yanında olmasını sağlayan kodlar
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REHBER_FILE = os.path.join(SCRIPT_DIR, "rehber.txt")

# Turkce karakterleri doğru çevirmek için çeviri tablosu
TURKISH_LOWER_MAP = str.maketrans("IİÇĞÖŞÜ", "ıiçğöşü")
TURKISH_UPPER_MAP = str.maketrans("ıiçğöşü", "IİÇĞÖŞÜ")


def turkish_lower(text):
    "turkce stringleri kucuk e cevirme fonksiyonu"
    return text.translate(TURKISH_LOWER_MAP).lower()


def kisi_ekle():
    """Rehbere yeni kişi ekler"""
    isim = input("İsim: ").strip().replace("|", "")
    if not isim:
        print("❌ İsim boş olamaz!\n")
        return

    telefon = input("Telefon: ").strip().replace("|", "")
    if not telefon:
        print("❌ Telefon boş olamaz!\n")
        return

    email = input("Email: ").strip().replace("|", "")
    if not email:
        print("❌ Email boş olamaz!\n")
        return

    with open(REHBER_FILE, "a", encoding="utf-8") as dosya:
        dosya.write(f"{isim}|{telefon}|{email}\n")

    print("✓ Kişi eklendi!\n")


def kisileri_listele():
    """Rehberdeki tüm kişileri gösterir"""
    try:
        with open(REHBER_FILE, "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()

        # bos satirlari atla
        satirlar = [s for s in satirlar if s.strip()]

        if not satirlar:
            print("Rehber boş.\n")
            return

        print("\n" + "=" * 50)
        print("KİŞİ REHBERİ")
        print("=" * 50)

        for i, satir in enumerate(satirlar, 1):
            parcalar = satir.strip().split("|")
            if len(parcalar) != 3:
                print(f"{i}. [HATALI VERİ]: {satir.strip()}")
                print("-" * 50)
                continue
            isim, telefon, email = parcalar
            print(f"{i}. {isim}")
            print(f"   Tel: {telefon}")
            print(f"   Email: {email}")
            print("-" * 50)
        print()

    except FileNotFoundError:
        print("Henüz kayıtlı kişi yok.\n")


def kisi_ara():
    """İsme göre kişi arar"""
    aranan = turkish_lower(input("Aramak istediğin isim: ").strip())

    if not aranan:
        print("❌ Arama terimi boş olamaz!\n")
        return

    try:
        with open(REHBER_FILE, "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()

        # bos satirlari atla
        satirlar = [s for s in satirlar if s.strip()]

        bulundu = False
        print("\n" + "=" * 50)

        for satir in satirlar:
            parcalar = satir.strip().split("|")
            if len(parcalar) != 3:
                continue  # her satirda 3 tane olmasi lazim, demekki veri bozuk, atla
            isim, telefon, email = parcalar
            if aranan in turkish_lower(isim):
                print(f"İsim: {isim}")
                print(f"Tel: {telefon}")
                print(f"Email: {email}")
                print("-" * 50)
                bulundu = True

        if not bulundu:
            print("Kişi bulunamadı!")
        print()

    except FileNotFoundError:
        print("Henüz kayıtlı kişi yok.\n")


def kisi_sil():
    """Rehberden kişi siler"""
    try:
        with open(REHBER_FILE, "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()

        # bos satirlari atla
        satirlar = [s for s in satirlar if s.strip()]

        if not satirlar:
            print("Rehber zaten boş.\n")
            return

        print("\n" + "=" * 50)
        for i, satir in enumerate(satirlar, 1):
            parcalar = satir.strip().split("|")
            isim = parcalar[0] if parcalar else "[HATALI VERİ]"
            print(f"{i}. {isim}")
        print("=" * 50)

        secim_str = input("Silmek istediğin kişinin numarası: ").strip()
        if not secim_str:
            print("❌ Numara boş olamaz!\n")
            return

        secim = int(secim_str)

        if 1 <= secim <= len(satirlar):
            silinen = satirlar.pop(secim - 1)
            parcalar = silinen.strip().split("|")
            isim = parcalar[0] if parcalar else "[BİLİNMEYEN]"

            with open(REHBER_FILE, "w", encoding="utf-8") as dosya:
                dosya.writelines(satirlar)

            print(f"✓ {isim} silindi!\n")
        else:
            print("Geçersiz numara!\n")

    except FileNotFoundError:
        print("Henüz kayıtlı kişi yok.\n")
    except ValueError:
        print("Lütfen geçerli bir numara gir!\n")


def menu():
    """Ana menü"""
    while True:
        print("=" * 50)
        print("KİŞİ REHBERİ UYGULAMASI")
        print("=" * 50)
        print("1. Kişi Ekle")
        print("2. Kişileri Listele")
        print("3. Kişi Ara")
        print("4. Kişi Sil")
        print("5. Çıkış")
        print("=" * 50)

        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            kisi_ekle()
        elif secim == "2":
            kisileri_listele()
        elif secim == "3":
            kisi_ara()
        elif secim == "4":
            kisi_sil()
        elif secim == "5":
            print("Görüşürüz!")
            break
        else:
            print("Geçersiz seçim!\n")


# Programı başlat
if __name__ == "__main__":
    menu()
