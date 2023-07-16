import requests


# 获取url
def get_baseurl():
    baseurl = 'https://www.baidu.com/s?'
    return baseurl


# 发起请求  request.get()
def get_response(baseurl):
    # 如果以后再用发现返回的数据很少,那就在请求头中多拿点东西放到headers中
    # cookie在不同网站中可能会不一样
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Cookie': 'BIDUPSID=F8467C8FAF335247AC3744226B6AA437; PSTM=1657027970; BAIDUID=F8467C8FAF335247537F73C4953994B0:FG=1; APPGUIDE_10_0_2=1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; H_PS_PSSID=36558_36463_36726_36454_31254_34813_36690_36165_36693_36698_36569_36807_36775_36731_36738_36762_36768_36764_26350_36714_36651; delPer=0; PSINO=7; BA_HECTOR=a0a020aga0810084012ndkis1hcimd217; ZFY=MGlTO0sMW1WEKuuZOLNwzilEuqDxC0WO4OktGpQbrcI:C; BAIDUID_BFESS=CC173ADE8E215811605C3415A100ACD8:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1657027973,1657028205,1657029051,1657370499; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1657370749',
    }
    kw = input('input a word:')
    data = {
        'wd': kw
    }
    # get后两个参数:params  参数
    #             kwargs  字典
    response = requests.get(url=baseurl, params=data, headers=headers)
    return response


# 解码数据
def get_content(response):
    content = response.text
    return content


if __name__ == '__main__':
    baseurl = get_baseurl()
    response = get_response(baseurl)
    content = get_content(response)
    print(content)

    # 你发现它少了请求对象的定制      参数不需要urlencode来编码
