#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https://github.com/Bin4xin
import matplotlib.pyplot as plt
from api_csv import writeIntoCSV, initCVS
import time
import data_capture_bilibili_for_followers as blf

plt.ion()
t = []
# x
v = []
# y
fig = plt.figure()
ax1 = fig.add_subplot(111)
line, = ax1.plot(t, v, linestyle="-", color="r")


def printDraw(a, b):
    t.append(a)
    v.append(b)
    # print("t:{}".format(t))
    # print("v:{}".format(v))
    ax1.set_xlim(min(t), max(t) + 1)
    ax1.set_ylim(min(v) - 200, max(v) + 200)
    # start from (start, end) start -> end.
    line.set_data(t, v)
    plt.pause(1.5)
    ax1.figure.canvas.draw()


initCVS()
while True:
    """REF
    bilibili API ref from: @link 
    {https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/user/status_number.md#UP%E4%B8%BB%E7%8A%B6%E6%80%81%E6%95%B0}
    """
    # 11 - 26 followers: 7114514 https://live.bilibili.com/919187?spm_id_from=333.880.0.0
    # follower_list.append(7114514)
    # follower_list = [7114514]
    follower_list = []

    # follower_list 不定长，所以会有重复绘制。
    for i in range(0, 60 * 60 * 2, 1):
        follower = blf.parseContentByBS(blf.requestUri("https://api.bilibili.com/x/relation/stat?vmid=122879"))
        follower_list.append(follower)
        printDraw(i, follower_list[i])
        # follower = blf.parseContentByBS(blf.requestUri("https://api.bilibili.com/x/relation/stat?vmid=122879"))
        # follower_list.append(follower)
        if i % 60 == 0 and i != 0:
            time_local = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            reduce_count = follower_list[i - 60] - follower_list[i]
            print("每分钟减少：{}".format(reduce_count))
            writeIntoCSV(time_local, follower_list[i - 60], follower_list[i], reduce_count)
    time.sleep(1)
