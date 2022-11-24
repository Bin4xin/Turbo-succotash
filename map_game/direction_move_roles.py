#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https://github.com/Bin4xin

import pygame
import time

pygame.init()
img = pygame.display.set_mode((512, 512))
pygame.display.set_caption("Demo for bin4xin")
img.fill((111, 111, 111))
x = y = 256
pygame.draw.circle(img, (173, 255, 47), (x, y), 8)
pygame.display.update()
"""@link {https://blog.csdn.net/weixin_43201103/article/details/101623587}"""
while True:
    img = pygame.display.set_mode((512, 512))
    img.fill((111, 111, 111))
    pygame.draw.circle(img, (173, 255, 47), (x, y), 8)
    pygame.display.update()
    str = pygame.key.get_pressed()
    if str[pygame.K_RIGHT]:
        x += 5
    elif str[pygame.K_DOWN]:
        y += 5
    elif str[pygame.K_LEFT]:
        x -= 5
    elif str[pygame.K_UP]:
        y -= 5
    elif str[pygame.K_ESCAPE]:
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
