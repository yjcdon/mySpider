import requests
import os
from lxml import etree
import threading
from tqdm import tqdm

# 用于:https://buondua.com/

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
# proxies = [
#     {'http': 'http://202.109.157.60:9000'},
#     {'http': 'http://121.13.252.62:41564'},
#     {'http': 'http://112.14.47.6:52024'},
#     {'http': 'http://121.13.252.58:41564'},
#     {'http': 'http://222.74.73.202:42055'},
#     {'http': 'http://117.114.149.66:55443'},
#     {'http': 'http://123.169.39.212:9999'},
#     {'http': 'http://27.42.168.46:55481'},
#     {'http': 'http://121.13.252.60:41564'},
#     {'http': 'http://61.216.185.88:60808'},
# ]
# # random只能处理列表
# proxy = random.choice(proxies)


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


def getAlbumName(url):
    responseToAlbumName = requests.Session().get(url=url, headers=headers).text
    albumName = str(etree.HTML(responseToAlbumName).xpath('/html/body/div[2]/div/div[2]/div[1]/h1/text()')[0]).replace(
        ':', '')
    return albumName


def getImgsURL(url, maxPage):
    imgURLsList = []
    everyPageImgsNum = 20

    if maxPage % 10 == 0 and (maxPage / 10) % 2 == 0:
        # pageNum是页数
        allPageNum = maxPage // 20
    else:
        allPageNum = maxPage // 20 + 1
    if maxPage <= 20:
        allPageNum = 1
        everyPageImgsNum = maxPage

    # 这个循环是处理页数的
    for nowPage in range(allPageNum):
        # 这是处理第一页
        if nowPage == 0:
            webURL = url
            r = requests.Session().get(url=webURL, headers=headers, timeout=timeOutSeconds).text
            for j in range(0, everyPageImgsNum):
                imgURLs = etree.HTML(r).xpath('//div/p/img/@src')[j]
                imgURLsList.append(imgURLs)

        if 0 < nowPage < allPageNum - 1:
            webURL = url + '?page=' + str(nowPage + 1)
            r = requests.Session().get(url=webURL, headers=headers, timeout=timeOutSeconds).text
            for j in range(0, everyPageImgsNum):
                imgURLs = etree.HTML(r).xpath('//div/p/img/@src')[j]
                imgURLsList.append(imgURLs)

        # 这里是处理最后一页的
        if nowPage == allPageNum - 1:
            webURL = url + '?page=' + str(nowPage + 1)
            r = requests.Session().get(url=webURL, headers=headers, timeout=timeOutSeconds).text
            for k in range(maxPage - 20 * (allPageNum - 1)):
                imgURLs = etree.HTML(r).xpath('//div/p/img/@src')[k]
                imgURLsList.append(imgURLs)
    return imgURLsList


def download(imgsURLList):
    # position=0可以避免出现多行进度条
    for count in tqdm(range(len(imgsURLList)), unit='imgs', desc='downloading', ncols=80, position=0, mininterval=0.1):
        try:
            responseToImgURLs = requests.Session().get(url=imgsURLList[count], headers=headers,
                                                       timeout=timeOutSeconds)
            with open(str(count + 1) + '.jpg', 'wb') as f:
                f.write(responseToImgURLs.content)
    # 只是不让报超时的错,最好别删
        except requests.exceptions.ReadTimeout:
            continue


def multiThread(imgsURLList):
    rs = []
    for i in range(10):
        r = threading.Thread(target=download, args=(imgsURLList,))
        rs.append(r)
    for rl in rs:
        rl.start()

    for rl in rs:
        rl.join()



if __name__ == '__main__':
    url = input("input url:")
    albumName = getAlbumName(url)
    maxPage = int(url.split('photos')[0].split('-')[-2])
    timeOutSeconds = maxPage // 2
    makedir('D:/Basic_spider/Basic_knowledge/0_download_image/' + albumName)
    print('start!')
    imgURLs = getImgsURL(url, maxPage)
    multiThread(imgURLs)
    print('over!')
