#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https:\\github.com/Bin4xin
import requests
from lxml import etree


class RuqestError(Exception):
    """请求异常"""
    pass


class ParseError(Exception):
    """解析异常"""
    pass


def requestUri(uri):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    Cookies = {
        'Cookie':'Pycharm-88c590de=f8b6e3eb-809d-4b28-b386-c9cd8bb5bf4d; Hm_lvt_9007fab6814e892d3020a64454da5a55=1669455142;Hm_lpvt_9007fab6814e892d3020a64454da5a55=1669455318'
    }
    response = requests.get(uri, headers=headers, cookies=Cookies)
    response.encoding = "utf-8"
    if response.status_code == 200:
        print("Get OJBK.")
        parseContentByLXML(response.text)
    else:
        raise RuqestError("Get Error, Plz check you uri or change header for your robots.")


"""
xpath定位标签、xpath选择范围，position @link {https://blog.csdn.net/Beyond_F4/article/details/104800739}
11 Xpath知识点整理 @link {https://www.jianshu.com/p/ddac85653526}
# //div[(@class='class')]@content
# // 找标签
#  / 找属性
"""

def parseContentByLXML(html):
    root = etree.HTML(html)
    divs = root.xpath("//div[@class='sons']//div[@class='cont']")
    for div in divs:
        # filter = root.xpath("//div[@class='sons']/@style")
        # print(filter)
        # if filter is not None:
        #######
        sonsTitle = div.xpath('.//p[1]//b/text()')
        sonsAuthor = div.xpath('.//p[2]//a/text()')
        sonsContent = div.xpath('.//div[@class="contson"]//text()')
        sonsTag = div.xpath('.//div[@class="tag"]//a/text()')
        print(sonsTitle, sonsAuthor, sonsContent, sonsTag)
        ####### TODO
        # else:
        #     divs.remove(div)
        #     #print()
        # ;)

requestUri("http://localhost:63342/workspace/Turbo-succotash/crawels/Oldsons.html?_ijt=t3dmuh180pldpcqi4m8ckn5o33&_ij_reload=RELOAD_ON_SAVE")
