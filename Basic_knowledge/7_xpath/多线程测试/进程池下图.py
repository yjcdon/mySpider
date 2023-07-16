from concurrent.futures import ProcessPoolExecutor
import requests
import os
from lxml import etree
import time


# def get_img(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
#     }
#     response=requests.get(url=url,headers=headers).text
#
#     img_url = etree.HTML(response).xpath('//div/p/img/@src')
#
#     return img_url

def get_img():
    img_url = ['https://meixiu.in/wp-content/uploads/2022/07/2022070218pbbckuyfkus.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218cfe5eg00zur.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218devmiivlqky.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218w2rmlk5k4rp.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/20220702184c0rxopq43t.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218coaaqn3gyeh.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218ndkewfzy0px.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/202207021802if3ra1fds.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218ovh0kol4wdm.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218tyx1o15ofg2.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218vuj4fzdr4xo.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218f5kqobjtws2.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218tfdkyzktuhm.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218iq4hprfnoyy.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218pkvhdf1zdlg.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218ms1kzlqnfoj.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218uo20bapox0n.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218bmfrbkkupxl.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218svgvqmtby4l.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218hqk4osc1gw5.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218tiad0phgev3.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218se5wrchr1m4.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218wqwm5ts2dyv.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218sb1pq2albkr.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/20220702182nuo4khsiy3.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218r0mh3wwkbhl.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/20220702181alvw4r4klq.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218eb5wikdahn5.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218r3eyko5bqxy.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218mtmhp0znljg.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218prxrirfgcbb.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218ax2t33rddu5.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/20220702182brqyri5r2i.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218t1nedphm2ii.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218puvtlv21fri.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218hdya4itxexb.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218zppxup0yhrq.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218lyvhlkja3ni.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218xqud4wmkjld.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218xltsuqoj4f2.jpg',
               'https://meixiu.in/wp-content/uploads/2022/07/2022070218f2fvpdarorj.jpg',
               ]

    return img_url


def download(img_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    for i in range(len(img_url)):
        response = requests.get(url=img_url[i], headers=headers)
        if os.path.exists(str(i + 1) + '.jpg'):
            continue
        else:
            with open(str(i + 1) + '.jpg', 'wb') as f:
                f.write(response.content)
            print('complished ' + str(i + 1))

def makedir(path, num):
    isExists = os.path.exists(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))
    if not isExists:
        print('系统中无该文件夹,创建的地址是:', path)
        os.makedirs(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))
        os.chdir(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))
        return True
    else:
        print(path, '该地址的文件夹已存在')
        os.chdir(os.path.join("D:\Basic spider\Basic knowledge\\0 download\呆梨\\" + num, path))
        return False

if __name__ == '__main__':
    # url=input('输入url:')
    num = input('输入文件夹的数字:')
    img_url=get_img()
    makedir('D:\Basic spider\Basic knowledge\\0 download\呆梨\\' + num, num)
    start=time.time()
    with ProcessPoolExecutor(10) as executor:
        print('downloading...')
        future=executor.submit(download, img_url)
        executor.shutdown(wait=True)
    end=time.time()
    print('consume time=',end-start,'secodes')
    print('over')


