from CommandHandler import CommandHandler

# db.create_table("annen1", ["aa", "1a"])

if __name__ == "__main__":
    command_handler = CommandHandler()
    while True:
        try:
            command_handler.main_screen()
        except KeyboardInterrupt:
            command_handler.clear_terminal()
            exit()
