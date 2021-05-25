from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('https://yeswhos.github.io/')

# 可选择子元素和后代元素
# 直接下属第一层的是子元素，后好多层的就是后代元素了
try:
    element = wd.find_element_by_css_selector('.post-item  .left >.post-title')
    print(element.get_attribute('outerHTML'))
except Exception as e:
    print(e)
finally:
    wd.quit()