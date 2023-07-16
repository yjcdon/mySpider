import os
import time
import random
import fake_useragent
import sys
import concurrent.futures

import requests
from lxml import etree
from tqdm import tqdm

# 生成随机ua
ua = fake_useragent.UserAgent(cache_path='fake_useragent.json').random
global proxy_list_random_num

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_6dfe3c8f195b43b8e667a2a2e5936122=1677156736,1677233662,1677496887,1677573254; clickbids=134823',
    'Host': 'www.biquzw.la',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua
}


# 从快代理中获取随机的ip
def get_proxy():
    # 随机获得1~30的整数和url拼起来,从随机url中再随机选择一组ip和端口,可以保证每次爬取的ip都不一样
    url = 'https://www.kuaidaili.com/free/inha/' + str(random.randint(1, 30))
    # print(url)
    headers = {
        'User-Agent': ua
    }
    r = requests.Session().get(url, headers=headers, timeout=10).text

    rows = etree.HTML(r).xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
    global proxy_list
    proxy_list = []
    for row in rows:
        # 把响应速度小于1秒的ip用于爬取
        response_time = float(str(row.xpath('./td[@data-title="响应速度"]/text()')[0]).replace('秒', ''))
        if response_time < 1:
            ip = row.xpath('./td[@data-title="IP"]/text()')[0]
            port = row.xpath('./td[@data-title="PORT"]/text()')[0]
            protocol = row.xpath('./td[@data-title="类型"]/text()')[0].lower()
            proxy_list.append({protocol: f'{ip}:{port}'})  # 变成字典后再变成列表
        else:
            continue
    # print(proxy_list)
    return proxy_list


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


def get_novel_title():
    # with作用:使用后会自动关闭
    with requests.Session() as session:
        proxy_list_random_num = random.randint(0, len(proxies) - 1)
        # print(proxies[proxy_list_random_num])
        r = session.get(url=url, headers=headers, proxies=proxies[proxy_list_random_num])
        r.encoding = 'utf-8'
        title = etree.HTML(r.content).xpath('//*[@id="info"]/h1/text()')[0]
        print(f'该小说名为：{title}')
    return title


def get_chapter_url(num):
    proxy_list_random_num = random.randint(0, len(proxies) - 1)
    # print(proxies[proxy_list_random_num])
    r = requests.Session().get(url=url, headers=headers, proxies=proxies[proxy_list_random_num])
    r.encoding = 'utf-8'
    chapter_urls = []
    for i in range(0, num):
        chapter_url = url + etree.HTML(r.content).xpath('//*[@id="list"]/dl/dd[%d]/a/@href' % (i + 1))[0]
        chapter_urls.append(chapter_url)
    return chapter_urls


def get_chapter_title(chapter_urls, ):
    with requests.Session() as session:
        chapter_titles = []
        for chapter_url in chapter_urls:
            proxy_list_random_num = random.randint(0, len(proxies) - 1)
            # print(proxies[proxy_list_random_num])
            r2 = session.get(url=chapter_url, headers=headers, proxies=proxies[proxy_list_random_num])
            r2.encoding = 'utf-8'
            chapter_title = etree.HTML(r2.content).xpath('//*[@id="wrapper"]/div[5]/div/div[2]/h1/text()')[0].replace(
                '**',
                '')
            chapter_titles.append(chapter_title)
    return chapter_titles


def get_chapter_content(chapter_urls, page_num, chapter_titles, ):
    with requests.Session() as session:
        for i in tqdm(range(0, page_num), unit='txt', desc='downloading', ncols=80, position=0, mininterval=0.1):
            proxy_list_random_num = random.randint(0, len(proxies) - 1)
            # print(proxies[proxy_list_random_num])
            r2 = session.get(url=chapter_urls[i], headers=headers, proxies=proxies[proxy_list_random_num])
            r2.encoding = 'utf-8'
            chapter_content = etree.HTML(r2.content).xpath('//*[@id="content"]/text()')
            string = '\r\n'
            with open(chapter_titles[i] + '.txt', 'w', encoding='utf-8') as f:
                f.write(string.join(chapter_content))


def multiThread():
    with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:
        executor.submit(get_chapter_url, num)
        executor.submit(get_chapter_title, chapter_urls)
        executor.submit(get_chapter_content, chapter_urls, num, chapter_titles)


def get_valid_page_num(max_page):
    """获取有效文章数"""
    while True:
        page_num_str = input(
            f"该小说共有{max_page}篇文章，全要请输入最大数字，否则请输入目标数字（1-{max_page}）(输入-1结束程序):")
        if page_num_str == "-1":
            print("==========================结束===========================")
            sys.exit()
        if not page_num_str.isdigit():
            print("请输入数字!")
            continue
        page_num = int(page_num_str)
        if page_num > max_page or page_num < 1:
            print(f"请输入1~{max_page}之间的数字!")
        else:
            if page_num == max_page:
                page_num = max_page
            return page_num


def get_maxpage_and_judge():
    global url
    session = requests.Session()
    while True:
        url = input('输入笔尖中文小说网址(如:https://www.biquzw.la/134_134823/):')
        # 判断字符串是否以某些字符开头
        if url.startswith("https://www.biquzw.la/"):
            try:
                proxy_list_random_num = random.randint(0, len(proxies) - 1)
                r = session.get(url=url, headers=headers, proxies=proxies[proxy_list_random_num]).text
                maxpage = len(etree.HTML(r).xpath('//*[@id="list"]/dl/text()')) - 1
                break
            except ValueError:
                print("输入正确的URL!")
        else:
            print("请输入有效的笔尖中文小说网址！")
    return maxpage


if __name__ == '__main__':
    proxies = get_proxy()
    proxy = random.choice(proxies)

    max_page = get_maxpage_and_judge()
    num = get_valid_page_num(max_page)

    print('==========================开始===========================')
    start = time.time()
    title = get_novel_title()
    makedir(r'D:\\Basic_spider\\Basic_knowledge\\novel\\' + title)
    chapter_urls = get_chapter_url(num, )
    chapter_titles = get_chapter_title(chapter_urls)
    multiThread()
    end = time.time()
    print('下载完成! 共用时%.1f' % (end - start) + '秒')
