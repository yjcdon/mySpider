import requests
from lxml import etree


def get_baseurl():
    baseurl = input('输入url:')
    return baseurl


def get_imgurl(baseurl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    end = int(input('最大页数:'))
    for page in range(0, end):
        if page == 0:
            Webpage = baseurl
        else:
            Webpage = baseurl + 'index_' + str(page + 1) + '.html'
        response = requests.get(url=Webpage, headers=headers).text
        img_url = etree.HTML(response).xpath('//div/div[2]/p/a/img/@src')[0]
        print(img_url)


if __name__ == '__main__':
    baseurl = get_baseurl()
    get_imgurl(baseurl)
