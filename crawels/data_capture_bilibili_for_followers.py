#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https://github.com/Bin4xin
import requests
import time
from bs4 import BeautifulSoup


def requestUri(uri):
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 Edg/107.0.1418.62"
    }
    response = requests.get(uri, headers=headers).json()
    parseContentByBS(response)


def parseContentByBS(response):
    """ REF @link { https://www.runoob.com/python/python-dictionary.html }
    dict = {'Name': 'Runoob', 'Age': 7}
    print(dict['Age'])
    """
    data = response["data"]
    """
    for data in response["data"]: !!!WRONG FOR LOOP {if there just one json->dict }!!!
    {'mid': int, 'following': int, 'whisper': 0, 'black': 0, 'follower': int}
    data: 'follower': int
    looks like a int type.
    """
    print(data['follower'])
    """
    Next TODO:
    I. Data persistence
    II. data visualization 22-12-4\day02-4.py
    """


while True:
    """REF
    bilibili API ref from: @link 
    {https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/user/status_number.md#UP%E4%B8%BB%E7%8A%B6%E6%80%81%E6%95%B0}
    """
    requestUri("https://api.bilibili.com/x/relation/stat?vmid=122879")
    time.sleep(3)
