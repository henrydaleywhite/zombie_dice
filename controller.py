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
        win_condition = game_round()
        if win_condition:
            view.player_win(player_tracker[0])
            return True    
        model.next_player(player_tracker, default_settings[0])
        break


def game_round():
    win_condition = model.player_scores[player_tracker[0]] >= 13
    view.player_start(player_tracker)
    current_shotguns = 0
    round_loss_condition = False
    while win_condition == False and round_loss_condition == False:
        view.player_score(player_tracker, model.player_scores)
        model.pull_dice()
        view.show_current_dice(model.dice_in_hand)
        view.show_turn_options()
        turn_input = view.turn_choice_input()
        if turn_input not in ('1', '2'):
            view.bad_input()
        elif turn_input == '1':
            roll_result = model.choice_roll_dice()
            round_loss_condition = model.check_loss(current_shotguns)
        else:
            #TODO implement meaningful round_score functionality
            round_score = 1 
            model.choice_bank_score(player_tracker[0], round_score)
            view.player_score(player_tracker, model.player_scores)
        break
    return win_condition
        

if __name__ == "__main__":
    main_menu = main_menu()
    if main_menu:
        play_game()