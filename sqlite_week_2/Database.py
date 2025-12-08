import sqlite3


class Database:
    """
    global database handler.

    before calling execute, you need to call connect first.
    this module doesnt handle errors, you are on your own. good luck.
    """

    global db_name
    global con
    global cur

    def __init__(self) -> None:
        self.db_name = "deneme.db"
        self.con = None
        # self.cur = None
        pass

    def connect(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def execute(self, sql):
        self.cur.execute(sql)

    def create_table(self, table_name, rows):
        row_str = ""
        for i in rows:
            row_str = row_str + i + ", "

        row_str = row_str[:-2]  # son iki karakteri siliyom ", "

        self.cur.execute(f"CREATE TABLE {table_name}({row_str})")

    def delete_table(self, table_name):
        self.cur.execute(f"DELETE TABLE {table_name}")
        return True  # TODO: add proper error return

    def list_tables(self):
        """returns a name list"""
        result = self.cur.execute("SELECT name FROM sqlite_master")
        return result.fetchall()
