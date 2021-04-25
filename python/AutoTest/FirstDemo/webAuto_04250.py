from selenium import webdriver

wb = webdriver.Chrome(r'D://chromedriver.exe')
wb.get("http://www.bing.com")
# element = wb.find_elements_by_tag_name('span')
# for ele in element:
#     print(ele.text)

# element = wb.find_elements_by_tag_name('div')
# for ele in element:
#     print(ele.text)

# element = wb.find_elements_by_id('est_switch')
# for ele in element:
#     print(ele.text)

elem = wb.find_element_by_id('est_switch')
el = wb.find_element_by_id('est_en')
print(el.text)