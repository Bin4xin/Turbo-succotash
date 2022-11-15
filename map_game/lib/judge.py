def judge(map, x, y):
    # print(x, y)
    if map[x][y] == " ":
        map[x][y] = "O"
    else:
        print("你撞墙啦")
        # return
        exit()  # TODO: return 撞墙之前的x y值，游戏继续。
