import Commands


class RowOperations:
    global db
    global command_handler

    def __init__(self) -> None:
        pass

    def set_db(self, db):
        self.db = db

    def set_command_handler(self, handler):
        self.command_handler = handler
