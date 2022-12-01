#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https://github.com/Bin4xin

import pygame
import time
import assets_config
from assets_config import *

global screen_width, screen_height
global room_m, room_n, room_size
pygame.init()
pygame.display.set_caption("Demo for bin4xin")
x = y = 5
# 设置小球的位置
# img = pygame.display.set_mode((512, 512))
# img.fill((111, 111, 111))
# pygame.draw.circle(img, (173, 255, 47), (x, y), 8)
# pygame.display.update()
"""
move role by keyboard. @link {https://blog.csdn.net/weixin_43201103/article/details/101623587}
pygame.key docs @link {https://www.pygame.org/docs/ref/key.html?highlight=k_right}
"""
while True:
    _init = pygame.display.set_mode((screen_width, screen_height))
    # 初始化地图大小为
    _init.fill(assets_config.map_color)
    # 颜色
    pygame.draw.circle(_init, assets_config.roles_color, (x, y), 8)
    # 画个圆，参数分别是画布，颜色，坐标，半径
    # TODO: 在画布需要再进行迷宫墙的绘制。
    from map_init import draw_room, creat_map, creat_migong
    clock = pygame.time.Clock()
    fps = 20
    r_list = creat_map(room_m, room_n)
    begin_point = [0, 0]
    begin_room = r_list[0][0]
    creat_migong(r_list, begin_room)
    for i in range(room_m):
        for j in range(room_n):
            begin_point[0] = 25 + i * room_size
            begin_point[1] = 25 + j * room_size
            r_color = Blue
            draw_room(_init, begin_point, r_list[i][j].wells, room_size, r_color)
    draw_room(_init, [25, 25], [0, 0, 0, 1], 5, White)
    draw_room(_init, [25 + (room_m - 1) * 5, 25 + (room_n - 1) * room_size], [0, 1, 0, 0], room_size, White)
    pygame.display.update()
    inputKeycode = pygame.key.get_pressed()
    if inputKeycode[pygame.K_RIGHT]:
        x += 5
    elif inputKeycode[pygame.K_DOWN]:
        y += 5
    elif inputKeycode[pygame.K_LEFT]:
        x -= 5
    elif inputKeycode[pygame.K_UP]:
        y -= 5
    elif inputKeycode[pygame.K_ESCAPE] or inputKeycode[pygame.K_q]:
        # quit game by type in Q or ESC.
        break
    time.sleep(0.05)

pygame.quit()
# def main():
#     stdscr = curses.initscr()
#     curses.noecho()
#     stdscr.nodelay(True)
#     while True:
#         stdscr.erase()
#         keycode = stdscr.getch()
#         stdscr.addstr(2, 3, "key:{}".format(keycode))
#         if keycode == ord('w'):
#             stdscr.addstr(1,3,"w")
#         elif keycode == ord('s'):
#             stdscr.addstr(1,3,"s")
#         elif keycode == ord('a'):
#             stdscr.addstr(1,3,"a")
#         elif keycode == ord('d'):
#             stdscr.addstr(1,3,"d")
#         elif keycode == ord('q'):
#             exit()
#         stdscr.refresh()
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     main()
