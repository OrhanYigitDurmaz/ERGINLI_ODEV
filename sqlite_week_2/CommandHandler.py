from os import name, remove, system
from time import sleep
from typing import List

import Commands
from Database import Database
from RowCommandHandler import RowCommandHandler
from TableCommandHandler import TableCommandHandler


class CommandHandler:
    global db
    global row_command
    global table_command

    def __init__(self) -> None:
        self.db = Database()  # creates database class
        self.row_command = RowCommandHandler()
        self.table_command = TableCommandHandler()

        self.row_command.set_db(self.db)
        self.table_command.set_db(self.db)
        pass

    def main_screen(self) -> None:
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
                self.table_command.command()

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
                self.main_screen()

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

    