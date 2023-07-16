import time
from lxml import etree
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains  # 实现键鼠一些操作的类

obj = webdriver.Chrome('chromedriver.exe')

obj.get('https://www.meitu131.com/meinv/7368/')
obj.maximize_window()
action = ActionChains(obj)
# 鼠标右键,记得要perform()才可以执行
# target1 = obj.find_element(By.XPATH, '//div/div[2]/p/a/img')  # 你要的是element,不是图片的url
# action.context_click(target1).perform()
for i in range(0,37):
    target1 = obj.find_element(By.XPATH, '//div/div[2]/p/a/img')
    action.context_click(target1).perform()
    pyautogui.typewrite('down')
    pyautogui.typewrite(['enter'])

    # time.sleep(1)
    # bottom = 'document.documentElement.scrollTop=1500'
    # obj.execute_script(bottom)
    new_window=obj.window_handles
    obj.switch_to.window(new_window[-1])

# 鼠标滚轮滚动

# target2 = obj.find_element(By.XPATH, '//div[3]/a')
# action.click(target2).perform()
