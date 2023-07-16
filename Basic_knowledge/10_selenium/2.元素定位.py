# 比如你要搜索周杰伦,那你要找到文本框,输入周杰伦,点百度一下
# 可以实现自动化,模拟键鼠操作
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_baseurl():
    baseurl = 'https://www.baidu.com/'
    return baseurl


# 创建浏览器对象
def create_browser_obj():
    path = 'chromedriver.exe'
    browser = webdriver.Chrome(path)
    return browser


# 访问网站
def access_web(browser, baseurl):
    browser.get(baseurl)


# 元素定位
def ele_position(browser):
    # 这个函数要导入一些东西
    # By.你需要的东西的大写,有ID,NAME,CLASS,标签名;XPATH,LINK_TEXT(超链接)
    # button=browser.find_elements(By.ID,'su')
    # button=browser.find_elements(By.NAME,'wd')
    # browser.find_elements(By.XPATH,'//div[@id="s-top-left"]/a[@href="http://news.baidu.com"]')
    button=browser.find_element(By.LINK_TEXT,'新闻')
    # 有s则返回列表
    print(button)


if __name__ == '__main__':
    baseurl = get_baseurl()
    browser = create_browser_obj()
    access_web(browser, baseurl)
    ele_position(browser)
