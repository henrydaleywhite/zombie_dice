import random

dice_in_hand = []

DIE_FACES = {
    "brain": "👍",
    "shotgun": "👎",
    "footprints": "👌"
}


RED_DIE = {
    1: "shotgun",
    2: "shotgun",
    3: "shotgun",
    4: "footprints",
    5: "footprints",
    6: "brain"
}


GREEN_DIE = {
    1: "shotgun",
    2: "footprints",
    3: "footprints",
    4: "brain",
    5: "brain",
    6: "brain"
}


YELLOW_DIE = {
    1: "shotgun",
    2: "shotgun",
    3: "footprints",
    4: "footprints",
    5: "brain",
    6: "brain"
}


player_scores = {}


# base dice cup has green x 6, yellow x 4, red x 3
dice_cup = [
    GREEN_DIE, GREEN_DIE, GREEN_DIE, GREEN_DIE, GREEN_DIE, GREEN_DIE, 
    YELLOW_DIE, YELLOW_DIE, YELLOW_DIE, YELLOW_DIE, 
    RED_DIE, RED_DIE, RED_DIE
]


def player_start_scores(num_players):
    for i in range(1,num_players+1):
        player_scores[i] = 0


def pull_dice():
    MAX_HAND = 3
    for i in range(MAX_HAND-len(dice_in_hand)):
	    die_index = random.randint(0,len(dice_cup)-1)
	    drawn_die = dice_cup.pop(die_index)
	    dice_in_hand.append(drawn_die)

def next_player(current_player, number_players):
    current_player[0] = (current_player % number_players) + 1