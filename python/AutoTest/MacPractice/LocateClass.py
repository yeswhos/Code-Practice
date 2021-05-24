from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')

wd.get('https://yeswhos.github.io/')

element = wd.find_element_by_class_name('post-title')
print(element.text)

elements = wd.find_elements_by_tag_name('h2')
for ele in elements:
    print(ele.text)