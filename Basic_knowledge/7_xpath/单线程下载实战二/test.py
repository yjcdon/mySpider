import requests
from lxml import etree
import os
import time
from concurrent.futures import ProcessPoolExecutor

url = input('输入url:')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
url_list = []
r_list = []
maxpage = int(input('输入最大页数:'))
response = requests.Session().get(url=url, headers=headers, timeout=5).text
temp = etree.HTML(response).xpath('//div/p/img/@src')
url_list.append(temp)
print('响应完毕')


def get_imgurl():
    for page in range(maxpage):
        r = requests.Session().get(url=temp[page], headers=headers)  # 这里是最慢的
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
    with ProcessPoolExecutor(6) as exe:
        r_list = get_imgurl()
        exe.submit(get_imgurl, r_list)
        download(r_list)
        exe.shutdown(wait=True)
    e = time.time()
    print('consume time=', e - s, 'seconds')
