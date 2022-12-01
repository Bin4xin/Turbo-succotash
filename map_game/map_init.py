#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https://github.com/Bin4xin

# import time
#
# import pygame
#
#
# def draw_room(_init, begin_point, wells, size, r_color):
#     n = 0
#     for well in wells:
#         print(well)
#         print(n)
#         x = begin_point[0]
#         y = begin_point[1]
#         n += 1
#         if n == 1 and well:
#             print("1::{},{}".format(n,well))
#             pygame.draw.line(_init, r_color, (x, y), (x + size, y))
#         if n == 2 and well:
#             print("2::{},{}".format(n,well))
#             pygame.draw.line(_init, r_color, (x + size, y), (x + size, y + size))
#         if n == 3 and well:
#             print("3::{},{}".format(n,well))
#             pygame.draw.line(_init, r_color, (x + size, y + size), (x, y + size))
#         if n == 4 and well:
#             print("4::{},{}".format(n,well))
#             pygame.draw.line(_init, r_color, (x, y + size), (x, y))
#         time.sleep(0.5)

"""
从任意一个房间开始访问算法中固定是从(0,0)开始,
往四个方向中的随机一个访问(每访问到一个可访问的房间,就去掉到该房间的那个方向的墙),
将这个新房间加入已访问过列表中，从这个访问房间继续以这种方法向下进行访问。

对每个被访问的房间都被标识为已访问,当一个房间对某个方向进行访问时我们首先会判断被访问房间是否已被访问,或者触到边界.如果四个方向
皆已访问或已无法访问,就从已访问列表中退回上一个房间继续这个过程，直到已访问列表长度为0
"""
import pygame
from pygame.locals import *
from random import randint, choice
from assets_config import *


colors = [Aqua, Black, Blue, Fuchsia, Gray, Green, Lime, Maroon, NavyBlue, Olive, Purple, Red, Silver, Teal, Yellow
          ]





class room():
    def __init__(self, x, y):
        self.wells = [True, True, True, True]
        self.visited = False
        self.x = x
        self.y = y


def draw_room(screen, begin_point, wells, size, r_color):
    n = 0
    for well in wells:
        x = begin_point[0]
        y = begin_point[1]
        n += 1
        if n == 1 and well:
            pygame.draw.line(screen, r_color, (x, y), (x + size, y))
        if n == 2 and well:
            pygame.draw.line(screen, r_color, (x + size, y), (x + size, y + size))
        if n == 3 and well:
            pygame.draw.line(screen, r_color, (x + size, y + size), (x, y + size))
        if n == 4 and well:
            pygame.draw.line(screen, r_color, (x, y + size), (x, y))
    return screen


def creat_map(m, n):
    room_list = [[0 for col in range(n)] for row in range(m)]
    for i in range(m):
        for j in range(n):
            room_list[i][j] = room(i, j)
    return room_list


def get_next_room(room_list, room):
    temp_rooms = {1: None,
                  2: None,
                  3: None,
                  4: None}
    temp_room_count = 0
    if (not room.y - 1 < 0) and (not room_list[room.x][room.y - 1].visited):
        temp_rooms[1] = room_list[room.x][room.y - 1]
        temp_room_count += 1
    if (not room.x + 1 > room_m - 1) and (not room_list[room.x + 1][room.y].visited):
        temp_rooms[2] = room_list[room.x + 1][room.y]
        temp_room_count += 1
    if (not room.y + 1 > room_n - 1) and (not room_list[room.x][room.y + 1].visited):
        temp_rooms[3] = room_list[room.x][room.y + 1]
        temp_room_count += 1
    if (not room.x - 1 < 0) and (not room_list[room.x - 1][room.y].visited):
        temp_rooms[4] = room_list[room.x - 1][room.y]
        temp_room_count += 1

    if temp_room_count > 0:
        do = True
        while do:
            room_id = randint(1, 4)
            if temp_rooms[room_id] != None:
                do = False
                next_room = temp_rooms[room_id]
                if room_id == 1:
                    room.wells[0] = 0
                    next_room.wells[2] = 0
                if room_id == 2:
                    room.wells[1] = 0
                    next_room.wells[3] = 0
                if room_id == 3:
                    room.wells[2] = 0
                    next_room.wells[0] = 0
                if room_id == 4:
                    room.wells[3] = 0
                    next_room.wells[1] = 0
        return next_room
    else:
        return None


def creat_migong(room_list, next_room, temp_yes_rooms=[]):
    while True:
        if next_room != None:
            if not next_room.visited:
                next_room.visited = True
                temp_yes_rooms.append(next_room)
            next_room = get_next_room(room_list, next_room)
        else:
            next_room = temp_yes_rooms.pop()
            if len(temp_yes_rooms) == 0: break

        # ********************************************


# ----test-----
# l=creat_map(room_m,room_n)
# r1=l[0][0]
# creat_migong(l,r1)
# for x in range(room_m):
#    for y in range(room_n):
#        print l[x][y].visited,l[x][y].wells
def print_r_list(room_list):
    for i in range(room_m):
        for j in range(room_n):
            print
            room_list[i][j].visited,


# ********************************************
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        #    clock.tick(fps)
    pygame.display.flip()

pygame.quit()