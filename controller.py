import model
import view
# default settings for number of players, 
default_settings = [4]


def main_menu():
    exit_condition = False
    while not exit_condition:
        view.display_menu(default_settings)
        choice = view.main_menu_input()
        if choice not in ('1', '2', '3'):
            view.bad_input()
        if choice == '1':
            pass
        if choice == '2':
            view.settings_menu(default_settings)
            if not 0 < default_settings[0] <= 4:
                view.bad_input()
                view.settings_menu(default_settings)
        if choice == '3':
            view.exit_message()
            exit_condition = True


if __name__ == "__main__":
    main_menu()