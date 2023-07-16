# 我的微博,QQ空间好像反爬手段比微博牛逼一些
# 你得先登录才行

import urllib.request
import urllib.parse


def get_url():
    url = 'https://weibo.cn/6217746534/info'
    return url


#不成功可能是headers信息不够
def create_request(url):
    headers = {
        #冒号开头和encoding没用,尤其是encoding必须注释掉
        # ':authority':'weibo.cn',
        # ':method': 'GET',
        # ':path': ' /6217746534/info',
        # ':scheme': ' https',
        'accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'accept-encoding': ' gzip, deflate, br',
        'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': ' max-age=0',
        'cookie': ' _T_WM=09f87e46c597bf794b0372932647a05a; ALF=1659693498; MLOGIN=1; SUB=_2A25PwS1RDeRhGeBM6lUW9CjJyDiIHXVtTbMZrDV6PUJbktANLRLMkW1NRR1Dv1Yd3ZMef3Go40Tsojk1YGWYHen6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF8KO4uHOTSKOQnCnhEX8ew5NHD95Qceo2NS0BcSKeXWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSozpS0MXSo-0S5tt; SSOLoginState=1657101569; M_WEIBOCN_PARAMS=oid%3D4787862929409180%26lfid%3D4787862929409180%26luicode%3D20000174',
        'referer': 'https://weibo.cn/',
        'sec-ch-ua': ' " Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': ' ?0',
        'sec-ch-ua-platform': ' "Windows"',
        'sec-fetch-dest': ' document',
        'sec-fetch-mode': ' navigate',
        'sec-fetch-site': ' same-origin',
        'sec-fetch-user': ' ?1',
        'upgrade-insecure-requests': ' 1',
        'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


# 将数据解码
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(content):
    # open函数默认的编码是gbk,如果我们要保存中文,要改成UTF-8
    with open('weibo.html', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    url = get_url()
    request = create_request(url)
    content = get_content(request)
    download(content)
#你会发现你点下载的html,还是要登录        是因为没把cookie和referer放到headers中