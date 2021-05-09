from selenium import webdriver

wd = webdriver.Chrome(r'D:/chromedriver.exe')
wd.implicitly_wait(5)
wd.get('https://yeswhos.github.io/')

ele_1 = wd.find_elements_by_xpath('//*[@class="post-item"]/div[position()<=2]')
for ele in ele_1:
    print(ele.get_attribute('outerHTML'))

wd.quit()