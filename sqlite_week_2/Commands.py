from os import name, system

DB_SELECT = "11"
DB_DELETE = "12"
DB_CREATE = "13"
TABLE_SCREEN = "20"
TABLE_LIST = "21"
TABLE_DELETE = "22"
TABLE_ADD = "23"
ROW_OP = "31"
ROW_ADD = "32"
ROW_DELETE = "33"
ROW_LIST = "34"
EXIT_PROGRAM = "99"
GO_BACK = "89"


def clear_terminal():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
