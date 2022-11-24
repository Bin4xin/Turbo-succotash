def allow_Pass_orNot(map, x, y):
    flag = "true"
    for index in map:
        if map[x][y] == "#":
            return flag
        elif map[x][y] != "#":
            flag = "false"
            return flag
