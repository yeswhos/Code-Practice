from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')

# 切换到frame里面去
# wd.switch_to.frame('frame1')
# wd.switch_to.frame('innerFrame')
wd.switch_to.frame(wd.find_element_by_css_selector('[src="sample1.html"]'))
element = wd.find_element_by_css_selector('.plant')
print(element.get_attribute('innerHTML'))

wd.switch_to.default_content()

# 然后再 选择操作 外部的 HTML 中 的元素
wd.find_element_by_id('outerbutton').click()

wd.quit()