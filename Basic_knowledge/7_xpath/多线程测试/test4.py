#coding: utf-8
import re
import os
import urllib.request
import threading

headers ={
    "Referer": "https://www.doutula.com/photo/list/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
url_list = []
pic_list = []
glock = threading.Lock()
http = "http://www.doutula.com/photo/list/?page="
for i in range(1,10):
    url = http+str(i)
    url_list.append(url)
# for url in url_list:
#     print(url)


#生产者：源源不断产生图片网址并存入列表
def get_pic_url():
    while True:
        glock.acquire()
        if len(url_list) == 0:
            glock.release()
            break
        else:
            page_url = url_list.pop()
            glock.release()
            res = urllib.request.Request(page_url,headers=headers)
            res2 = urllib.request.urlopen(res).read().decode("UTF-8")
            result = re.findall(re.compile(r'<img referrerpolicy="no-referrer".*?data-original="(.*?)"',re.S),res2)
            glock.acquire()
            for rel in result:
                pic_list.append(rel)
            glock.release()

#消费者：从存储图片网址的列表中拿出网址，进行下载

def download_picture():
    while True:
        glock.acquire()
        if len(pic_list) ==0:
            glock.release()
            continue
        else:
            url = pic_list.pop()
            glock.release()
            #修改文件名
            split_list = url.split("/")
            filename = split_list.pop()
            path = os.path.join("doutu",filename)
            #下载图片，保存本地
            urllib.request.urlretrieve(url,filename=path)

def main():
    #创建两个线程作为生产者
    for x in range(2):
        product = threading.Thread(target=get_pic_url)
        product.start()
    #创建三个线程作为消费者
    for x in range(3):
        consumer = threading.Thread(target=download_picture)
        consumer.start()

if __name__ == '__main__':
    main()
