import requests
import json
#json用不用,看content_type有无json

def get_url():
    url = 'https://fanyi.baidu.com/sug'#这个URL就很离谱,通用的
    return url


# 请求数据并获得源码
def get_response(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',

    }
    kw=input('input a word:')
    data = {
        'kw':kw
    }

    # url:请求网址,data:请求参数,kwargs:字典
    response = requests.post(url=url, data=data, headers=headers)
    return response


# 解码数据
def get_content(response):
    # 这个是将数据解码再变成我们能看得懂的
    # content = response.text
    # obj = json.loads(content)

    obj = response.json()
    return obj


if __name__ == '__main__':
    url = get_url()
    response = get_response(url)
    obj = get_content(response)
    print(obj)

'''1.不需要编解码
   2.不需要请求对象的定制'''
