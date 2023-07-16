from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

baseurl = 'https://www.baidu.com/'
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
browser.get(baseurl)

# 定位文本框
input = browser.find_element(By.ID, 'kw')

# 等待两秒
time.sleep(2)

# 输入周杰伦      想用send_keys,上面的find_element绝对没有s
input.send_keys('周杰伦')

# 定位百度一下
button = browser.find_element(By.ID, 'su')

# 点击百度一下
button.click()
time.sleep(2)

# 滑动到底部
bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(bottom)
time.sleep(2)

# 获取下一页的按钮并点击下一页
next_page = browser.find_element(By.CLASS_NAME, 'n').click()
time.sleep(2)

#回到上一页
browser.back()
time.sleep(2)

#下一页
browser.forward()
time.sleep(2)

#关闭浏览器
browser.quit()
