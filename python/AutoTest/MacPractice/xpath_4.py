from selenium import webdriver

# 创建webdriver对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome('/Users/mengfanhui/Downloads/chromedriver')
wd.implicitly_wait(10)
wd.get('http://cdn1.python3.vip/files/selenium/test1.html')

# 选取us的上一层节点
element = wd.find_element_by_xpath('//*[@id="us"]/..')
print("--------------------------------------")
print(element.get_attribute('outerHTML'))

# 选取后续标签为select的同级兄弟节点
element = wd.find_elements_by_xpath('//*[@class="single_choice"]/following-sibling::select')
print("--------------------------------------")
for ele in element:
    print(ele.get_attribute('outerHTML'))

# 选取无论标签是什么的前面的兄弟节点
element = wd.find_elements_by_xpath('//*[@class="single_choice"]/preceding::*')
print("--------------------------------------")
for ele in element:
    print(ele.get_attribute('outerHTML'))

# 逐级往下找，关键是下面的option前面要加点
element_1 = wd.find_element_by_xpath('//*[@class="single_choice"]')
element_2 = element_1.find_element_by_xpath('./option[1]')
print("--------------------------------------")
print(element_2.text)

wd.quit()