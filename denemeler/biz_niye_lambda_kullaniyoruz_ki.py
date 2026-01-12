# https://www.artima.com/weblogs/viewpost.jsp?thread=98196

# 1. Önce senin için basit bir 'User' sınıfı yapalım.
# Bu sınıfın objelerinin içinde 'id' ve 'name' olacak.
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # Ekrana basınca güzel görünsün diye (bu kısım şov)
    def __repr__(self):
        return f"User(id={self.id})"


# 2. Elimizde bu objelerden oluşan bir liste var.
# İşte 'users' listesi bu:
users = [
    User(id=101, name="Ahmet"),
    User(id=102, name="Mehmet"),
    User(id=103, name="Ayşe"),
]

print("Liste şu:", users)
# Çıktı: [User(id=101), User(id=102), User(id=103)]

# --- CAN ALICI KISIM ---

# 3. map ve lambda iş başında
# Python burada sırayla şunları yapıyor:
# a) users listesindeki İLK elemanı alıyor (User(id=101)).
# b) lambda fonksiyonundaki 'u' parametresine atıyor. (u = User(id=101))
# c) u.id'yi okuyor (101) ve kenara koyuyor.
# ... sonra ikinci elemana geçiyor, ona 'u' diyor...
user_ids_iterator = map(lambda u: u.id, users)

# 4. Sonucu görelim (map lazy olduğu için list'e çeviriyoruz)
user_ids = list(user_ids_iterator)

print("Sonuç ID'ler:", user_ids)
# Çıktı: [101, 102, 103]
