import urllib.request

def get_url():
    url = 'https://cn.bing.com/search?q=IP'
    return url

def create_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_IP():#proxy,proxies,代理
    #你得写成这样,字典,key是'http',value是'IP:端口'
    proxies={
        'http':'218.252.244.104:80'
    }

    return proxies

def three_step(request,proxies):

    # 1.获取handler对象(代理这边变一个)
    handler = urllib.request.ProxyHandler(proxies=proxies)
    # 2.获取opener对象
    opener = urllib.request.build_opener(handler)
    # 3.调用open方法
    response = opener.open(request)

    return response

def get_content(response):
    content = response.read().decode('utf-8')
    return content

def download(content):
    with open('代理.html','w',encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    url = get_url()
    request = create_request(url)
    proxies=get_IP()
    response = three_step(request,proxies)
    content = get_content(response)
    download(content)