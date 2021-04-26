import time

from selenium import webdriver

wd = webdriver.Chrome(r'D:\chromedriver.exe')
wd.get('https://www.baidu.com')
wd.find_element_by_id('kw').send_keys('csgo')
wd.find_element_by_id('su').click()
# 轮询，最大时间10s
wd.implicitly_wait(10)
element_new = wd.find_element_by_id('1')
# 获取某个属性
print(element_new.get_attribute('srcid'))
# 获取文本内容
print(element_new.text)
# 获取元素整个标签
print(element_new.get_attribute('outerHTML'))
# 获取元素内部的标签
print(element_new.get_attribute('innerHTML'))
wd.quit()

