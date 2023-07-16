from tqdm import tqdm
import time
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

img_url = ['https://www.meitun168.com/pic/24/xingyan/128/24mnorg_12308.jpg',
           'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_22309.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_32310.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_42311.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_52312.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_62313.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_72314.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_82315.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_92316.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_102317.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_112318.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_122319.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_132320.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_142321.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_152322.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_162323.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_172324.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_182325.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_192326.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_202327.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_212328.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_222329.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_232330.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_242331.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_252332.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_262333.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_272334.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_282335.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_292336.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_302337.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_312338.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_322339.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_332340.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_342341.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_352342.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_362343.jpg',
           # 'https://www.meitun168.com/pic/24/xingyan/128/24mnorg_372344.jpg',
           ]

for num in range(len(img_url)):
    response = requests.get(url=img_url[num], headers=headers, stream=True)
    head = requests.head(url=img_url[num], headers=headers)
    file_size = int(head.headers.get('Content-Length'))
    bar = tqdm(total=file_size, unit_scale=True, colour='blue', unit='B',
               desc='正在下载第 ' + str(num + 1) + ' 张图片')
    chunk_size = 1024
    file_name = '韩雨馨' + str(num + 1) + '.jpg'
    with open(file_name, 'wb') as f:
        # 写入分块文件
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)
            # 更新进度条
            bar.update(chunk_size)
    bar.close()
