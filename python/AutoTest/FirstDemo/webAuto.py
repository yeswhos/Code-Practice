from selenium import webdriver

# 创建一个web-driver对象
wd = webdriver.Chrome(r'D:\chromedriver.exe')
wd.get('https://www.baidu.com')
# 返回webElement对象，通过这个对象，可以对界面元素进行操作
element = wd.find_element_by_id('kw')
element.send_keys('auto\n')
