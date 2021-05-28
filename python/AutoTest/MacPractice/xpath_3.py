from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('http://cdn1.python3.vip/files/selenium/test1.html')

# 选择子节点第一个的p节点
element = wd.find_element_by_xpath('//p[1]')
for ele in element:
    print(ele.get_attribute('outerHTML'))

# 选择倒数第二个的p节点
element = wd.find_element_by_xpath('//p[last()-1]')
for ele in element:
    print(ele.get_attribute('outerHTML'))

# 选择前两个的p节点
element = wd.find_element_by_xpath('//p[position()>=2]')
for ele in element:
    print(ele.get_attribute('outerHTML'))
    
# 选择倒数前三个的p节点
element = wd.find_element_by_xpath('//p[position()>=last()-2]')
for ele in element:
    print(ele.get_attribute('outerHTML'))

wd.quit()