import requests
import time
from concurrent.futures import ThreadPoolExecutor
import threading


def get_codelen(weburl):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    response = requests.get(url=weburl, headers=headers).text
    print(weburl, len(response))


if __name__ == '__main__':
    url = 'https://www.cnblogs.com/'
    lock = threading.Lock()
    start = time.time()
    for i in range(0, 30):
        if i == 0:
            weburl = url
        else:
            weburl = url + '#p' + str(i + 1)

        ex = ThreadPoolExecutor(2)
        ex.submit(get_codelen, weburl)

    end = time.time()
    print('time=', end - start, 'seconds')
#十倍于进程池