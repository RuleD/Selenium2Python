from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

#获取cookie信息
cookie = driver.get_cookies()

#将获得cookie中的信息打印
print(cookie)
time.sleep(3)
driver.quit()