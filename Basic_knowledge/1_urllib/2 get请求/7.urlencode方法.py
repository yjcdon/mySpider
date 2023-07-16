# 虽然在6中我们成功了,但是我们在搜索中可能会要很多个关键词,那不可能一个个字去转对吧
# 所以我们需要批量转码的函数————urlencode

# https://www.baidu.com/s?wd=周杰伦&sex=男&location=中国台湾省

# data={
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国台湾省'
# }
#
# data=urllib.parse.urlencode(data)
# print(data)
# '''结果会用&拼接'''

# 需求:获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%E7%9C%81 的网页源码

import urllib.parse
import urllib.request


# 转码
def transcoding():
    base_url = 'https://www.baidu.com/s?'
    data = {
        'wd': '周杰伦',
        'sex': '男',
        'location': '中国台湾省'
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data
    return url


# 请求对象的定制
def create_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


# 模拟浏览器请求数据
def get_content(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content


# 调用函数并打印
if __name__ == '__main__':
    url = transcoding()
    request = create_request(url)
    content = get_content(request)
    print(content)
