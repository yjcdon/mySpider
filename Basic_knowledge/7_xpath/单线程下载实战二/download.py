import requests
import os
import datetime


def receive_url():
    img_url = ['https://meixiu.in/wp-content/uploads/2022/07/202207021815whkgvoe4i.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/202207021844grhmlgw01.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218sngc4dgcigp.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218gc5y1pj2wkr.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218rvpdebwojjm.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218vhuo0wat1fr.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218nzgt233czmf.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218abmke2iggno.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218tegwpv0dtb0.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218la53dwsd44u.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/202207021851fq3tyay3d.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218c40t0sie0yh.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218jssjtgg2jio.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/20220702180hlxyh3ndzk.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/20220702181uucyw2zrbt.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218fd0ebwq2inx.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218rzv3v0yruym.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218ck2nrze0h4p.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218sixfqhoaoxh.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218a0wnyr2sef1.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218vaon33opb2m.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218i3hay2mzsik.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218vdp4nc3atic.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218lufqhmseebs.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218wypdrkdgvw2.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218jl3hoaqhekb.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218lc4zj3n4zdz.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218nx5wxdpw2jk.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/20220702183vbbg0k4pjl.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218iuqqgbg5fyz.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218tjeipp2ffah.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218dopkrrnb0fk.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218bqotu3udwqh.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218f5iyzlaybkp.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/20220702183l1enxxi30q.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218rxdqtd3rni1.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218nfwa5mu1mth.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218sxb3mpddccw.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218pwcbw4rnouh.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218vvuyqkan5x0.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218juk1k034kov.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218pwwsvfncdi3.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218fnatobotcep.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218s55odcs4bga.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218ib1hmqgxgf2.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218tj433bdybjy.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218b1dl0fgijjb.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218yaoseqzir2s.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218q4zhyegmho3.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218t45gik1isek.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218eei5oo3ntzx.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218cuqdclvqhbo.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218vuoaeltsbgs.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218mxl024uybbe.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218wi0daepfbmb.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218f4nky12d0ic.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218y1kwrdup1ew.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218aapzlcvglk5.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218qb041bowbpa.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218gue1oso5c4j.jpg',
'https://meixiu.in/wp-content/uploads/2022/07/2022070218dl1xx41uqh1.jpg',

]

    return img_url


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


def download(img_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    for i in range(len(img_url)):
        response = requests.Session().get(url=img_url[i], headers=headers)
        if os.path.exists(str(i + 1) + '.jpg'):
            continue
        else:
            with open(str(i + 1) + '.jpg', 'wb') as f:
                f.write(response.content)
            print('complished ' + str(i + 1))


if __name__ == '__main__':
    num = input('输入文件夹的数字:')
    makedir('D:\Basic spider\Basic knowledge\\0 download\呆梨\\' + num, num)
    img_url = receive_url()
    print('downloading...')
    download(img_url)
    print('over')
