# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert

driver = webdriver.Ie()
driver.maximize_window()
driver.get('http://sahitest.com/demo/index.htm')

current_window = driver.current_window_handle  # 获取当前窗口handle name
driver.find_element_by_link_text('Window Open Test With Title').click()

all_windows = driver.window_handles  # 获取所有窗口handle name
# 切换window，如果window不是当前window，则切换到该window
for window in all_windows:
    if window != current_window:
        driver.switch_to.window(window)

print(driver.title)  # 打印该页面title
sleep(3)
driver.close()
driver.switch_to.window(current_window)  # 关闭新窗口后切回原窗口，在这里不切回原窗口，是无法操作原窗口元素的，即使你关闭了新窗口
print(driver.title)  # 打印原页面title
sleep(3)

driver.quit()
