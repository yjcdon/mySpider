import requests
from lxml import etree
import os
import time

url = input('输入url:')
headers = {
    'cookie': '_gid=GA1.2.751392223.1660561858; theme_mode=dark-theme; history_search=%5B%22%5Cu5957%5Cu56fe%22%2C%22%5Cu8bed%5Cu753b%5Cu754c%22%2C%22%5Cu3051%5Cu3093%5Cu3051%5Cu3093%22%2C%22Lovepop%22%2C%22%5Cu8ff7%5Cu4e4b%5Cu5446%5Cu68a8%22%2C%22XiuRen%5Cu79c0%5Cu4eba%5Cu7f51%22%2C%22%5Cu514b%5Cu62c9%5Cu5973%5Cu795e%22%2C%22%5Cu798f%5Cu5229%22%2C%22%5Cu79c0%5Cu4eba%22%5D; _ga_Z890VSYJMK=GS1.1.1660564344.13.1.1660567408.0; _ga=GA1.1.498096635.1660140338',
    'referer': 'https://meixiu.in/?s=%E8%BF%B7%E4%B9%8B%E5%91%86%E6%A2%A8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

url_list = []
r_list = []
maxpage = int(input('输入最大页数:'))
response = requests.Session().get(url=url, headers=headers,timeout=5).text
temp = etree.HTML(response).xpath('//div/p/img/@src')
url_list.append(temp)
print('响应完毕')


def get_imgurl():
    for page in range(maxpage):
        r = requests.Session().get(url=temp[page], headers=headers)#这里是最慢的
        r_list.append(r)
    return r_list


def download(r_list):
    for page in range(maxpage):
        if os.path.exists(str(page + 1) + '.jpg'):
            continue
        else:
            with open(str(page + 1) + '.jpg', 'wb') as f:
                f.write(r_list[page].content)
        print('complised ' + str(page + 1))


def makedir(path, num):
    isExists = os.path.exists(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))
    if not isExists:
        print('系统中无该文件夹,创建的地址是:', path)
        os.makedirs(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))
        os.chdir(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))
        return True
    else:
        print(path, '该地址的文件夹已存在')
        os.chdir(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))
        return False


if __name__ == '__main__':
    num = input('输入文件夹的数字:')
    makedir('D:\Basic spider\Basic knowledge\\0 download\呆梨\\' + num, num)
    print('downloading...')
    s = time.time()
    download(get_imgurl())
    e = time.time()
    print('consume time=', e - s, 'seconds')
