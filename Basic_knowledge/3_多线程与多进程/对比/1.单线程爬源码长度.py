import requests
import time

url='https://www.cnblogs.com/'

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
start=time.time()
for i in range(0,20):
    if i==0:
        weburl=url
    else:
        weburl=url+'#p'+str(i+1)
    response=requests.get(url=weburl,headers=headers).text
    print(weburl,len(response))
end=time.time()
print('time=',end-start,'seconds')