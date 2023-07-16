import requests
import os
from lxml import etree
import threading
from tqdm import tqdm
import random
import fake_useragent
ua = fake_useragent.UserAgent(cache_path='fake_useragent.json').random

headers = {
    'User-Agent': ua,
}


proxies = [
    {'http': 'http://202.109.157.60:9000'},
    {'http': 'http://121.13.252.62:41564'},
    {'http': 'http://112.14.47.6:52024'},
    {'http': 'http://121.13.252.58:41564'},
    {'http': 'http://222.74.73.202:42055'},
    {'http': 'http://117.114.149.66:55443'},
    {'http': 'http://123.169.39.212:9999'},
    {'http': 'http://27.42.168.46:55481'},
    {'http': 'http://121.13.252.60:41564'},
    {'http': 'http://61.216.185.88:60808'},
]
# random只能处理列表
proxy = random.choice(proxies)


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
    r = requests.Session().get(url=url, headers=headers,proxies=proxy)
    r.encoding = 'utf-8'
    r = r.text
    albumName = etree.HTML(r).xpath('//*[@id="main-wrapper"]/div[1]/h1/text()')[0]
    return albumName


def getMaxPage(url):
    resp = requests.get(url=url, headers=headers,proxies=proxy).text
    maxpage = int(str(etree.HTML(resp).xpath('//div/div[3]/a/text()')[0]).lstrip('1/'))
    if maxpage < 19:
        maxpage = maxpage + 10
    return maxpage


def getImgsUrl(maxpage, url):
    imgurllist = []
    for page in range(maxpage):
        if page == 0:
            weburl = url
            r = requests.Session().get(url=weburl, headers=headers,proxies=proxy).text
            imgurl = etree.HTML(r).xpath('//*[@id="main-wrapper"]/div[2]/p/a/img/@src')[0]
            imgurllist.append(imgurl)
        else:
            weburl = url + 'index_' + str(page + 1) + '.html'
            r = requests.Session().get(url=weburl, headers=headers,proxies=proxy).text
            imgurl = etree.HTML(r).xpath('//*[@id="main-wrapper"]/div[2]/p/a/img/@src')[0]
            imgurllist.append(imgurl)
    return imgurllist


def download(imgurllist):
    for i in tqdm(range(len(imgurllist)), unit='imgs', desc='downloading', ncols=80, position=0, mininterval=0.1):
        r = requests.Session().get(url=imgurllist[i], headers=headers,proxies=proxy)
        with open(str(i + 1) + '.jpg', 'wb') as f:
            f.write(r.content)


def multiThread(imgurllist):
    r1 = []
    for i in range(3):
        r = threading.Thread(target=download, args=(imgurllist,))
        r1.append(r)
    for rl in r1:
        rl.start()
    for rl in r1:
        rl.join()


if __name__ == '__main__':
    url = input('输入URL:')
    albumName = getAlbumName(url)
    maxpage=getMaxPage(url)
    makedir(r'D:/Basic_spider/Basic_knowledge/0_download_image/' + albumName)
    imgurllist=getImgsUrl(maxpage,url)
    multiThread(imgurllist)
