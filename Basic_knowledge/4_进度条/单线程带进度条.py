import requests
# 导入 tqdm
from tqdm import tqdm

# 文件下载直链
url = 'https://issuecdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.2.8.9.exe'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
file_name = 'BaiduNetdisk_7.2.8.9.exe'
# 发起 head 请求，即只会获取响应头部信息
head = requests.head(url=url, headers=headers)
# 文件大小，以 MB 为单位
file_size = int(head.headers.get('Content-Length'))
response = requests.get(url=url, headers=headers, stream=True)
# 一块文件的大小
chunk_size = 1024
# 这里是生成进度条的函数
bar = tqdm(total=file_size, desc='下载文件:' + file_name, unit_scale=True, unit='B', colour='blue')
with open(file_name, 'wb') as f:
    # 写入分块文件
    for chunk in response.iter_content(chunk_size=chunk_size):
        f.write(chunk)
        bar.update(chunk_size)
# 关闭进度条
bar.close()
