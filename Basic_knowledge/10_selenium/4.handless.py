from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#你的浏览器安装路径
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path

browser = webdriver.Chrome(options=chrome_options)
# --------------------------------------------------以上是固定不变的--------------------------------------------------

#这个玩意牛在不需要打开浏览器,也能完成你指定的操作;所以速度会快很多
#其他操作和在   交互  中一样
baseurl = 'https://www.baidu.com/'
browser.get(baseurl)
browser.save_screenshot('baidu.png')