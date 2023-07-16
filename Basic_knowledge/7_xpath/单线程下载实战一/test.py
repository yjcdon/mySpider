import requests
from lxml import etree
import os
import time
from concurrent.futures import ThreadPoolExecutor

url = input('输入url:')
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
resp=requests.Session().get(url=url,headers=headers).text

maxpage =int(str(etree.HTML(resp).xpath('//div/div[3]/a/text()')[0]).lstrip('1/'))
if maxpage<19:
    maxpage=maxpage+10
url_list = []
r_list=[]

def get_imgurl():
    for page in range(maxpage):
        if page == 0:
            weburl = url
        else:
            weburl = url + 'index_' + str(page + 1) + '.html'
        response = requests.Session().get(url=weburl, headers=headers).text

        temp = etree.HTML(response).xpath('//div/p/a/img/@src')[0]
        url_list.append(temp)
        r = requests.Session().get(url=url_list[page], headers=headers)
        r_list.append(r)
    return r_list


def download(r_list):
    for page in range(maxpage):
        with open(str(page + 1) + '.jpg', 'wb') as f:
            f.write(r_list[page].content)
        print('complised ' + str(page + 1))


def makedir(path):
    isExists = os.path.exists(os.path.join("D:\Basic spider\Basic knowledge\\0 download\lxl", path))
    if not isExists:
        print('系统中无该文件夹,创建的地址是:', path)
        os.makedirs(os.path.join("D:\Basic spider\Basic knowledge\\0 download\lxl", path))
        os.chdir(os.path.join("D:\Basic spider\Basic knowledge\\0 download\lxl", path))
        return True
    else:
        print(path, '该地址的文件夹已存在')
        os.chdir(os.path.join("D:\Basic spider\Basic knowledge\\0 download\lxl", path))
        return False


if __name__ == '__main__':
    num = input('输入文件夹的数字:')
    makedir('D:\Basic spider\Basic knowledge\\0 download\lxl\\' + num)
    s=time.time()
    download(get_imgurl())
    e=time.time()
    print('consume time=',e-s,'seconds')

#你把s换到download上面,你会发现下载是真滴快;主要的时间花在解析网页中