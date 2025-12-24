import sqlite3


class Database:
    def __init__(self, db_dosyasi):
        self.connection = sqlite3.connect(db_dosyasi)
        self.imlec = self.connection.cursor()
        self.imlec.execute("""CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY,
            name text,
            surname text,
            phonenumber text
        )""")
        self.connection.commit()

    def kisi_ekle(self, ad, soyad, tel):
        self.imlec.execute(
            "INSERT INTO people VALUES (NULL, ?, ?, ?)", (ad, soyad, tel)
        )
        self.connection.commit()

    def kisileri_getir(self):
        self.imlec.execute("SELECT * FROM people")
        return self.imlec.fetchall()

    def kisi_sil(self, id):
        self.imlec.execute(f"DELETE FROM people WHERE id={id}")
        self.connection.commit()

    def __del__(self):
        # Automatically close connection when the object is destroyed
        self.connection.close()
