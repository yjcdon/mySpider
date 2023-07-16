from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import requests
import os
from lxml import etree
import time


# def get_img(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
#     }
#     response = requests.get(url=url, headers=headers).text
#
#     img_url = etree.HTML(response).xpath('//div/p/img/@src')
#
#     return img_url



def get_img():
    img_url = ['https://www.meitun168.com/pic/24/xingyan/128/24mnorg_12308.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_22309.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_32310.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_42311.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_52312.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_62313.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_72314.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_82315.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_92316.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_102317.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_112318.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_122319.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_132320.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_142321.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_152322.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_162323.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_172324.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_182325.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_192326.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_202327.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_212328.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_222329.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_232330.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_242331.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_252332.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_262333.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_272334.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_282335.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_292336.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_302337.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_312338.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_322339.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_332340.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_342341.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_352342.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_362343.jpg',
'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_372344.jpg',


]

    return img_url


def download(img_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    for i in range(len(img_url)):
        response = requests.Session().get(url=img_url[i], headers=headers)

        with open(str(i + 1) + '.jpg', 'wb') as f:
            f.write(response.content)
        print('complished ' + str(i + 1))


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
    img_url = get_img()
    start = time.time()
    with ThreadPoolExecutor(6) as executor:
        print('downloading...')
        result = executor.submit(download, img_url)
        executor.shutdown(wait=True)
    end = time.time()
    print('consume time=', end - start, 'secodes')
    print('over')
