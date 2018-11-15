import model
import view
# default settings for number of players, 
default_settings = [4]
# current player
player_tracker = [1]


def main_menu():
    while True:
        view.display_menu(default_settings)
        choice = view.main_menu_input()
        if choice not in ('1', '2', '3'):
            view.bad_input()
        if choice == '1':
            model.player_start_scores(default_settings[0])
            return True
        if choice == '2':
            #TODO add player names?
            default_settings[0] = view.settings_view(default_settings)
            while not 0 < default_settings[0] <= 4:
                view.bad_input()
                default_settings[0] = view.settings_view(default_settings)
        if choice == '3':
            view.exit_message()
            return None


def play_game():
    while True:
        win_condition = model.player_scores[player_tracker[0]] >= 13
        view.player_start(player_tracker)
        current_shotguns = 0
        round_loss_condition = current_shotguns >= 3
        while not win_condition or round_loss_condition
            view.player_score(player_tracker, model.player_scores)
            model.pull_dice()
            view.show_current_dice(model.dice_in_hand)
            view.show_turn_options()
        if win_condition:
            view.player_win(player_tracker[0])
            return True    
        model.next_player(player_tracker, default_settings[0])

        

if __name__ == "__main__":
    main_menu = True
    while main_menu:
        main_menu = main_menu()
        if main_menu:
            play_game()