from selenium import webdriver
import time
# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('https://yeswhos.github.io/')

"""
不仅webdriver有选择元素的方法，webElement也有选择元素的方法
WebElement也可以调用find element by什么什么方法

WebDriver选择元素范围是整个web界面
WebElement选择范围是某个元素的内部
"""
element = wd.find_element_by_class_name('left')
text_content = element.find_element_by_tag_name('h2')
print(text_content.text)

wd.quit()