from selenium import webdriver


def get_baseurl():
    baseurl = 'https://www.jd.com/'
    return baseurl


# 创建浏览器对象
def create_browser_obj():
    path = 'chromedriver.exe'
    browser = webdriver.Chrome(path)
    return browser


# 访问网站
def access_web(browser, baseurl):
    browser.get(baseurl)


# 获取源码      貌似要打开网站,才能打印源码
def get_src_code(browser):
    srccode = browser.page_source  # browser.page_source获取网页源码
    print('OK')

if __name__ == '__main__':
    baseurl = get_baseurl()
    browser = create_browser_obj()
    access_web(browser, baseurl)
    get_src_code(browser)
