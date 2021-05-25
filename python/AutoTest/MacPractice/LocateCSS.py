from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('https://yeswhos.github.io/')

# 通过class来定位元素，9和10行效果都是一样的。去掉.的话意思就是找标签名为site-title的，而不是class为那个的
element_1 = wd.find_element_by_css_selector('.site-title')
element_2 = wd.find_element_by_class_name('site-title')

# 选择id的时候带井号
element_3 = wd.find_element_by_css_selector('#app')
element_4 = wd.find_element_by_id('app')

# 选择标签的时候啥也不带
element_5 = wd.find_elements_by_css_selector('h1')
element_6 = wd.find_elements_by_tag_name('h1')

