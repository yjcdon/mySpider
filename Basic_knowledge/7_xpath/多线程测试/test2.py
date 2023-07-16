import requests
from lxml import etree
from concurrent.futures import ProcessPoolExecutor
import socket


def download(img_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    NETWORK_STATUS = True
    for i in range(len(img_url)):
        # if os.path.exists(str(i + 1) + '.jpg'):
        #     continue
        # else:
        try:
            req = requests.get(img_url[i], headers=headers, timeout=(3, 7))
            if req.status_code == 200:
                req = req
        except requests.exceptions.Timeout:
            NETWORK_STATUS = False  # 请求超时改变状态
        if NETWORK_STATUS == False:
            # '''请求超时'''
            for i in range(len(img_url)):
                print('请求超时，第%s次重复请求' % i+1)
                req = requests.get(img_url[i], headers=headers, timeout=(3, 7))
                if req.status_code == 200:
                    req = req
                else :
                    continue
            # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # s.settimeout(2)
            with open(str(i + 1) + '.jpg', 'wb') as f:
                f.write(req.content)
            print('complished ' + str(i + 1))
    print('下载完成')


if __name__ == '__main__':
    url = input('输入url:')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    num = int(input('有多少张图片:'))
    response = requests.Session().get(url=url, headers=headers).text
    img_url = etree.HTML(response).xpath('//div/p/img/@src')
    with ProcessPoolExecutor(max_workers=20) as ex:
        ex.submit(download, img_url)
        ex.shutdown(wait=True)
