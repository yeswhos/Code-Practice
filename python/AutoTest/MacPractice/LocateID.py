from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')

wd.get('https://www.baidu.com')
# 根据id选择元素，返回的就是该元素对应的webElement对象
element = wd.find_element_by_id('kw')

# 通过该webElement对象，可以对页面元素进行操作，比如下面输入字符串到输入框
element.send_keys('buff\n')

wd.quit()