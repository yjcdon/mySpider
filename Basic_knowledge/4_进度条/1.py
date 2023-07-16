import requests

url = 'https://issuecdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.2.8.9.exe'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
head=requests.head(url=url,headers=headers)
#head.headers可以获取文件的很多信息
file_size=int(head.headers.get('Content-Length'))//1024//1024

print('文件大小:',file_size,'Mb')