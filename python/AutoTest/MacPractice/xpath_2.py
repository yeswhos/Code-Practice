from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('http://cdn1.python3.vip/files/selenium/test1.html')

# 通过属性值来选择
element = wd.find_element_by_xpath('//select[@class="single_choice"]')
print(element.get_attribute('outerHTML'))

# 包含某个字符串
element = wd.find_element_by_xpath('//*[contains(@class,"single")]')
print(element.get_attribute('outerHTML'))

# 以什么字符串开头
element = wd.find_element_by_xpath('//starts_with(@class,"single")')
print(element.get_attribute('outerHTML'))
# # 以什么字符串结尾
# element = wd.find_element_by_xpath('//ends-with(@class,"choice")')
# print(element.get_attribute('outerHTML'))

wd.quit()