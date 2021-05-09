from selenium import webdriver

wd = webdriver.Chrome(r'D:/chromedriver.exe')
wd.implicitly_wait(5)
wd.get('https://yeswhos.github.io/')

elements = wd.find_elements_by_xpath('//*[@class="post-item"]/article[position()>3]')
for element in elements:
    print(element.get_attribute('outerHTML'))
wd.quit()