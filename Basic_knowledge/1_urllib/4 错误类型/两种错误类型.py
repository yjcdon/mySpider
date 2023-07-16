#URLError  HTTPError
#增加代码的健壮性:使用try-except

import urllib.request
import urllib.error


# HTTPError
# url='https://blog.csdn.net/yuan2019035055/article/details/125345488'
# 我在末尾不小心加了个1
# url='https://blog.csdn.net/yuan2019035055/article/details/1253454881'


#URLError
url='https://www.lyjnb666.com'


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
    }

try:
    request=urllib.request.Request(url=url,headers=headers)

    response= urllib.request.urlopen(request)

    content=response.read().decode('utf-8')

    print(content)

except urllib.error.HTTPError:
    print('网址有误')

except urllib.error.URLError:
    print('该网址不存在')