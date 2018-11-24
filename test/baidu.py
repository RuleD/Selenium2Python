# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

search_text = ['python','中文','text']

#driver = webdriver.Firefox()

for text in search_text:
    driver = webdriver.Ie()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(text)
    driver.find_element_by_id("su").click()
    driver.quit()





'''
try:
    print(time.ctime())
    driver.find_element_by_id("22222222").send_keys("adf")
except NoSuchElementException as e:
    print(e)
finally:
    print(time.ctime())
    driver.quit()
'''
'''
print(time.ctime())
for i in range(10):
    try:
        el = driver.find_element_by_id("22kw22")
        if el.is_displayed():
            break
    except:
        pass
        time.sleep(1)
    else:
        print("time out")
driver.close()        
print(time.ctime())
         '''


'''
element=WebDriverWait(driver,5,0.5).until(
    EC.presence_of_element_located((By.ID,"kw"))
)
element.send_keys('selenium')
'''

#driver.find_element_by_id("kw").send_keys("Selenium2")
#driver.find_element_by_id("su").click()
#driver.quit()


'''
#获取输入框的尺寸
size = driver.find_element_by_id("kw").size
print(size)

#获取百度页面底部备案信息
text = driver.find_element_by_id("cp").text
print(text)

#返回元素的属性值，可以是id、name、type或其他任意属性
attribute=driver.find_element_by_id("kw").get_attribute("type")
print(attribute)

#返回元素的结果是否可见，返回结果为True或False
result = driver.find_element_by_id("kw").is_displayed()
print(result)
'''

