from selenium import webdriver

wd = webdriver.Chrome(r'D:/chromedriver.exe')
wd.implicitly_wait(5)
wd.get('https://cn.bing.com/')

element = wd.find_elements_by_css_selector('[herf="http://go.microsoft.com/fwlink/?LinkId=521839"]')
for ele in element:
    print(ele.get_attribute('outerHTML'))
wd.quit()