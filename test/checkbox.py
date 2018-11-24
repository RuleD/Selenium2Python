from selenium import webdriver
import os,time

driver = webdriver.Ie()
file_path = "file:///"+os.path.abspath("checkbox.html")
driver.get(file_path)

#选择页面上所有的tag name为input 的元素
inputs =  driver.find_elements_by_tag_name("input")
for i in inputs:
    if i.get_attribute("type") == "checkbox":
        i.click()
        time.sleep(1)

#打印当前页面上的type为checkbox 的个数
print(len(inputs))

#把页面上最后1个chechbox的勾去掉
driver.find_elements_by_css_selector("input[type=checkbox]").pop().click()