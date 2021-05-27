from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('http://cdn1.python3.vip/files/selenium/sample1b.html')

# h3后面的span标签，返回满足这样关系的span标签
element = wd.find_element_by_css_selector('h3+span')
print(element.text)