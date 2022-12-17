#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https://github.com/Bin4xin
import requests


def requestUri(uri):
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 Edg/107.0.1418.62"
    }
    response = requests.get(uri, headers=headers).json()
    return response


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
    followers = data['follower']
    # follower_list.append(followers)
    return followers


"""
Next TODO:
I. ~~Data persistence~~
II. Data visualization Data_visualization_Demo.py
"""
