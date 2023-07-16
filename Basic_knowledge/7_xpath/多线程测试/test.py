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
    img_url = ['https://file.ertuba.com/2022/0621/bb1fd7e244012dbaf18cd49bcb085005.jpg',
'https://file.ertuba.com/2022/0621/7ddcda2070cecafde4a330432387e738.jpg',
'https://file.ertuba.com/2022/0621/fe0b8ae36535f7ce0478c949602e2ef1.jpg',
'https://file.ertuba.com/2022/0621/70d6a6746c99763df502fd83c6b9d1c5.jpg',
'https://file.ertuba.com/2022/0621/329eaf5fc5cf933999913ef80095efb7.jpg',
'https://file.ertuba.com/2022/0621/35bae61738b6e5a217ac0d9fe1c9663d.jpg',
'https://file.ertuba.com/2022/0621/62686f9299ae0d4ba5f17f4bffc72ef8.jpg',
'https://file.ertuba.com/2022/0621/99e66a7152fea3cceb9f45a36617850e.jpg',
'https://file.ertuba.com/2022/0621/0754d4a36ec6235f8f062d7deb6955a9.jpg',
'https://file.ertuba.com/2022/0621/637ee3db7b052a4ea37d556ad6247686.jpg',
'https://file.ertuba.com/2022/0621/ef1de0b2b46d7ef1aa41ea6bf3218bd5.jpg',
'https://file.ertuba.com/2022/0621/bd130dca0db26aff0dc68d32247928d9.jpg',
'https://file.ertuba.com/2022/0621/601cf1e79036ab9c7add112f23fc7c40.jpg',
'https://file.ertuba.com/2022/0621/3525cb02be25c7e85bf0186fc99e82e4.jpg',
'https://file.ertuba.com/2022/0621/2f6ecb0f096e4b52d11d66801329da36.jpg',
'https://file.ertuba.com/2022/0621/33dfb7fcaea2a55010844ee844b8db30.jpg',
'https://file.ertuba.com/2022/0621/28b23d73a99cff665954df925932fd28.jpg',
'https://file.ertuba.com/2022/0621/366914b0922da52d0ec2551fa50a2ef6.jpg',
'https://file.ertuba.com/2022/0621/b22be1300b39db13a3165b6cf5b92c34.jpg',
'https://file.ertuba.com/2022/0621/4b5a80710237736c566278a9e2c73986.jpg',
'https://file.ertuba.com/2022/0621/b9a1dbd6a44a2369494de606547efc48.jpg',
'https://file.ertuba.com/2022/0621/fb0007fb096696f23258ae6544efef25.jpg',
'https://file.ertuba.com/2022/0621/fde9d6b4e4eaf737a7c2f9864e62379d.jpg',
'https://file.ertuba.com/2022/0621/6b50509a422f97742234a62dc560fbee.jpg',
'https://file.ertuba.com/2022/0621/9265e653e517d19dac95250162daa1e0.jpg',
'https://file.ertuba.com/2022/0621/14725fe6e86c348c87d159094703f12e.jpg',
'https://file.ertuba.com/2022/0621/ad1b991d07f5cfffb298393b9d372cc0.jpg',
'https://file.ertuba.com/2022/0621/d81b6f5b5ccc2da676db46364d148013.jpg',
'https://file.ertuba.com/2022/0621/0a76155180a5f54f2300728e8594d60a.jpg',
'https://file.ertuba.com/2022/0621/4f661e658b821a217be7a8b8b7c5d6fd.jpg',
'https://file.ertuba.com/2022/0621/b41e9309d22a2a1dd2125b27ee484968.jpg',
'https://file.ertuba.com/2022/0621/a01f982227f2379068f28443498f8342.jpg',
'https://file.ertuba.com/2022/0621/ce5940bb46498ecc6fb5fd3b8904e975.jpg',
'https://file.ertuba.com/2022/0621/fac5b3407ad7579f1ea6fd12c836f8bc.jpg',
'https://file.ertuba.com/2022/0621/1b8fbe455f4533f2f0597bf50e604181.jpg',
'https://file.ertuba.com/2022/0621/2069aa03fe85eea4f8f9c693624447a3.jpg',
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
    makedir('D:\Basic spider\Basic knowledge\\0 download\lxl\\'  + num)
    img_url = get_img()
    start = time.time()
    with ProcessPoolExecutor(6) as executor:
        print('downloading...')
        result = executor.submit(download, img_url)
        executor.shutdown(wait=True)
    end = time.time()
    print('consume time=', end - start, 'secodes')
