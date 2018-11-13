die_faces = {
    "brain": "👍",
    "shotgun": "👎",
    "footprints": "👌"
}

red_die = {
    "faces": tuple(die_faces["brain"] + die_faces["footprints"]*2 + die_faces["shotgun"]*3),
    "occurences": 3
}
"""
red_die = tuple(die_faces["brain"] + die_faces["footprints"]*2 + die_faces["shotgun"]*3)
yellow_die = tuple(die_faces["brain"]*2 + footprints*2 + shotgun*3)
green_die = tuple(brain*3 + footprints*2 + shotgun)
base_dice_cup = tuple((green_die, green_die, green_die, green_die, green_die, green_die, red_die, red_die, red_die, yellow_die, yellow_die, yellow_die, yellow_die))
"""