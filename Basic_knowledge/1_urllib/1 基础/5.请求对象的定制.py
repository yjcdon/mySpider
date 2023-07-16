import urllib.request

url = 'https://www.baidu.com'

'''由下面可知,ua是字典数据'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
}

'''因为urlopen无法储存字典数据,所以无法传入headers
但可以储存request对象
所以此时需要请求对象的定制'''

'''对陌生的函数参数,你应该Ctrl+左键去看,它的参数传递是按顺序的;所以这里是关键字传参'''
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
'''若没有上面的伪装,那么返回的数据是很少的
因为使用了一种ua(用户代理),是一种反爬手段'''
