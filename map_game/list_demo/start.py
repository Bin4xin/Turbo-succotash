from lib.judge import  allow_Pass_orNot
from assets.map import map
from assets.map import map_init
from lib.clear import clear


def start_game():
    x = 1
    y = 1
    _init_location = map[x][y]
    while _init_location != map[2][11]:
        # TODO replace up down right left from type input.
        move = input("请输入移动方向[w/s/a/d](q退出游戏)：")
        """ need to place x,y into judge. In another way, just replace roles to space before judge() """
        if move == "s":
            """while role in 11,1. player will be alerted "撞墙", but can't move to "wall". """
            if allow_Pass_orNot(map, x+1, y) == "false":
                map[x][y] = " "
                x += 1
                map[x][y] = "O"
                """While player operate role to move. Replace <space> to O, means move one step."""
            else:
                """ else, role can't move. """
                print("你撞墙啦")
        elif move == "d":
            if allow_Pass_orNot(map, x, y+1) == "false":
                map[x][y] = " "
                y += 1
                map[x][y] = "O"
            else:
                print("你撞墙啦")
        elif move == "w":
            if allow_Pass_orNot(map, x-1, y) == "false":
                map[x][y] = " "
                x -= 1
                map[x][y] = "O"
        elif move == "a":
            if allow_Pass_orNot(map, x, y-1) == "false":
                map[x][y] = " "
                y -= 1
                map[x][y] = "O"
            else:
                print("你撞墙啦")
        elif move == "q":
            exit()
        else:
            print("Plz type in [w/s/a/d]！(q退出游戏)")
        clear()
        map_init()
    else:
        print("You Win!")
