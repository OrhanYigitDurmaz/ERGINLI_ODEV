from time import sleep

import Commands


class RowOperations:
    def __init__(self) -> None:
        self.selected_table = None

    def set_db(self, db):
        self.db = db

    def set_command_handler(self, handler):
        self.command_handler = handler

    def row_screen(self):
        self.command_handler.clear_terminal()

        # Show table selection if no table is selected
        if self.selected_table is None:
            self.select_table_screen()
            if self.selected_table is None:
                return

        print(f"""
        SATIR İŞLEMLERİ EKRANI:
        Seçili Veritabanı: {self.db.db_name}
        Seçili Tablo: {self.selected_table}
        {Commands.ROW_LIST}) Satırları Listele
        {Commands.ROW_ADD}) Satır Ekle
        {Commands.ROW_DELETE}) Satır Sil
        {Commands.GO_BACK}) Geri Dön
        """)
        command = input("Seçiminizi Yapın: ")
        self.command_row(command)

    def command_row(self, command):
        match command:
            case Commands.ROW_ADD:
                self.row_add_screen()

            case Commands.ROW_DELETE:
                self.row_delete_screen()

            case Commands.ROW_LIST:
                self.row_list_screen()

            case Commands.GO_BACK:
                self.selected_table = None
                self.command_handler.main_screen()

            case _:
                print("Geçersiz seçim!")
                sleep(1)
                self.row_screen()

    def select_table_screen(self):
        self.command_handler.clear_terminal()
        print("TABLO SEÇİMİ")
        tables = self.db.list_tables()

        if not tables:
            print("Hiç tablo bulunamadı!")
            input("Geri dönmek için enter'a basın.")
            self.command_handler.main_screen()
            return

        print("Mevcut tablolar:")
        for i, table in enumerate(tables, 1):
            print(f"  {i}) {table[0]}")

        print(f"  0) Geri Dön")

        choice = input("\nTablo numarasını seçin: ")

        try:
            choice_num = int(choice)
            if choice_num == 0:
                self.command_handler.main_screen()
                return
            if 1 <= choice_num <= len(tables):
                self.selected_table = tables[choice_num - 1][0]
            else:
                print("Geçersiz seçim!")
                sleep(1)
                self.select_table_screen()
        except ValueError:
            print("Lütfen bir sayı girin!")
            sleep(1)
            self.select_table_screen()

    def row_add_screen(self):
        self.command_handler.clear_terminal()
        print(f"SATIR EKLEME EKRANI - Tablo: {self.selected_table}\n")

        columns, error = self.db.get_table_columns(self.selected_table)

        if error:
            print(f"Hata: {error}")
            input("Devam etmek için enter'a basın.")
            self.row_screen()
            return

        if not columns:
            print("Bu tabloda hiç kolon bulunamadı!")
            input("Devam etmek için enter'a basın.")
            self.row_screen()
            return

        print(f"Kolonlar: {columns}\n")

        values = []
        for col in columns:
            value = input(f"'{col}' için değer girin: ")
            values.append(value)

        print("\nEkleniyor...")
        sleep(0.5)

        success, error = self.db.insert_row(self.selected_table, values)

        if success:
            print("Satır başarıyla eklendi!")
        else:
            print(f"Hata oluştu: {error}")

        input("Devam etmek için enter'a basın.")
        self.row_screen()

    def row_delete_screen(self):
        self.command_handler.clear_terminal()
        print(f"SATIR SİLME EKRANI - Tablo: {self.selected_table}\n")

        rows, error = self.db.select_all_rows(self.selected_table)

        if error:
            print(f"Hata: {error}")
            input("Devam etmek için enter'a basın.")
            self.row_screen()
            return

        if not rows:
            print("Bu tabloda hiç satır bulunamadı!")
            input("Devam etmek için enter'a basın.")
            self.row_screen()
            return

        columns, _ = self.db.get_table_columns(self.selected_table)

        print(f"{'ROWID':<8} | {' | '.join(columns)}")
        print("-" * 50)

        for row in rows:
            rowid = row[0]
            values = row[1:]
            print(f"{rowid:<8} | {' | '.join(str(v) for v in values)}")

        print()
        rowid_to_delete = input(
            "Silmek istediğiniz satırın ROWID'sini girin (0 = iptal): "
        )

        try:
            rowid_num = int(rowid_to_delete)
            if rowid_num == 0:
                self.row_screen()
                return

            success, error = self.db.delete_row(self.selected_table, rowid_num)

            if success:
                print("Satır başarıyla silindi!")
            else:
                print(f"Hata oluştu: {error}")
        except ValueError:
            print("Geçersiz ROWID!")

        input("Devam etmek için enter'a basın.")
        self.row_screen()

    def row_list_screen(self):
        self.command_handler.clear_terminal()
        print(f"SATIR LİSTESİ - Tablo: {self.selected_table}\n")

        rows, error = self.db.select_all_rows(self.selected_table)

        if error:
            print(f"Hata: {error}")
            input("Devam etmek için enter'a basın.")
            self.row_screen()
            return

        if not rows:
            print("Bu tabloda hiç satır bulunamadı!")
            input("Devam etmek için enter'a basın.")
            self.row_screen()
            return

        columns, _ = self.db.get_table_columns(self.selected_table)

        print(f"{'ROWID':<8} | {' | '.join(columns)}")
        print("-" * 50)

        for row in rows:
            rowid = row[0]
            values = row[1:]
            print(f"{rowid:<8} | {' | '.join(str(v) for v in values)}")

        print(f"\nToplam {len(rows)} satır bulundu.")
        input("\nGeri gitmek için enter'a basın.")
        self.row_screen()
