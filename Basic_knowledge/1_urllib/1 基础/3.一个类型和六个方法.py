import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

# print(type(response))  # HTTPResponse,很重要,你得记住

# 1.read对源码是一个字节一个字节去读,read()中放数字,那就会返回几个字节
# content = response.read(5)
# print(content)

# 2.readline只读一行
# content = response.readline()
# print(content)

# 3.readlines可以一行一行读取,知道末尾
# content = response.readlines()
# print(content)

# 4.getcode,返回状态码,通过状态码来判断代码有无问题
# print(response.getcode())
# 像200就没问题,404就不行

# 5.geturl,返回URL地址
# print(response .geturl())

# 6.getheaders,获取状态信息
print(response.getheaders())
