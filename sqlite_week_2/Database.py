import sqlite3


class Database:
    """
    global database handler.

    before calling execute, you need to call connect first.
    this module doesnt handle errors, you are on your own. good luck.
    """

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

    def get_table_columns(self, table_name):
        """returns column names for a table"""
        try:
            result = self.cur.execute(f"PRAGMA table_info({table_name})")
            columns = result.fetchall()
            return [col[1] for col in columns], None  # col[1] is the column name
        except sqlite3.OperationalError as e:
            return None, str(e)

    def insert_row(self, table_name, values):
        """inserts a row into the table"""
        try:
            placeholders = ", ".join(["?" for _ in values])
            self.cur.execute(
                f"INSERT INTO {table_name} VALUES ({placeholders})", values
            )
            self.con.commit()
            return True, None
        except sqlite3.Error as e:
            return False, str(e)

    def delete_row(self, table_name, rowid):
        """deletes a row by rowid"""
        try:
            self.cur.execute(f"DELETE FROM {table_name} WHERE rowid = ?", (rowid,))
            self.con.commit()
            return True, None
        except sqlite3.Error as e:
            return False, str(e)

    def select_all_rows(self, table_name):
        """returns all rows from a table with rowid"""
        try:
            result = self.cur.execute(f"SELECT rowid, * FROM {table_name}")
            rows = result.fetchall()
            return rows, None
        except sqlite3.Error as e:
            return None, str(e)
