from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Ie()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#获取百度搜索窗体的句柄
sreach_windows = driver.current_window_handle
time.sleep(1)
driver.find_element_by_link_text("登录").click()
time.sleep(1)
driver.find_element_by_link_text("立即注册").click()




#新建标签页
ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
# 关闭标签页
#ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
#获取当前所有打开的窗口的句柄
all_handles = driver.window_handles
print(len(all_handles))
time.sleep(5)


#进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print("now rgister window!")
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__userName"]').send_keys("username")
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__password"]').send_keys("password")
        time.sleep(2)

#回到搜索窗口
for handle in all_handles:
    if handle ==sreach_windows:
        driver.switch_to.window(handle)
        print("now sreach window!")
        driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)

driver.quit()       