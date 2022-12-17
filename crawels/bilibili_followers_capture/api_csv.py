#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https://github.com/Bin4xin
import csv
import time

"""
@ 写入csv编码为utf-8
https://blog.51cto.com/chenxiaolong/1839527"""


def writeIntoCSV(time_local, follower_list_start, follower_list_end, reduce_count):
    with open("reduce_log.csv", "a+", encoding="utf-8", newline="") as file:
        f = csv.writer(file)
        rows = [(time_local, follower_list_start, follower_list_end, reduce_count), ]
        f.writerows(rows)


def initCVS():
    with open("reduce_log.csv", "w", encoding="utf-8", newline="") as file:
        head = ["time_local", "start_count", "end_count", "reduce/min"]
        f = csv.writer(file)
        f.writerow(head)
