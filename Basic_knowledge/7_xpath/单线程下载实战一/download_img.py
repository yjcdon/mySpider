import requests
import os
import time


def receive_url():
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


def makedir(path):
    isExists = os.path.exists(os.path.join("D:\Basic_spider\Basic_knowledge\0 download", path))
    if not isExists:
        print('系统中无该文件夹,创建的地址是:', path)
        os.makedirs(os.path.join("D:\Basic_spider\Basic_knowledge\0 download", path))
        os.chdir(os.path.join("D:\Basic_spider\Basic_knowledge\0 download", path))
        return True
    else:
        print(path, '该地址的文件夹已存在')
        os.chdir(os.path.join("D:\Basic_spider\Basic_knowledge\0 download", path))
        return False


def download(img_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    for i in range(len(img_url)):
        response = requests.get(url=img_url[i], headers=headers)
        if os.path.exists(str(i + 1) + '.jpg'):
            continue
        else:
            with open(str(i + 1) + '.jpg', 'wb') as f:
                f.write(response.content)
        print('complished ' + str(i + 1))


if __name__ == '__main__':
    num = input('输入文件夹的数字:')
    makedir('D:\Basic_spider\Basic_knowledge\0 download\\lxl'  + num)
    img_url = receive_url()
    print('downloading...')
    s=time.time()
    download(img_url)
    e=time.time()
    print('consume time=',e-s,'seconds')
