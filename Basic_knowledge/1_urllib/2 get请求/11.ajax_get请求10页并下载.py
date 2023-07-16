# 1.请求对象的定制
# 2.模拟浏览器请求数据
# 3.下载到本地

'''请求多页数据,我们找到接口,并寻找url的规律
第一页:https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
第二页:https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20
第三页:https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20
第四页:https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=60&limit=20

我们发现前面都一样,但是start=的数字会变化,且有规律
page:   1   2   3   4
start:  0   20  40  60
显然,start=(page-1)*20

所以我们要base_url+变化的start组成请求对象的定制,我们用函数来实现比较容易
比较正式的代码
'''
import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
    }

    # get请求是这样
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }

    # get请求输入数据后,别忘了编码
    data = urllib.parse.urlencode(data)

    url = base_url + data
    request = urllib.request.Request(url=url, headers=headers)
    return request


# 2.模拟浏览器请求数据
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


# 3.下载到本地
def download(page, content):
    with open('douban' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


# 1.请求对象的定制
if __name__ == '__main__':
    start_page = int(input('输入起始页码:'))
    end_page = int(input('输入结束页码:'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)  # 返回值你要储存
        content = get_content(request)
        download(page, content)
