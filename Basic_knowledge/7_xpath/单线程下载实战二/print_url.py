import requests
from lxml import etree

'''
https://meixiu.in/6500.html
'''


def get_baseurl():
    baseurl = input('输入url:')
    return baseurl


def get_otherurl():
    otherurl = ''
    return otherurl


def get_imgurl(baseurl, otherurl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    end = int(input('共有多少张图:'))

    for page in range(0, end + 1):
        response = requests.get(url=baseurl, headers=headers).text
        xpathurl = etree.HTML(response).xpath('//div/p/img/@src')[page]
        img_url = xpathurl
        print(img_url)


if __name__ == '__main__':
    baseurl = get_baseurl()
    otherurl = get_otherurl()
    get_imgurl(baseurl, otherurl)
    print('over')
