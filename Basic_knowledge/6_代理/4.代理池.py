#大量高匿的ip,需要random模块中的方法来随机选择

import random

proxies=[
    {'http':'114.114.114.114:666'},
    {'http':'123.123.123.123:777'},
    {'http':'8.8.8.8'}
]

proxy=random.choices(proxies)

print(proxy)