import requests
import urllib.request
import urllib.parse
import os

'''
第一页:https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20
第二页:https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=20&limit=20
第三页:https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=40&limit=20

我们发现前面都一样,但是start=的数字会变化,且有规律
page:   1   2   3   4
start:  0   20  40  60
显然,start=(page-1)*20

所以我们要base_url+变化的start,我们用函数和循环来实现比较容易
'''


# 获取url
def get_url(page):
    baseurl = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)

    # 我不懂怎么把字典变成字符串,强制转换不行
    url = baseurl + data
    return url


# 发起请求并获取源码
def get_response(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    response = requests.get(url=url, headers=headers)
    return response


# 解码数据
def get_content(response):
    content = response.text
    return content


def download(page, content):
    with open('douban' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


def makedir(path):
    # os.path.exists(name)判断是否存在路径
    # os.path.join(path, name)连接目录与文件名
    isExists = os.path.exists(os.path.join("/Basic knowledge/0 download", path))
    if not isExists:
        print('系统中无此文件夹,创建的地址是:', path)
        # 创建文件夹
        os.makedirs(os.path.join("/Basic knowledge/0 download", path))
        # 切换到创建的文件夹
        os.chdir(os.path.join("/Basic knowledge/0 download", path))
        return True
    else:
        print('系统中已有地址为:',path, '的文件夹')
        os.chdir(os.path.join("/Basic knowledge/0 download", path))
        return False


if __name__ == '__main__':
    start_page = int(input('输入起始页码:'))
    end_page = int(input('输入结束页码:'))
    makedir(path='/Basic knowledge/0 download')
    for page in range(start_page, end_page + 1):
        url = get_url(page)
        response = get_response(url)
        content = get_content(response)
        download(page, content)
    print('over')
