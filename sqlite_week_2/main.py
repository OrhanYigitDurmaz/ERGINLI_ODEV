from CommandHandler import CommandHandler
from Commands import clear_terminal

# db.create_table("annen1", ["aa", "1a"])

if __name__ == "__main__":
    command_handler = CommandHandler()
    while True:
        try:
            command_handler.main_screen()
        except KeyboardInterrupt:
            clear_terminal()
            exit()
