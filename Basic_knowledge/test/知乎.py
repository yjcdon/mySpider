import os
import threading
import time
import random

import requests
from lxml import etree
from tqdm import tqdm

headers = {
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': '_zap=22a23326-25b4-48f0-864d-8fea5565eedc; d_c0="ADCfCQKYOBWPTjdcZFF9gLXR8ZY9BQoJeho=|1657355197"; theme=dark; q_c1=3eaef45ca97a439e9fed4cb457bbc37d|1658915045000|1658915045000; __utma=155987696.45695629.1674726372.1674726372.1674726372.1; __utmz=155987696.1674726372.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); q_c1=3eaef45ca97a439e9fed4cb457bbc37d|1674728429000|1658915045000; wzaIsOn=true; speakVolume=0; readStatus=pointRead; batchReadIsOn=false; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; z_c0=2|1:0|10:1677933180|4:z_c0|80:MS4xLW9wOEN3QUFBQUFtQUFBQVlBSlZUY1JhNkdUWE5sOHMwaTdvMXdxeWV4SXJDdENES0RoY19nPT0=|0f955f14df0a01a14dd91213a694334c50fd8c84e866316810e62d115fd36d1c; _xsrf=e1313f16-f81a-438a-ab38-8bf1a1526317; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1677903912,1677906987,1677948467,1678000078; tst=r; SESSIONID=CvkmBzWuUUpigKA6u6UYY4CdnGEDNT658hixFqfLxMH; JOID=W10dBUl1fC0BURjDPHp7Pij-85goOgdIaBhumUcrJVBmMliOB7rrI2pWGcA2JgAIN15OaeZfnJbCgZ7E0NcxQwo=; osd=UlkcAk58eCwGVhHHPX18Nyz_9J8hPgZPbxFqmEAsLFRnNV-HA7vsJGNSGMcxLwQJMFlHbedYm5_GgJnD2dMwRA0=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1678021844; KLBRSID=f48cb29c5180c5b0d91ded2e70103232|1678022129|1678016222',
    'referer': 'https://www.zhihu.com/question/587490449',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-ab-pb': 'ClIbAD8ARwC0AGkBagF0ATsCzALXAtgCtwPWBBEFUQWLBYwFngUxBusGJwd0CHkIYAn0CUkKawq+CkMLcQuHC40L1wvgC+UL5gtxDI8MrAzDDPgMEikAAAAAAgEAAQAAAAAEAAEAAAEAAQAABgIDAAAAAQAABQIAAAAGAAACAA==',
    'x-requested-with': 'fetch',
    'x-zse-93': '101_3_3.0',
    'x-zse-96': '2.0_U4II0bjJ6k8psFUxAPQRQTLefxb/qP1Z5+s3xoziNvO8xs+0soMl8R8umMwaYpFB',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}


# 调用该函数后,文件指针指向该文件夹
def makedir(path):
    isExists = os.path.exists(os.path.join("path", path))
    if not isExists:
        # print('系统中无该文件夹,创建的地址是:', path)
        # 创建文件夹
        os.makedirs(os.path.join("path", path))
        # 切换到创建的文件夹
        os.chdir(os.path.join("path", path))
        return True
    else:
        # print(path, '该地址的文件夹已存在')
        os.chdir(os.path.join("path", path))
        return False


def getQuestionTitle(url):
    r = requests.get(url=url, headers=headers).text
    questionTitle = etree.HTML(r).xpath('//*[@id="root"]/div/main/div/div/div[1]/div[2]/div/div[1]/div[1]/h1/text()')
    return questionTitle


if __name__ == '__main__':
    url = input('输入问题的URL：')
    qt = getQuestionTitle(url)
    print(qt)
