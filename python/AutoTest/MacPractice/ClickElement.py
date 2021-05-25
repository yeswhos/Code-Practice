from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('https://www.bing.com/')

"""
不仅webdriver有选择元素的方法，webElement也有选择元素的方法
WebElement也可以调用find element by什么什么方法

WebDriver选择元素范围是整个web界面
WebElement选择范围是某个元素的内部
"""
wd.find_element_by_id('sb_form_q').send_keys('how to find a girlfriend')
wd.find_element_by_id('sb_go_par').click()
