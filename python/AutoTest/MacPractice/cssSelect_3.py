from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('https://yeswhos.github.io/')

# 用逗号，选取多个元素，即使这些元素没有什么关系
element = wd.find_element_by_css_selector("[href='https://yeswhos.github.io/post/ce-shi-lei-xing/'], .post-date")
print(element.get_attribute('outerHTML'))

wd.quit()