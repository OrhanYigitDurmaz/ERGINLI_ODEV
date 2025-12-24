import sqlite3
from pyexpat import ErrorString

DB_NAME = "expense.db"


class Database:
    global con
    global cur

    def __init__(self) -> None:
        pass

    def connect(self) -> bool:
        try:
            self.con = sqlite3.connect(DB_NAME)
        except sqlite3.Error as e:
            print(f"Hata var lan: {e}")
            return False

        self.cur = self.con.cursor()
        return True
