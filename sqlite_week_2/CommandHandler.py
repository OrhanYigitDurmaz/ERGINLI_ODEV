from os import name, remove, system
from time import sleep

import Commands
from Database import Database
from RowOperations import RowOperations
from TableOperations import TableOperations


class CommandHandler:
    def __init__(self) -> None:
        self.db = Database()  # creates database class
        self.db.connect(self.db.db_name)

        self.row_op = RowOperations()
        self.table_op = TableOperations()

        self.row_op.set_db(self.db)
        self.table_op.set_db(self.db)

        self.row_op.set_command_handler(self)
        self.table_op.set_command_handler(self)

    def clear_terminal(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def main_screen(self) -> None:
        self.clear_terminal()
        print(f"""
        SQLITE CLI MERHABA
        Komutlar:
        {Commands.DB_SELECT}) Veritabanı İsmi Seç: {self.db.db_name}
        {Commands.TABLE_SCREEN}) Tablo İşlemleri Ekranına git
        {Commands.ROW_OP}) Satır İşlemleri Ekranına git
        {Commands.DB_DELETE}) Veritabanını SİL (gERİ dÖNÜŞÜ yOK HA)
        {Commands.EXIT_PROGRAM}) ÇIKIŞ

        """)
        # wait for user inputprint("TABLO EKLEME EKRANI")
        secenek = input("Seçiminizi Yapın: ")
        self.command_main(secenek)

    def command_main(self, command):
        match command:
            case Commands.DB_SELECT:
                self.select_db_screen()

            case Commands.DB_DELETE:
                self.delete_db_screen()

            case Commands.TABLE_SCREEN:
                self.table_op.table_screen()

            case Commands.ROW_OP:
                self.row_op.row_screen()

            case Commands.EXIT_PROGRAM:
                print("GÖRÜŞÇEZ...")
                exit()
            case _:
                print("YANLIS SECIM LA, GERI DON")
                self.clear_terminal()

    def command_row(self, command):
        match command:
            case Commands.ROW_ADD:
                pass
            case Commands.ROW_DELETE:
                pass
            case Commands.ROW_LIST:
                pass

        pass

    def select_db_screen(self):
        """gets the db name from user, sets it as db_name"""
        self.clear_terminal()
        print("Veritabanı İsmi Ayarlama Ekranı")
        self.db.db_name = input("Veritabanı İsmini Giriniz: ")
        self.main_screen()  # geri dön

    def delete_db_screen(self):
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

    def delete_db(self):
        try:
            remove(self.db.db_name)
            return "True", True
        except FileNotFoundError as e:
            return e, False
