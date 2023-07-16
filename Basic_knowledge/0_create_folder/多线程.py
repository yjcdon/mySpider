import requests
import os
from lxml import etree
import threading
import time
# 用于:https://www.meitu131.com/

def makedir(path):
    isExists = os.path.exists(os.path.join("path", path))
    if not isExists:
        print('系统中无该文件夹,创建的地址是:', path)
        # 创建文件夹
        os.makedirs(os.path.join("path", path))
        # 切换到创建的文件夹
        os.chdir(os.path.join("path", path))
        return True
    else:
        print(path, '该地址的文件夹已存在')
        os.chdir(os.path.join("path", path))
        return False


def getName(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    r = requests.Session().get(url=url, headers=headers).text
    albumName = etree.HTML(r).xpath('//*[@id="main-wrapper"]/div[1]/h1/text()')[0].encode('ISO-8859-1').decode('utf-8')
    return albumName


def getMaxPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    r = requests.Session().get(url=url, headers=headers).text
    maxPage = int(str(etree.HTML(r).xpath('//*[@id="pages"]/a[1]/text()')[0]).lstrip('1/'))
    if maxPage < 19:
        maxPage = maxPage + 10
    return maxPage


def getImgsURL(url, maxPage):
    imgsURLList = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    for i in range(maxPage):
        if i == 0:
            webURL = url
        else:
            webURL = url + 'index_' + str(i + 1) + '.html'

        r = requests.Session().get(url=webURL, headers=headers).text
        imgsURL = etree.HTML(r).xpath('//*[@id="main-wrapper"]/div[2]/p/a/img/@src')[0]
        imgsURLList.append(imgsURL)
    return imgsURLList


def getRToImgs(imgsURLList):
    rToImgsList = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    for i in range(len(imgsURLList)):
        rToImgs = requests.Session().get(url=imgsURLList[i], headers=headers)
        rToImgsList.append(rToImgs)
    return rToImgsList


def download(rToImgsList):
    for i in range(len(rToImgsList)):
        with open(str(i + 1) + '.jpg', 'wb') as f:
            f.write(rToImgsList[i].content)


def multithread(imgsURLList):
    rs = []
    for i in range(6):
        r = threading.Thread(target=getRToImgs, args=(imgsURLList,))
        rs.append(r)
    for rl in rs:
        rl.start()
    for rl in rs:
        rl.join()


if __name__ == '__main__':
    url = input("input url:")
    maxPage = getMaxPage(url)
    makedir('D:\\Basic_spider\\Basic_knowledge\\0 download\\' + getName(url))
    s = time.time()
    i = getImgsURL(url, maxPage)
    multithread(i)
    download(getRToImgs(i))
    e = time.time()
    print('总用时:', e - s, 's')
