import urllib.request

def get_url():
    url = 'http://www.baidu.com'
    return url


def create_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def three_step(request):

    # 1.获取handler对象
    handler = urllib.request.HTTPHandler
    # 2.获取opener对象
    opener = urllib.request.build_opener(handler)
    # 3.调用open方法
    response = opener.open(request)

    return response


def get_content(response):
    content = response.read().decode('utf-8')
    return content


if __name__ == '__main__':
    url = get_url()
    request = create_request(url)
    response = three_step(request)
    content = get_content(response)
    print(content)
