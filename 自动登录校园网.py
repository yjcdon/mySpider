import random

import requests

# 找对接口兄弟
# ip会变,现在不懂怎么操作

'''
1   10.33.0.108
2   10.34.180.181
3   10.33.28.241
'''
iplist = ['10.33.0.108', '10.34.180.181','10.33.28.241']
for i in range(0,10):
    ip = random.choice(iplist)

    url = 'http://10.0.1.5:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C2100300117&user_password=LiangYuJia66%40&wlan_user_ip=' + ip + '&wlan_user_ipv6=&wlan_user_mac=b07d648db2d3&wlan_ac_ip=' + ip + '&wlan_ac_name=HJ-BRAS-NE20E-S8&jsVersion=4.1&terminal_type=1&lang=zh-cn&v=6459&lang=zh'
    headers = {
        'Host': '10.0.1.5:801',
        'Referer': 'http://10.0.1.5/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',

    }

    data = {
        'user_account': '2100300117',
        'user_password': 'LiangYuJia66@',
    }

    r = requests.get(url=url, data=data, headers=headers)
    print('电脑')
    print(r)
