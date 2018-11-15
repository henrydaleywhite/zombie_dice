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


def settings_view(default_settings):
    return int(input("Number of players:\n"))
    

def player_score(player_tracker, player_scores):
    print("Current score:", player_scores[player_tracker[0]])


def player_start(player):
    print("Player {}'s turn.".format(player[0]))


def player_win(current_player):
    print("Player {} wins!".format(current_player))


def show_turn_options():
    pass


def show_current_dice(dice_in_hand):
    pass