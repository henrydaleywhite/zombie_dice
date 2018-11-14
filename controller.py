import model
import view
# default settings for number of players, 
default_settings = [4]
player_tracker = [1]


def main_menu():
    while True:
        view.display_menu(default_settings)
        choice = view.main_menu_input()
        if choice not in ('1', '2', '3'):
            view.bad_input()
        if choice == '1':
            return True
        if choice == '2':
            view.settings_menu(default_settings)
            if not 0 < default_settings[0] <= 4:
                view.bad_input()
                view.settings_menu(default_settings)
        if choice == '3':
            view.exit_message()
            return None


def play_game():
    while True:
        view.player_start(player_tracker)
        break


if __name__ == "__main__":
    main_menu = main_menu()
    if main_menu:
        play_game()