from os import name, remove, system
from time import sleep
from typing import List
from database import Database
import Commands
from . import RowCommands
from . import TableCommands


class CommandHandler():
    global db
    global row_command
    global table_command


    def __init__(self) -> None:
        self.db = Database()  # creates database class
        self.row_command = RowCommands()
        self.table_command = TableCommands()
        pass

    def main_loop(self) -> None:
        sleep(1)
        self.clear_terminal()
        print(f"""
        SQLITE CLI MERHABA
        Komutlar:
        {Commands.DB_SELECT}) Veritabanı İsmi Seç: {self.db.db_name}
        {Commands.TABLE_SCREEN}) Tablo İşlemleri Ekranına git
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
                self.clear_terminal()
                print(f"""
                TABLO İŞLEMLERİ EKRANI:
                Seçili Veritabanı: {self.db.db_name}
                {Commands.ROW_OP}) Row İşlemleri

                {Commands.GO_BACK}) Geri Dön
                """)
                command = input("Seçiminizi Yapın: ")
                self.command_table(command)

            case Commands.EXIT_PROGRAM:
                print("GÖRÜŞÇEZ...")
                exit()
            case _:
                print("YANLIS SECIM LA, GERI DON")
                self.clear_terminal()
                pass

    def command_row(self, command):
        match command:
            case Commands.ROW_ADD:
                pass
            case Commands.ROW_DELETE:
                pass
            case Commands.ROW_LIST:
                pass

        pass

    def command_table(self, command):
        match command:
            case Commands.TABLE_ADD:
                self.table_add_screen()

            case Commands.TABLE_DELETE:
                self.table_delete_screen()

            case Commands.TABLE_LIST:
                self.table_list_screen()

            case Commands.GO_BACK:
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

    def table_add_screen(self):
        print("TABLO EKLEME EKRANI")
        table_name = input("Eklenecek Tablonun İsmini Giriniz: ")
        self.clear_terminal()
        print("TABLO EKLEME EKRANI")
        print(f"Eklenecek Tablo İsmi: {table_name}\n")
        print("Eklenecek Row ismini gir:")
        pass

    def table_delete_screen(self):
        print("Şu anda olan tablolar:")
        print(self.db.list_tables())
        table = input("Hangi tabloyu silmek istediğinizi yazın:")
        self.db.delete_table(table)
        print("Sanırım silindi. Yanlış bir şey yazmadıysan tabi")

    def table_list_screen(self):
        print("Tablo Listesi:\n")
        print(self.db.list_tables())

    def get_table_to_be_added(self) -> List:
        x = 0
        row_list = []
        while x != 1
            row_name = input("Eklenecek Row İsmini Giriniz: ")
            row_list.append(row_name)


        return row_list
