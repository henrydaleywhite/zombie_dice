import model
import view
# default settings for number of players, 
default_settings = {'number of players': 4}
# current player
player_tracker = [1]


def main_menu():
    """Menu for play, settings, quit"""
    while True:
        view.display_menu(default_settings)
        choice = view.main_menu_input()
        if choice not in ('1', '2', '3'):
            view.bad_input()
        # play game
        if choice == '1':
            model.player_start_scores(default_settings['number of players'])
            return True
        # settings
        if choice == '2':
            #TODO add player names?
            default_settings['number of players'] = view.settings_view(default_settings)
            while not 0 < default_settings['number of players'] <= 4:
                view.bad_input()
                default_settings['number of players'] = view.settings_view(default_settings)
        # quit
        if choice == '3':
            view.exit_message()
            return None


def play_game():
    """Parent function for game functionality"""
    while True:
        win_condition = game_round()
        # game will end once a player hits the win condition
        if win_condition:
            view.player_win(player_tracker[0])
            return True    
        # if win condition is not met, increment current player and restock dice
        model.next_player(player_tracker, default_settings['number of players'])
        model.refresh_dice_cup()


def game_round():
    """Functionality for individual player rounds"""
    win_condition = model.player_scores[player_tracker[0]] >= 13
    view.print_bars()
    view.player_start(player_tracker)
    current_shotguns = 0
    round_score = 0
    round_loss_condition = False
    view.player_score(player_tracker, model.player_scores)

    # loops until current player banks or loses
    while win_condition is False and round_loss_condition is False:
        # turn options
        view.show_current_dice(model.dice_in_hand)
        view.show_turn_options()
        turn_input = view.turn_choice_input()

        # evaluate turn input
        if turn_input not in ('1', '2'):
            view.bad_input()
        # roll dice option
        elif turn_input == '1':
            # draw and roll dice
            view.print_bars()
            model.pull_dice()
            view.show_current_dice(model.dice_in_hand)
            roll_result = model.choice_roll_dice()
            view.show_roll_result(roll_result)
            view.print_bars()

            # store results in more usable format and print
            current_shotguns += model.count_shotguns(roll_result)
            round_score += model.count_brains(roll_result)
            model.remove_brain_shotgun_post_roll(roll_result)
            view.round_so_far(current_shotguns, round_score, model.dice_in_hand)
            view.print_bars()

            # evaluate if player has met round loss condition
            round_loss_condition = model.check_loss(current_shotguns)
            if round_loss_condition:
                view.three_shot_message()
        # bank score option
        else:
            # total player's score, evaluate win condition, break loop
            model.choice_bank_score(player_tracker[0], round_score)
            view.bank_message()
            view.player_score(player_tracker, model.player_scores)
            win_condition = model.player_scores[player_tracker[0]] >= 13
            break
    # return whether current player has met win condition after most recent round
    return win_condition
        

if __name__ == "__main__":
    main_menu = main_menu()
    if main_menu:
        play_game()