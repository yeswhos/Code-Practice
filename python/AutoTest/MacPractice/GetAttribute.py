from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('https://www.bing.com/')

"""
不仅webdriver有选择元素的方法，webElement也有选择元素的方法
WebElement也可以调用find element by什么什么方法

WebDriver选择元素范围是整个web界面
WebElement选择范围是某个元素的内部
"""
# 获取标签内某个属性的值
elem_1 = wd.find_element_by_id('sb_form_q')
print(elem_1.get_attribute('title'))

# 获取外部整个HTML，或者内部就是innerHTML
elem_2 = wd.find_element_by_id('sb_form_q')
print(elem_2.get_attribute('outerHTML'))

# 获取输入框里面的内容，除了value，也可以用innerText，或者textContent，适用于文本太长显示不完的情况
elem_3 = wd.find_element_by_id('sb_form_q')
elem_3.send_keys('how to find a girlfriend')
print(elem_3.get_attribute('value'))
wd.quit()

