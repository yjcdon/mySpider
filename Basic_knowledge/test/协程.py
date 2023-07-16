import asyncio
import os
import time
import fake_useragent

import aiohttp
from lxml import etree
from tqdm import tqdm

# 生成随机ua
ua = fake_useragent.UserAgent(cache_path='fake_useragent.json').random

headers = {
    'Cookie': 'clickbids=122867; Hm_lvt_6dfe3c8f195b43b8e667a2a2e5936122=1677156736,1677233662; Hm_lpvt_6dfe3c8f195b43b8e667a2a2e5936122=1677237471',
    'User-Agent': ua
}


# proxies = [{'http': 'http://202.109.157.60:9000'}, {'http': 'http://121.13.252.62:41564'},
#            {'http': 'http://112.14.47.6:52024'}, {'http': 'http://121.13.252.58:41564'},
#            {'http': 'http://222.74.73.202:42055'}, {'http': 'http://117.114.149.66:55443'},
#            {'http': 'http://123.169.39.212:9999'}, {'http': 'http://27.42.168.46:55481'},
#            {'http': 'http://121.13.252.60:41564'}, {'http': 'http://61.216.185.88:60808'}, ]
# proxy = random.choice(proxies)
# proxy = str(proxy)


# 调用该函数后,文件指针指向该文件夹
def makedir(path):
    isExists = os.path.exists(os.path.join("path", path))
    if not isExists:
        # 创建文件夹
        os.makedirs(os.path.join("path", path))
        # 切换到创建的文件夹
        os.chdir(os.path.join("path", path))
        return True
    else:
        os.chdir(os.path.join("path", path))
        return False


async def get_title(url):
    # 创建异步HTTP会话
    async with aiohttp.ClientSession() as session:
        # 使用异步HTTP会话发送GET请求，并等待响应
        async with session.get(url=url, headers=headers) as resp:
            # 从响应中获取HTML文本并解析出小说标题
            html = await resp.text()
            title = etree.HTML(html).xpath('//*[@id="info"]/h1/text()')[0]
            # 打印小说标题
            print('该小说名为：' + title)
            # 返回小说标题
            return title


async def get_chapter_url(url, num):
    # 创建异步HTTP会话
    async with aiohttp.ClientSession() as session:
        # 使用异步HTTP会话发送GET请求，并等待响应
        async with session.get(url=url, headers=headers) as resp:
            # 从响应中获取HTML文本并解析出章节链接
            html = await resp.text()
            chapter_urls = []
            for i in range(0, num):
                # 获取第i个章节的链接并添加到列表中
                chapter_url = url + etree.HTML(html).xpath('//*[@id="list"]/dl/dd[%d]/a/@href' % (i + 1))[0]
                chapter_urls.append(chapter_url)
            # 返回包含所有章节链接的列表
            return chapter_urls


async def get_chapter_title(chapter_urls, num):
    # 创建空列表以存储所有章节标题
    chapter_titles = []
    async with aiohttp.ClientSession() as session:
        # 遍历所有章节链接并获取章节标题
        for i in range(0, num):
            # 使用异步HTTP会话发送GET请求，并等待响应
            async with session.get(url=chapter_urls[i], headers=headers) as resp:
                # 从响应中获取HTML文本并解析出章节标题
                html = await resp.text()
                chapter_title = etree.HTML(html).xpath('//*[@id="wrapper"]/div[5]/div/div[2]/h1/text()')[0] \
                    .replace('**', '')
                # 将章节标题添加到列表中
                chapter_titles.append(chapter_title)
    # 返回包含所有章节标题的列表
    return chapter_titles


async def download_chapter_content(url, title):
    try:
        # 创建异步HTTP会话并发送GET请求
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers) as resp:
                # 从响应中获取HTML文本并解析出章节内容
                html = await resp.text()
                chapter_content = etree.HTML(html).xpath('//*[@id="content"]/text()')
                string = '\r\n'

                # 将章节内容写入文件
                with open(title + '.txt', 'w', encoding='utf-8') as f:
                    f.write(string.join(chapter_content))
    except Exception as e:
        # 如果下载失败，打印出错信息
        print(f"下载章节 {title} 失败：{e}")


# 和上一个相比,这段代码的作用是为了异步执行多个下载任务，并等待它们全部完成。
async def get_chapter_content(chapter_urls, num, chapter_titles):
    # 创建任务列表
    tasks = []

    # 循环添加下载任务到任务列表中
    for i in range(0, num):
        task = asyncio.create_task(download_chapter_content(chapter_urls[i], chapter_titles[i]))
        tasks.append(task)

    # 等待所有任务完成
    await asyncio.gather(*tasks)


async def main():
    # 输入小说目录页的URL
    url = input('请输入小说目录页的url：')
    if not url:
        print("请输入正确的小说目录页的url")
        return

    # 输入小说章节数
    num_input = input('请输入小说章节数：')
    if not num_input.isdigit():
        print("请输入正确的小说章节数")
        return
    num = int(num_input)

    # 获取小说标题并打印开始下载信息
    t1 = time.time()
    title = await get_title(url)
    print('开始下载《%s》...' % title)

    # 创建存储文件夹并进入其中
    makedir(title)

    # 获取各个章节链接
    chapter_urls = await get_chapter_url(url, num)
    print('共找到%d个章节' % len(chapter_urls))

    # 获取每个章节标题
    chapter_titles = await get_chapter_title(chapter_urls, num)

    # 开始下载所有章节内容
    await get_chapter_content(chapter_urls, num, chapter_titles)

    # 将所有章节内容合并为一本完整的小说并保存到本地
    await download_chapter_content(url, title)

    # 打印全部下载完成信息及耗时
    print('全部下载完成，用时%.2f秒' % (time.time() - t1))


if __name__ == '__main__':
    asyncio.run(main())
