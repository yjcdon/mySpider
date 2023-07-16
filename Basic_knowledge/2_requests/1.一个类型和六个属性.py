import requests

url = 'http://www.baidu.com'

response = requests.get(url)
print(response)

# 一个类型
# print(type(response)) 类型是:Response

# 六个属性
# 1.改变响应的编码格式
# response.encoding='utf-8'

# 2.获取网页源码
# print(response.text),此时response的编码是Unicode

# 3.获取网页url
# print(response.url)

# 4.获取响应的字节类型
# print(response.content),类型是bytes

# 5.获取状态码
# print(response.status_code)

# 6.获取响应头
# print(response.headers)
