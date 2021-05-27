from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('http://cdn1.python3.vip/files/selenium/sample1b.html')

# libai，第二个为span的子节点
element = wd.find_element_by_css_selector('span:nth-child(2)')
print(element.text)

# 李白，倒数第二个为span的子节点
element = wd.find_element_by_css_selector('span:nth-last-child(2)')
print(element.text)

# span类型的第一个节点
element = wd.find_element_by_css_selector('span:nth-of-type(1)')
print(element.text)

# span类型的倒数第二个节点
element = wd.find_element_by_css_selector('span:nth-last-of-type(1)')
print(element.text)

# p类型所有偶数的节点，这块应该用for循环打印所有的会好些
element = wd.find_element_by_css_selector('p:nth-of-type(even)')
print(element.text)

# p类型所有的奇数节点，和上个一样
element = wd.find_element_by_css_selector('p:nth-of-type(odd)')
print(element.text)
