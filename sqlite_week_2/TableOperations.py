from time import sleep
from typing import List

import Commands


class TableOperations:
    global db
    global command_handler

    def __init__(self) -> None:
        pass

    def set_db(self, db):
        self.db = db

    def set_command_handler(self, handler):
        self.command_handler = handler

    def table_screen(self):
        self.command_handler.clear_terminal()
        print(f"""
        TABLO İŞLEMLERİ EKRANI:
        Seçili Veritabanı: {self.db.db_name}
        {Commands.TABLE_LIST}) Tabloları Listele
        {Commands.TABLE_ADD}) Tablo Ekle
        {Commands.TABLE_DELETE}) Tablo Sil
        {Commands.GO_BACK}) Geri Dön
        """)
        command = input("Seçiminizi Yapın: ")
        self.command_table(command)

    def command_table(self, command):
        match command:
            case Commands.TABLE_ADD:
                self.table_add_screen()

            case Commands.TABLE_DELETE:
                self.table_delete_screen()

            case Commands.TABLE_LIST:
                self.table_list_screen()

            case Commands.GO_BACK:
                self.command_handler.main_screen()

            case _:
                print("napıyon amk")

    def table_add_screen(self):
        print("TABLO EKLEME EKRANI")
        table_name = input("Eklenecek Tablonun İsmini Giriniz: ")
        self.command_handler.clear_terminal()
        print("TABLO EKLEME EKRANI")
        print(f"Eklenecek Tablo İsmi: {table_name}\n")

        # TODO: get the row names in a loop???
        column_name = ""
        x = 0
        columns = []
        while x != 1:
            print(f"Eklenecek Columnlar: {columns}")
            column_name = input("Eklenecek Column ismini giriniz: ")
            columns.append(column_name)
            s = input("Devam etmek için enter'a, çıkmak için 1 basın.")
            if not s:
                x = 1
        self.command_handler.clear_terminal()
        print("Ekleniyor...")
        sleep(0.5)
        self.db.create_table(column_name, columns)

    def table_delete_screen(self):
        print("TABLO SİLME EKRANI")
        print("Şu anda olan tablolar:")
        print(self.db.list_tables())
        table = input("Hangi tabloyu silmek istediğinizi yazın:")
        self.db.delete_table(table)
        print("Sanırım silindi. Yanlış bir şey yazmadıysan tabi")

    def table_list_screen(self):
        print("Tablo Listesi:\n")
        print(self.db.list_tables())
        input("Geri gitmek için enter a basın")
        self.table_screen()

    def get_tables_to_be_added(self) -> List:
        x = 0
        row_list = []
        while x != 1:
            row_name = input("Çıkmak için 0 yazın.\nEklenecek Row İsmini Giriniz: ")
            row_list.append(row_name)
        return row_list
