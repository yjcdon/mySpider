import requests
import os
import time
from lxml import etree
import threading

url = input('输入url:')
weburl = url
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
r = requests.Session().get(url=url, headers=headers).text
maxpage = int(str(etree.HTML(r).xpath('//div/div[3]/a/text()')[0]).lstrip('1/'))
if maxpage < 19:
    maxpage = maxpage + 10
img_list = []
r_list = []


def get_imgurl():
    for page in range(maxpage):
        if page == 0:
            weburl = url
        else:
            weburl = url + 'index_' + str(page + 1) + '.html'
        r = requests.Session().get(url=weburl, headers=headers).text
        imgurl = etree.HTML(r).xpath('//div/p/a/img/@src')[0]
        img_list.append(imgurl)
    return img_list


# 最费时间的,对图片的url发起请求
def get_img_response(img_list):
    s = time.time()


    for i in range(maxpage):
        r2 = requests.Session().get(url=img_list[i], headers=headers)
        r_list.append(r2)
    e = time.time()
    print('请求花费time =', e - s, 'seconds')
    return r_list


def download(r_list):


    for page in range(maxpage):
        if os.path.isfile(str(page + 1) + '.jpg'):
            continue
        else:
            with open(str(page + 1) + '.jpg', 'wb') as f:
                f.write(r_list[page].content)
    print('\n成功下载', page + 1, '张图片')


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


def multithread(r_list, img_list):
    img = []
    resp = []
    dls = []
    for i in range(6):
        i = threading.Thread(target=get_imgurl)
        img.append(i)
        r = threading.Thread(target=get_img_response, args=(img_list,))
        resp.append(r)
        d = threading.Thread(target=download, args=(r_list,))
        dls.append(d)

    for im in img:
        im.start()
    for res in resp:
        res.start()
    for dl in dls:
        dl.start()

    for im in img:
        im.join()
    for res in resp:
        res.join()
    for dll in dls:
        dll.join()


if __name__ == '__main__':
    num = input('输入文件夹的数字:')
    makedir(r"D:\Basic_spider\Basic_knowledge\0 download\lxl\\" + num, num)


    multithread(get_img_response(get_imgurl()), get_imgurl())

