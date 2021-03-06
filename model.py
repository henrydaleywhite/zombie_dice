import random

dice_in_hand = []

MAX_HAND_SIZE = 3

# lookup for emoji results should they be used for display in later design
DIE_FACES = {
    "brain": "👍",
    "shotgun": "👎",
    "footprints": "👌"
}


RED_DIE = {
    "color": "Red",
    "faces": {
        1: "shotgun",
        2: "shotgun",
        3: "shotgun",
        4: "footprints",
        5: "footprints",
        6: "brain"
    }
}


GREEN_DIE = {
    "color": "Green",
    "faces": {
        1: "shotgun",
        2: "footprints",
        3: "footprints",
        4: "brain",
        5: "brain",
        6: "brain"
    }
}


YELLOW_DIE = {
    "color": "Yellow", 
    "faces": {
        1: "shotgun",
        2: "shotgun",
        3: "footprints",
        4: "footprints",
        5: "brain",
        6: "brain"
    }
}


player_scores = {}


# base dice cup has green x 6, yellow x 4, red x 3
dice_cup = [
    GREEN_DIE, GREEN_DIE, GREEN_DIE, GREEN_DIE, GREEN_DIE, GREEN_DIE, 
    YELLOW_DIE, YELLOW_DIE, YELLOW_DIE, YELLOW_DIE, 
    RED_DIE, RED_DIE, RED_DIE
]


def player_start_scores(num_players):
    """Populate a blank dictionary with the number of players and starting score 0"""
    for i in range(1, num_players + 1):
        player_scores[i] = 0


def pull_dice():
    """Draw until player has 3 dice in hand"""
    for i in range(MAX_HAND_SIZE - len(dice_in_hand)):
        # pull random number between 0 and the number of dice in the cup
	    die_index = random.randint(0, len(dice_cup) - 1)
	    drawn_die = dice_cup.pop(die_index)
	    dice_in_hand.append(drawn_die)


def next_player(current_player, number_players):
    """Move to next player, mod included to cycle back to first player"""
    current_player[0] = (current_player[0] % number_players) + 1


def check_loss(current_shotguns):
    """Round ends if a player has rolled 3 or more shotguns"""
    return current_shotguns >= 3
        

def choice_roll_dice():
    """Die rolling- returns color, text result, and emoji for each rolled die"""
    roll_results = [[], [], []]
    for i in range(MAX_HAND_SIZE):
        roll_int = random.randint(1, 6)
        die_color = dice_in_hand[i]['color']
        die_result = dice_in_hand[i]['faces'][roll_int]
        die_result_symbol = DIE_FACES[die_result]
        roll_results[i] = [die_color, die_result, die_result_symbol]
    # list of 3 lists with 3 elements each
    return roll_results


def choice_bank_score(current_player, round_score):
    """Add score from this round to cumulative player score when player banks"""
    player_scores[current_player] += round_score


def count_shotguns(result):
    """Count shotguns present in most recent roll for remaining lives"""
    shot_count = 0
    for i in range(MAX_HAND_SIZE):
        if result[i][1] == "shotgun":
            shot_count += 1
    return shot_count


def count_brains(result):
    """Count brains present in most recent roll for round score"""
    brain_count = 0
    for i in range(MAX_HAND_SIZE):
        if result[i][1] == "brain":
            brain_count += 1
    return brain_count


def remove_brain_shotgun_post_roll(result):
    """Remove dice that rolled a brain or a shotgun from current hand (dice_in_hand)"""
    for i in range(MAX_HAND_SIZE-1, -1, -1):
        if result[i][1] in ("brain", "shotgun"):
            dice_in_hand.pop(i)


def refresh_dice_cup():
    """Restock cup with 13 dice between players"""
    global dice_cup
    dice_cup = [
    GREEN_DIE, GREEN_DIE, GREEN_DIE, GREEN_DIE, GREEN_DIE, GREEN_DIE, 
    YELLOW_DIE, YELLOW_DIE, YELLOW_DIE, YELLOW_DIE, 
    RED_DIE, RED_DIE, RED_DIE
]


def refresh_dice_in_hand():
    """Reset dice in hand variable between players"""
    global dice_in_hand
    dice_in_hand = []