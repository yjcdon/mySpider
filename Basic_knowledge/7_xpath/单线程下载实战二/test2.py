import requests
import time
url = input('输入url:')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
s = time.time()
r=requests.Session().get(url=url,headers=headers).text
e = time.time()
print('consume time=', e - s, 'seconds')

