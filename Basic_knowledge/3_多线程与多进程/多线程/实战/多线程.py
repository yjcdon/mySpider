import requests
import threading
import time
from lxml import etree
import os

url = input('输入url:')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
resp=requests.get(url=url,headers=headers).text
maxpage = int(str(etree.HTML(resp).xpath('//div/div[3]/a/text()')[0]).lstrip('1/'))
if maxpage < 19:
    maxpage = maxpage + 10


def create_thread(urllist):
    th = []
    th2 = []
    for x in range(6):
        t = threading.Thread(target=get_imgurl)
        t2 = threading.Thread(target=get_imgresponse, args=(urllist,))
        th.append(t)
        th2.append(t2)
        t.start()
        t2.start()


def get_imgurl():
    urllist = []
    for page in range(maxpage):
        if page == 0:
            weburl = url
        else:
            weburl = url + 'index_' + str(page + 1) + '.html'
        s=requests.Session()
        re = s.get(url=weburl, headers=headers).text
        xpathurl = etree.HTML(re).xpath('//div/p/a/img/@src')[0]
        urllist.append(xpathurl)
    return urllist


def get_imgresponse(urllist):
    print('获取图片响应完毕,开始下载')
    s = time.time()
    for page in range(maxpage):
        res = requests.Session().get(url=urllist[page], headers=headers)
        with open(str(page + 1) + '.jpg', 'wb') as f:
            f.write(res.content)
    e = time.time()
    print('time = ', e - s, '秒')



def makedir(path, num):
    isExists = os.path.exists(os.path.join(r"D:\Basic_spider\Basic_knowledge\0 download\lxl\\" + num, path))
    if not isExists:
        print('系统中无该文件夹,创建的地址是:', path)
        os.makedirs(os.path.join(r"D:\Basic_spider\Basic_knowledge\0 download\lxl\\" + num, path))
        os.chdir(os.path.join(r"D:\Basic_spider\Basic_knowledge\0 download\lxl\\" + num, path))
        return True
    else:
        print(path, '该地址的文件夹已存在')
        os.chdir(os.path.join(r"D:\Basic_spider\Basic_knowledge\0 download\lxl\\" + num, path))
        return False


if __name__ == '__main__':
    num = input('输入文件夹的数字:')
    makedir(r"D:\Basic_spider\Basic_knowledge\0 download\lxl\\" + num, num)


    urllist = get_imgurl()
    create_thread(urllist)

