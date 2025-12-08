from typing import List

import Commands


class TableCommandHandler:
    global db

    def __init__(self) -> None:
        pass

    def set_db(self, db):
        self.db = db
        pass

    def table_screen(self):
        Commands.clear_terminal()
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
            case Commands.TABLE_LIST:
                pass
            case Commands.TABLE_ADD:
                pass
            case Commands.TABLE_DELETE:
                pass
            case _:
                "yanlıs secım"
                pass

    def table_add_screen(self):
        print("TABLO EKLEME EKRANI")
        table_name = input("Eklenecek Tablonun İsmini Giriniz: ")
        self.clear_terminal()
        print("TABLO EKLEME EKRANI")
        print(f"Eklenecek Tablo İsmi: {table_name}\n")
        print("Eklenecek Row ismini gir:")
        pass

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

    def get_tables_to_be_added(self) -> List:
        x = 0
        row_list = []
        while x != 1:
            row_name = input("Çıkmak için 0 yazın.\nEklenecek Row İsmini Giriniz: ")
            row_list.append(row_name)
        return row_list
