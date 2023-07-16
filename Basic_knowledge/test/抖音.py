import requests
import os
from lxml import etree

from selenium import webdriver
from selenium.webdriver.common.by import By

# 需要selenium,并且是无窗口的打开才行
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 'ttwid=1%7CV_NLJsEWWBwe_89wtgvDmRDbRwRQmoCjF2NhCluaqOQ%7C1671986295%7C341cf094c20c503fc6d3a891b007eb7989f60a3707deb242fe5c9402a05bdf40; d_ticket=0d04636698a8ce83503cea090f380da237a4b; passport_assist_user=CkEOj9b3v5drh4c2sK_swQZTK-0hIZErCjDvhwP1qmzG-fP0JoR7giTYHz-YyoHjgT0XcXPPHlPF9689Ksj03KJf9RpICjxL0TI7ca5q15mvElOz5omxfG1C9LnDHDtQ9LQK_tnVXkf6mpRMeELYaQbyYLLgTSjUc9BJWb6f2UIhg6UQrcWpDRiJr9ZUIgEDU0izEA%3D%3D; n_mh=P3gRmpc_LjfyXPoz7tuVRWAWjuuxMcNtEj83842N19M; sso_auth_status=c6b12d997c0d16c1ccb9d56ef15a85fe; sso_auth_status_ss=c6b12d997c0d16c1ccb9d56ef15a85fe; sso_uid_tt=303859459c850b3a823fae711ffe5a2f; sso_uid_tt_ss=303859459c850b3a823fae711ffe5a2f; toutiao_sso_user=a58d9ea466530a9eb94e45a3e7bed4e4; toutiao_sso_user_ss=a58d9ea466530a9eb94e45a3e7bed4e4; sid_ucp_sso_v1=1.0.0-KDE5ZmZmNWFkMzlmMTA4YjZhNzliYTQwNDNhMGRkZjY3YzQ3YzZkMjcKHwjPucC9qI3fBBDy072fBhjvMSAMMPf4oZ0GOAJA7AcaAmxmIiBhNThkOWVhNDY2NTMwYTllYjk0ZTQ1YTNlN2JlZDRlNA; ssid_ucp_sso_v1=1.0.0-KDE5ZmZmNWFkMzlmMTA4YjZhNzliYTQwNDNhMGRkZjY3YzQ3YzZkMjcKHwjPucC9qI3fBBDy072fBhjvMSAMMPf4oZ0GOAJA7AcaAmxmIiBhNThkOWVhNDY2NTMwYTllYjk0ZTQ1YTNlN2JlZDRlNA; odin_tt=168117a3f6e9d9812a9fca8941b6a7b620490828402b17c226cef8812686a69987aa1d8a8b732abd04d0ca9eb725c63356dc26765487618560a331869043394d; passport_auth_status=642ed2485daaef809d8950d472cbba85%2C5bcaee11eca044d5941f85b0b9aa6c64; passport_auth_status_ss=642ed2485daaef809d8950d472cbba85%2C5bcaee11eca044d5941f85b0b9aa6c64; uid_tt=388ce70caabc95dbf758515eb28b455e; uid_tt_ss=388ce70caabc95dbf758515eb28b455e; sid_tt=49f237b5036333286501358b90b04a20; sessionid=49f237b5036333286501358b90b04a20; sessionid_ss=49f237b5036333286501358b90b04a20; sid_guard=49f237b5036333286501358b90b04a20%7C1676634623%7C5183986%7CTue%2C+18-Apr-2023+11%3A50%3A09+GMT; sid_ucp_v1=1.0.0-KGY5YjBhMDQ4M2YyZjhlNmQ3NmExNTZjMjkxZTM2OWQ3ZjdhNjViYzEKGwjPucC9qI3fBBD_072fBhjvMSAMOAJA7AdIBBoCbGYiIDQ5ZjIzN2I1MDM2MzMzMjg2NTAxMzU4YjkwYjA0YTIw; ssid_ucp_v1=1.0.0-KGY5YjBhMDQ4M2YyZjhlNmQ3NmExNTZjMjkxZTM2OWQ3ZjdhNjViYzEKGwjPucC9qI3fBBD_072fBhjvMSAMOAJA7AdIBBoCbGYiIDQ5ZjIzN2I1MDM2MzMzMjg2NTAxMzU4YjkwYjA0YTIw; douyin.com; strategyABtestKey=%221677574172.463%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1678178972475%2C%22type%22%3A1%7D; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWNsaWVudC1jZXJ0IjoiLS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tXG5NSUlDRlRDQ0FidWdBd0lCQWdJVkFKNjBidUFIZ3Y3QjhmOWhWQmRFbWt1UGdOWG1NQW9HQ0NxR1NNNDlCQU1DXG5NREV4Q3pBSkJnTlZCQVlUQWtOT01TSXdJQVlEVlFRRERCbDBhV05yWlhSZlozVmhjbVJmWTJGZlpXTmtjMkZmXG5NalUyTUI0WERUSXpNREl4TnpFeE5UQXhNRm9YRFRNek1ESXhOekU1TlRBeE1Gb3dKekVMTUFrR0ExVUVCaE1DXG5RMDR4R0RBV0JnTlZCQU1NRDJKa1gzUnBZMnRsZEY5bmRXRnlaREJaTUJNR0J5cUdTTTQ5QWdFR0NDcUdTTTQ5XG5Bd0VIQTBJQUJOZmpLdnE2Q1ZwQTNiN0lKY3hqcWtnSmhrT21yODFJWDhHU3Rvc2hhbzBWdllEc2k5WXhvdm9GXG56bFJIOE5BS04rekRGQ2RvcXk4SHpQS0xEWEpjUmpXamdia3dnYll3RGdZRFZSMFBBUUgvQkFRREFnV2dNREVHXG5BMVVkSlFRcU1DZ0dDQ3NHQVFVRkJ3TUJCZ2dyQmdFRkJRY0RBZ1lJS3dZQkJRVUhBd01HQ0NzR0FRVUZCd01FXG5NQ2tHQTFVZERnUWlCQ0NlcXIvMmFvMjBXeFU3YzBCNHdhYTJQWHVEL1MzOXRsTGorVEY2WEhCTjREQXJCZ05WXG5IU01FSkRBaWdDQXlwV2Zxam1SSUVvM01UazFBZTNNVW0wZHRVM3FrMFlEWGVaU1hleUpIZ3pBWkJnTlZIUkVFXG5FakFRZ2c1M2QzY3VaRzkxZVdsdUxtTnZiVEFLQmdncWhrak9QUVFEQWdOSUFEQkZBaUJkSTZONkR1dVMvSzd0XG50ZE9QRTJxT3pSb09Fck5UNVRUR1FDWlpuVVRNTndJaEFNbkVJdWZJbHMwc09UdDRNbHpIZ1UrTGlMdFc4OHlJXG4wTkJqZGk1U1Q2aDZcbi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS1cbiJ9; s_v_web_id=verify_leo0cklh_n6y35Qqb_ts1o_45ej_BuZe_kCNje8lJJdox; LOGIN_STATUS=1; passport_csrf_token=aa25e9385ca9346266255894fd50c76c; passport_csrf_token_default=aa25e9385ca9346266255894fd50c76c; store-region=cn-gx; store-region-src=uid; csrf_session_id=15c03cc795c296361c07c641d30a418a; __ac_nonce=063fdc06e00afc455be27; __ac_signature=_02B4Z6wo00f01SipMVQAAIDBqKvLFoFXw20oiTXAACnacyVEIh9jQl9PTvW43trLjikRU13OZeVaAFVngBXF7OfchjaI47.xpzbNlU.vIxVBIUP5MXK2cWRDZX-sDd8I-qctBuyei4zuhXvQ93; passport_fe_beating_status=true; download_guide=%223%2F20230228%22; tt_scid=NvGV8aoT97XN.q4MCpHrMAoMbb396qSvnvUUGWIM2vr2AK3t4YCOvfDXOVMQyFao6cae; SEARCH_RESULT_LIST_TYPE=%22single%22; msToken=ArGoCyim0xs2Uolc4i8iJ-hB5d-MQV8jry8zzo2NCJIMHPNg0LBB4D6E0HTf7NPVJASDI3HHklMk98__Uzls88pqM3MT0gQH-nVHWZlW2eR3QblcT5uoR7umW9DI_6w=; home_can_add_dy_2_desktop=%221%22; msToken=G7yizlogTRKLzwKEiiqLR20J9pkwnDv0MMgU9G4f7ydXNWpWQ1PMX9VbScBMElfMKc2smf_izfqUMBesTIFlgvSzxWtnX98vaMhBoAX81WUjqPk-oW5iyzEtBy5Uu04=',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.3',
}


def test(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    t = driver.find_element(By.XPATH, '//video/source/@src')
    print(t)


def getVideoName(url):
    r = requests.Session().get(url=url, headers=headers, allow_redirects=False).text
    videoName = etree.HTML(r).xpath(
        '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[3]/div/div[1]/div/h1/span/span[2]/span/span[1]/span/span/span/text()')[
        0]
    return videoName


def download(url):
    r = requests.Session().get(url=url, headers=headers, allow_redirects=False).text
    videoURL = etree.HTML(r).xpath('//video/source/@src')
    return videoURL


def makedir(path):
    isExists = os.path.exists(os.path.join("path", path))
    if not isExists:
        print('系统中无该文件夹,创建的地址是:', path)
        # 创建文件夹
        os.makedirs(os.path.join("path", path))
        # 切换到创建的文件夹
        os.chdir(os.path.join("path", path))
        return True
    else:
        print(path, '该地址的文件夹已存在')
        os.chdir(os.path.join("path", path))
        return False


if __name__ == '__main__':
    # https://www.douyin.com/video/7205074781492759869
    # url = input('input url:')
    url = 'https://www.douyin.com/video/7205074781492759869'
    # test(url)
    # videoName = getVideoName(url)
    # print(videoName)
    # videoURL = download(url)
    # print(videoURL)
    t = requests.get(url=url, headers=headers).text
    print(t)