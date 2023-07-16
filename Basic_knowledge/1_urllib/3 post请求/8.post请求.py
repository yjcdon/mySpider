# 向指定的资源提交要被处理的数据

# 从百度翻译中入手

'''难点在于找到谁是接口(即谁在翻译)'''

# 需求:获取 https://fanyi.baidu.com/v2transapi?from=en&to=zh 的源码

import urllib.request
import urllib.parse
import json


def get_url():
    url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'  # 你找到的接口url是详细翻译,目前只有这种
    # post请求的参数在哪?这是与get请求不同的点
    return url


# 请求对象的定制(规范点)
def create_request(url):
    headers = {  # 加cookie是因为反爬
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'Cookie': 'BIDUPSID=F8467C8FAF335247AC3744226B6AA437; PSTM=1657027970; BAIDUID=F8467C8FAF335247537F73C4953994B0:FG=1; BAIDUID_BFESS=F8467C8FAF335247AC3744226B6AA437:FG=1; BA_HECTOR=a0a185al25ah852k001hc8fc415; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZFY=MGlTO0sMW1WEKuuZOLNwzilEuqDxC0WO4OktGpQbrcI:C; APPGUIDE_10_0_2=1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1657027973,1657028205,1657029051; ab_sr=1.0.1_MWUzNGM4ZTU1Mjg1ZDEzNTU1N2Q3NmYzMzNmNmZhMTYwYTBlYmFiNjdkN2RmNDE2ZmU1NmYzMTU3MTI5NjM5ZjdhZjljN2ZkOGYyZDk1M2MzYzIwMDg0ZjVkMGZhYzQ2NDBmMDM4OWQ0Yjg0NDVjNDEwYmMzMTVkMmI0ZTY1NzMyYjM5YjJlYzg2MjFjMmU3OTk0MjFjZTRlNTFmZGM3ZQ==; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1657037260'
    }

    data = {
        'query': 'spider',
        'from': 'en',
        'to': 'zh',
        'query': 'spider',
        'simple_means_flag': '3',
        'sign': '63766.268839',
        'token': '64e5cb5f4d0f927cb2c81a4c811ef247',
        'domain': 'common'
    }

    # post请求的参数,必须要编码encode
    data = urllib.parse.urlencode(data).encode('utf-8')

    # post请求的参数,不会拼接到url后面,而是放在请求对象的定制的参数中,这就是和get请求不同的点
    request = urllib.request.Request(url=url, data=data, headers=headers)
    return request


# 模拟浏览器,向服务器请求数据
def get_content(request):
    response = urllib.request.urlopen(request)

    # 储存数据并解码
    content = response.read().decode('utf-8')
    return content


def get_data(content):
    # print(content)  # 现在content是str类型,打印出来看不懂,发现content的内容是json
    # 那么就要把字符串->json对象,记得导入json模块

    obj = json.loads(content)
    return obj


if __name__ == '__main__':
    url = get_url()
    request = create_request(url)
    content = get_content(request)
    obj = get_data(content)
    print(obj)
