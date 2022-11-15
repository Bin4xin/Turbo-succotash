from lib.judge import judge
from assets.map import map
from assets.map import map_init
from lib.clear import clear


def start_game():

    x = 1
    y = 1
    _init_location = map[x][y]
    while _init_location != map[2][11]:
        move = input("请输入移动方向[w/s/a/d]：")
        # TODO need to place x,y into judge. In another way, just replace roles to space before judge()
        if move == "s":
            x += 1
            map[x - 1][y] = " "
            judge(map, x, y)
        elif move == "d":
            y += 1
            map[x][y - 1] = " "
            judge(map, x, y)
        elif move == "w":
            x -= 1
            map[x + 1][y] = " "
            judge(map, x, y)
        elif move == "a":
            y -= 1
            map[x][y + 1] = " "
            judge(map, x, y)
        elif move == "Q":
            exit()
        else:
            print("Plz type in [w/s/a/d]！")
        clear()
        map_init()
        if map[2][11] == "O":
            print("You Win!")
