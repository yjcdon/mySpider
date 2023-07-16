#-*- coding: utf-8 -*
import requests


src = 'http://img.netbian.com/file/2018/0127/7acb22d76d5ad9706bbb4251481b2e3b.jpg'

r = requests.get(src)

with open('bizhi.jpg', 'wb') as f:
    f.write(r.content)

print('下载完成')