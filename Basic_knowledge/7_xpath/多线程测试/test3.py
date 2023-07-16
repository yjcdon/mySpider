import re
import os
import urllib.request
import threading
from lxml import etree
import requests

num = input('输入文件夹数字:')
path="D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num
isExists = os.path.exists(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))
if not isExists:
    print('系统中无该文件夹,创建的地址是:', path)
    os.makedirs(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))
    os.chdir(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))
else:
    print(path, '该地址的文件夹已存在')
    os.chdir(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
url_list = []
pic_list = []
glock = threading.Lock()
http = "https://meixiu.in/6183.html"
r = requests.get(url=http, headers=headers,timeout=5).text
temp = etree.HTML(r).xpath('//div/p/img/@src')
print('开始获取图片url...')
for i in range(len(temp)):
    url_list.append(temp[i])
print('获取完毕')

def producer():
    while True:
        glock.acquire()
        if len(url_list) == 0:
            glock.release()
            break
        else:
            page_url = url_list.pop()
            glock.acquire()
            for result in url_list:
                pic_list.append(result)
            glock.release()


def comsumer():
    i = 1
    while True:
        glock.acquire()
        if len(pic_list) == 0:
            glock.release()
            continue
        else:
            url = pic_list.pop()
            glock.release()
            urllib.request.urlretrieve(url, filename=str(i) + '.jpg')
            print('ok ',i)




def main():
    # 创建两个线程作为生产者
    for x in range(10):
        product = threading.Thread(target=producer)
        product.start()
    # 创建三个线程作为消费者
    for x in range(10):
        consumer = threading.Thread(target=comsumer)
        consumer.start()


if __name__ == '__main__':
    main()
