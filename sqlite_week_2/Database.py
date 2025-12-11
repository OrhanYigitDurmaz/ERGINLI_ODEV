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

    def create_table(self, table_name, columns):
        column_str = ""
        for i in columns:
            column_str = column_str + i + ", "

        column_str = column_str[:-2]  # son iki karakteri siliyom ", "
        print(f"CREATE TABLE {table_name}({column_str})")
        try:
            self.cur.execute(f"CREATE TABLE {table_name}({column_str})")
        except sqlite3.OperationalError:
            print("essekoglu essek niye hatalı yazıyon")

    def delete_table(self, table_name):
        try:
            self.cur.execute(f"DROP TABLE IF EXISTS {table_name}")
            self.con.commit()
            return True, None
        except sqlite3.OperationalError as e:
            return False, str(e)

    def list_tables(self):
        """returns a name list"""
        result = self.cur.execute("SELECT name FROM sqlite_master")
        tables = result.fetchall()

        return tables
