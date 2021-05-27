from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('https://www.bing.com/')

# 判断属性的值来定位元素，用[]
element = wd.find_element_by_css_selector("[class='logo']")
print(element.get_attribute('outerHTML'))

# 同时也可以加限制条件，比如class值是logo，而且标签名为svg
element = wd.find_element_by_css_selector("svg[class='logo']")
print(element.get_attribute('outerHTML'))

wd.quit()