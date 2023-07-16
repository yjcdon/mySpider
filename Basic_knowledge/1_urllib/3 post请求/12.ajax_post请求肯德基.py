# 肯德基餐厅信息url:http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname

# 需求:把北京前十页保存到本地

# 第一页
# url:http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

# 第二页
# url:http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

# 貌似只有pageIndex不同

import urllib.request
import urllib.parse


def get_url():
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    return url


def create_request(url, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
    }

    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10',
    }
    data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url=url, data=data, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(page, content):
    with open('KFC in Beijing' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('输入起始页码:'))
    end_page = int(input('输入结束页码:'))
    for page in range(start_page, end_page + 1):
        url = get_url()
        request = create_request(url, page)
        content = get_content(request)
        download(page, content)
        # 如果打印没信息,你试着把data中的单引号中的空格删去
