"""
Here a <1x1> list with another <1x1> list combined into a two-dimensional list <2x2>
Or maybe import random lib. Combined a random map.
"""
# TODO random map combined
map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "O", "#", " ", " ", " ", "#", " ", " ", "#", "#", "#"],
    ["#", " ", "#", " ", "#", " ", " ", " ", "#", "#", " ", " "],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#", "#", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", " ", " ", "#", " ", "#", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#", " ", "#", "#"],
    ["#", " ", "#", " ", "#", "#", " ", " ", "#", " ", "#", "#"],
    ["#", " ", "#", " ", "#", "#", " ", "#", "#", " ", "#", "#"],
    ["#", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]


def map_init():
    for a in map:
        print('\r', list(a), end='\n')
