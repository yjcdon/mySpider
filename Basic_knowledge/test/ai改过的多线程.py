import os
import threading
import time
import random
import fake_useragent

import requests
from lxml import etree
from tqdm import tqdm

# generate a random user agent
ua = fake_useragent.UserAgent(cache_path='fake_useragent.json').random

headers = {
    'Cookie': 'clickbids=122867; Hm_lvt_6dfe3c8f195b43b8e667a2a2e5936122=1677156736,1677233662; Hm_lpvt_6dfe3c8f195b43b8e667a2a2e5936122=1677237471',
    'User-Agent': ua
}
proxies = [{'http': 'http://202.109.157.60:9000'}, {'http': 'http://121.13.252.62:41564'},
           {'http': 'http://112.14.47.6:52024'}, {'http': 'http://121.13.252.58:41564'},
           {'http': 'http://222.74.73.202:42055'}, {'http': 'http://117.114.149.66:55443'},
           {'http': 'http://123.169.39.212:9999'}, {'http': 'http://27.42.168.46:55481'},
           {'http': 'http://121.13.252.60:41564'}, {'http': 'http://61.216.185.88:60808'}, ]
proxy = random.choice(proxies)


# change the directory to the created folder
def change_directory(path):
    is_exists = os.path.exists(os.path.join("path", path))
    if not is_exists:
        os.makedirs(os.path.join("path", path))
    os.chdir(os.path.join("path", path))


def get_novel_title(url):
    r = requests.Session().get(url=url, headers=headers, proxies=proxy)
    r.encoding = 'utf-8'
    title = etree.HTML(r.text).xpath('//*[@id="info"]/h1/text()')[0]
    print(f'The novel title is: {title}')
    return title


def get_chapter_urls(url, num):
    r = requests.Session().get(url=url, headers=headers, proxies=proxy)
    r.encoding = 'utf-8'
    chapter_urls = [url + etree.HTML(r.text).xpath(f'//*[@id="list"]/dl/dd[{i + 1}]/a/@href')[0] for i in range(num)]
    return chapter_urls


def get_chapter_titles(chapter_urls):
    chapter_titles = []
    for url in chapter_urls:
        r = requests.Session().get(url=url, headers=headers, proxies=proxy)
        r.encoding = 'utf-8'
        chapter_title = etree.HTML(r.text).xpath('//*[@id="wrapper"]/div[5]/div/div[2]/h1/text()')[0] \
            .replace('**', '')
        chapter_titles.append(chapter_title)
    return chapter_titles


# def download_chapters(chapter_urls, chapter_titles):
#     for url, title in tqdm(zip(chapter_urls, chapter_titles), unit='txt', desc='downloading', ncols=80,
#                            position=0, mininterval=0.1):
#         r = requests.Session().get(url=url, headers=headers, proxies=proxy)
#         r.encoding = 'utf-8'
#         chapter_content = etree.HTML(r.text).xpath('//*[@id="content"]/text()')
#         string = '\r\n'
#         with open(title + '.txt', 'w', encoding='utf-8') as f:
#             f.write(string.join(chapter_content))

def download_chapters(chapter_urls, chapter_titles):
    for url, title in zip(chapter_urls, chapter_titles):
        r = requests.Session().get(url=url, headers=headers, proxies=proxy)
        r.encoding = 'utf-8'
        chapter_content = etree.HTML(r.text).xpath('//*[@id="content"]/text()')
        string = '\r\n'
        with open(title + '.txt', 'w', encoding='utf-8') as f:
            f.write(string.join(chapter_content))


def multi_thread_download(num, chapter_urls):
    # create threads for all three functions and start them
    thread_funcs = [get_chapter_urls, get_chapter_titles, download_chapters]
    args_list = [(url, num), (chapter_urls,), (chapter_urls, chapter_titles)]
    threads = [threading.Thread(target=func, args=args) for func, args in zip(thread_funcs, args_list)]
    for t in threads:
        t.start()
    # wait for all threads to finish
    for t in threads:
        t.join()


if __name__ == '__main__':
    while True:
        try:
            url = input('Enter the URL of the novel (e.g. https://www.example.com/): ')
            r = requests.Session().get(url=url, headers=headers, proxies=proxy).text
            maxpage = len(etree.HTML(r).xpath('//*[@id="list"]/dl/text()')) - 1
        except Exception as e:
            print("Please enter a valid URL!")
        else:
            break


    while True:
        try:
            num = int(input(f'The novel has {maxpage} chapters. Enter the number of chapters to download: '))
        except ValueError as e:
            print("Please enter a number!")
            continue
        if num > maxpage or num <= 0:
            print("Please enter a valid number of chapters!")
        else:
            if num == maxpage:
                num = maxpage
            break

    print('==========================Starting===========================')
    start_time = time.time()
    novel_title = get_novel_title(url)
    change_directory('D:\\Basic_spider\\Basic_knowledge\\novel\\' + novel_title)
    chapter_urls = get_chapter_urls(url, num)
    chapter_titles = get_chapter_titles(chapter_urls)
    multi_thread_download(num, chapter_urls)
    end_time = time.time()
    print(f'Download completed! Took {end_time - start_time:.1f} seconds.')
