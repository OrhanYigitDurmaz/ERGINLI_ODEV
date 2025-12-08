from codeop import compile_command
from os import name, remove, system
from time import sleep

from database import Database


class CommandHandler:
    global db

    DB_SELECT = "11"
    DB_DELETE = "12"
    DB_CREATE = "13"
    TABLE_SCREEN = "20"
    TABLE_LIST = "21"
    TABLE_DELETE = "22"
    TABLE_ADD = "23"
    EXIT_PROGRAM = "99"
    GO_BACK = "89"

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
        self.command_main(secenek)

    def command_main(self, command):
        match command:
            case self.DB_SELECT:
                self.select_db_screen()

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

            case self.TABLE_SCREEN:
                self.clear_terminal()
                print(f"""
                TABLO İŞLEMLERİ EKRANI:
                Seçili Veritabanı: {self.db.db_name}


                {self.GO_BACK}) Geri Dön
                """)
                command = input("Seçiminizi Yapın: ")
                self.command_table(command)

            case self.EXIT_PROGRAM:
                print("GÖRÜŞÇEZ...")
                exit()
            case _:
                print("YANLIS SECIM LA, GERI DON")
                self.clear_terminal()
                pass

    def command_table(self, command):
        match command:
            case self.TABLE_ADD:
                self.table_add_screen()

            case self.TABLE_DELETE:
                self.table_delete_screen()

            case self.TABLE_LIST:
                self.table_list_screen()

            case self.GO_BACK:
                self.main_loop()

    def clear_terminal(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def select_db_screen(self):
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

    def table_add_screen(self):
        pass

    def table_delete_screen(self):
        print("Şu anda olan tablolar:")
        print(self.db.list_tables())
        table = input("Hangi tabloyu silmek istediğinizi yazın:")
        self.db.delete_table(table)
        print("Sanırım silindi. Yanlısş bir şey yazmadıysan tabi")

    def table_list_screen(self):
        print("Tablo Listesi:\n")
        print(self.db.list_tables())
