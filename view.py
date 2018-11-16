def display_menu(default_settings):
    """Display options for main menu"""
    print("Welcome to Zombie Dice!\n")
    print("1. Play")
    print("2. Number of players - currently", default_settings['number of players'])
    print("3. Exit")


def main_menu_input():
    """Input based on options in display_menu"""
    return input("Selection: ")


def bad_input():
    """Generic bad input message"""
    print("\nBad input, please try again\n")


def exit_message():
    """Message for quitting"""
    print("\nGoodbye!\n")


def settings_view(default_settings):
    """Display options for settings"""
    return int(input("Number of players:\n"))
    

def player_score(player_tracker, player_scores):
    """Display player's banked score"""
    print("Player's cumulative score is", player_scores[player_tracker[0]])


def player_start(player):
    """Display whose turn it is"""
    print("Player {}'s turn.".format(player[0]))


def player_win(current_player):
    """Display the player that won"""
    print("Player {} wins!".format(current_player))


def show_turn_options():
    """Display turn options"""
    print("1. Roll Dice")
    print("2. Bank Score")


def turn_choice_input():
    """Input based on options in show_turn_options"""
    return(input("Your choice: "))


def show_current_dice(dice_in_hand):
    """Display the dice that the player currently holds"""
    hand_str = ""
    for die in dice_in_hand:
        hand_str += die['color'] + " Die, "
    print("Dice in hand: {}".format(hand_str[:len(hand_str) - 2]))
    print()

def show_roll_result(result):
    """Display the results of the three die rolls"""
    for i in range(3):
        print("{} die had result {}.".format(result[i][0], result[i][1]))


def round_so_far(shotguns, points, remaining_dice):
    """Display status of current round"""
    hand_str = ""
    print("Overall Status: ")
    print("{} points accumulated".format(points))
    print("{} shotguns hits sustained".format(shotguns))
    for die in remaining_dice:
        hand_str += die['color'] + " Die, "
    print("Remaining hand is {}".format(hand_str[:len(hand_str) - 2]))


def print_bars():
    """Cosmetic print line breaks and a line for sanity"""
    print("\n", "-"*30, "\n")


def three_shot_message():
    """Loss message"""
    print("3+ shotgun hits, player loses this round's points")


def bank_message():
    """Display for a player banking round points"""
    print("Player has banked this round's points")    