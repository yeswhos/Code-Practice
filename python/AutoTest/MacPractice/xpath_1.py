from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('http://cdn1.python3.vip/files/selenium/test1.html')

element = wd.find_element_by_xpath('html/body/div/p')
print(element.get_attribute('outerHTML'))

# //div//p表示div下所有的p子节点
# //div/p 表示div的p直接子节点（隔一个不行）
element = wd.find_elements_by_xpath('//div//p')
for ele in element:
    print(ele.text)

# *所有的子节点
element = wd.find_elements_by_xpath('//div/*')
for ele in element:
    print(ele.text)

wd.quit()