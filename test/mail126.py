from selenium import webdriver
import time
from public import Login

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.126.com")




Login().user_login(driver,"a724153792","18795650445ya")

#收信，写信，删除信息等操作
time.sleep(5)


#退出
Login().user_logout(driver)

