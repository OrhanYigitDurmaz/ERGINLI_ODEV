from os import name, remove, system
from time import sleep

from database import Database


class CommandHandler:
    global db

    DB_SELECT = "11"
    DB_DELETE = "12"
    TABLE_SCREEN = "20"
    TABLE_LIST = "21"
    TABLE_DELETE = "22"
    TABLE_ADD = "23"
    EXIT_PROGRAM = "99"

    def __init__(self) -> None:
        self.db = Database()  # creates database class
        pass

    def main_loop(self) -> None:
        sleep(1)
        self.clear_terminal()
        print(f"""
        SQLITE CLI MERHABA
        Komutlar:
        {self.DB_SELECT}) Veritabanı İsmi Seç: {self.db.db_name}
        {self.TABLE_SCREEN}) Tablo İşlemleri Ekranına git
        {self.DB_DELETE}) Veritabanını SİL (gERİ dÖNÜŞÜ yOK HA)
        {self.EXIT_PROGRAM}) ÇIKIŞ

        """)
        # wait for user input
        secenek = input("Seçiminizi Yapın: ")
        # after this, it should go back to first screen

        self.command(secenek)

    def command(self, command):
        match command:
            case self.DB_SELECT:
                self.select_db()

            case self.DB_DELETE:
                self.clear_terminal()
                print(f"BAK SU VERITABANINI SILIYOM HA: {self.db.db_name}")
                if input("Devam etmek için tam Olarak 'Evet' yaz: ") == "Evet":
                    error, stat = self.delete_db()
                    if stat:
                        print("SİLDİM. benle işin kalmamıştır, çıkıyom")
                    else:
                        print(f"Hata Çıktı: {error}")
                    exit()

                else:
                    print("YANLIS GIRDIN SILMIYOM")
                    sleep(2)

            case self.EXIT_PROGRAM:
                print("GÖRÜŞÇEZ...")
                exit()
            case _:
                print("YANLIS SECIM LA, GERI DON")
                self.clear_terminal()
                pass

    def clear_terminal(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def select_db(self):
        """gets the db name from user, sets it as db_name"""
        self.clear_terminal()
        print("Veritabanı İsmi Ayarlama Ekranı")
        self.db.db_name = input("Veritabanı İsmini Giriniz: ")
        self.main_loop()  # geri dön

    def delete_db(self):
        try:
            remove(self.db.db_name)
            return "True", True
        except FileNotFoundError as e:
            return e, False
