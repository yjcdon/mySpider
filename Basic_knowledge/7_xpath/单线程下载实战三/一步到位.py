import requests
from lxml import etree
import os
import time

url = input('输入url:')
baseurl='https://www.meitun168.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
r = requests.Session().get(url=url, headers=headers).text

maxpage = 37

picurl_list = []
r_list = []

def get_src():
    for i in range(maxpage):
        src = etree.HTML(r).xpath('//div/p/img/@data-src')
        picurl=baseurl+src[i]
        print(picurl)


if __name__ == '__main__':
    get_src()