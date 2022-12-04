#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https://github.com/Bin4xin

import requests
from bs4 import BeautifulSoup
import urllib.request


class RuestError(Exception):
    """请求异常"""
    pass


class ParseError(Exception):
    """解析异常"""
    pass


def requestUri(uri):
    headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }
    Cookies = {
        'Cookie': 'Pycharm-88c590de=f8b6e3eb-809d-4b28-b386-c9cd8bb5bf4d; Hm_lvt_9007fab6814e892d3020a64454da5a55=1669455142;Hm_lpvt_9007fab6814e892d3020a64454da5a55=1669455318'
    }
    response = requests.get(uri, headers=headers)
    response.encoding = "utf-8"
    if response.status_code == 200:
        ParseResponse = BeautifulSoup(response.content, 'html.parser')
        parseContentByBS(ParseResponse)
    else:
        raise RuestError("Get Error, Plz check you uri or change header for your robots.")


def parseContentByBS(html):
    # print(html)
    big_div = html.find("div", attrs={"id": "section-container"})
    div_user = big_div.find_all("li")
    for lis in div_user:
        img_title = lis.find("a").get("title")
        img_src = "https:" + lis.find("img").get("data-img")
        #print(img_title, img_src)
        urllib.request.urlretrieve(img_src, "HePingJingYing_Weapons/%s.jpg" % (img_title))


requestUri("http://localhost:63342/workspace/22-12-3/demo.html")