def display_menu(default_settings):
    print("Welcome to Zombie Dice!\n")
    print("1. Play")
    print("2. Number of players - currently", default_settings[0])
    print("3. Exit")


def main_menu_input():
    return input("Selection: ")


def bad_input():
    print("\nBad input, please try again\n")


def exit_message():
    print("\nGoodbye!\n")


def settings_menu(default_settings):
    default_settings[0] = int(input("Number of players:\n"))
    if not 0 < default_settings[0] <= 4:
        bad_input()
        settings_menu(default_settings)
