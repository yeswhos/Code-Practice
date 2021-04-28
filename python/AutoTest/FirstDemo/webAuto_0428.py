from selenium import webdriver

wd = webdriver.Chrome(r'D:/chromedriver.exe')
wd.implicitly_wait(5)
wd.get('https://yeswhos.github.io/')

# class用. 标签直接加，id用#
# 直接后代 > ，所有子结点空格
elements = wd.find_elements_by_css_selector('.post-item  h2')
# elements = wd.find_elements_by_css_selector('h2')
for element in elements:
    print("--------------------------")
    print(element.get_attribute('outerHTML'))
    #print(element.get_attribute('innerHTML'))

wd.quit()