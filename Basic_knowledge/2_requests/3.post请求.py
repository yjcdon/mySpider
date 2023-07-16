import requests
import json
#json用不用,看content_type有无json

def get_url():
    url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    return url


# 请求数据并获得源码
def get_response(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie': 'BIDUPSID=F8467C8FAF335247AC3744226B6AA437; PSTM=1657027970; APPGUIDE_10_0_2=1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; BAIDUID_BFESS=CC173ADE8E215811605C3415A100ACD8:FG=1; ZFY=wyIwF60Hjd2:AC5CaSCZHX:BWfCeqfLfIANfuL1kievXI:C; BAIDU_WISE_UID=wapp_1657730725913_553; newlogin=1; BDUSS=VSVWpkWVdXfjFSMEpLcUZta04zVGE3Wjg0Uzlzb0dJalIzc05FOTJSc1ZFZ3BqRVFBQUFBJCQAAAAAAAAAAAEAAACJw5pN09C92rLZtcTFtsWjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWF4mIVheJiU2; BDUSS_BFESS=VSVWpkWVdXfjFSMEpLcUZta04zVGE3Wjg0Uzlzb0dJalIzc05FOTJSc1ZFZ3BqRVFBQUFBJCQAAAAAAAAAAAEAAACJw5pN09C92rLZtcTFtsWjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWF4mIVheJiU2; RT="z=1&dm=baidu.com&si=l4srk5m918&ss=l6gi6zr0&sl=2&tt=352&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2x9&ul=3mr&hd=3ne"; BA_HECTOR=ah012h2galak808l84akqqod1heqd9q17; BAIDUID=F8467C8FAF335247537F73C4953994B0:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1657370499,1659771544; ab_sr=1.0.1_ZTBkOGQzNzdjOTdjMjljZWFkNTIyYzdiZmU1ODVlNzFiZjZiN2NjMmVlZDgwOTUxNmRjNWJjMWNhMzI1NDg2ZTgzZTRkZTMxZjJkZTBkMGQ4ZTIyNTY3MWY2NDI2ZDhkMTQ4MjBkNjExMGUzMjk5MmNhMTZlNWQ1NjMxN2JlNThjNzlhYWQxYTRhZTgyOWQyZDU4ZGE2M2MxMzVjMjFmMzhiZjgxYjQwNzBkOGYyNGZkZDEwNWE2YmY0ZmI1MGU2; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1659773912',

    }
    data = {
        'from': 'en',
        'to': 'zh',
        'query': 'request',
        'simple_means_flag': '3',
        'sign': '620615.891766',
        'token': '17a7bae4d13fc7500cea06b84db9194d',
        'domain': 'common',
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
