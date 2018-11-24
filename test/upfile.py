from selenium import webdriver
import os,time

driver = webdriver.Ie()
file_path = "file:///"+os.path.abspath("upfile.html")
driver.get(file_path)

'''
#定位上传按钮，添加本地文件
driver.find_element_by_name('file').send_keys('F:\\Selenium2Python\\test\\baidu.py')
'''

#单击打开上传窗口
driver.find_element_by_name("file").click()
#调用upfile.exe 上传程序
os.system('F:\\Selenium2Python\\test\\upfile.exe')


time.sleep(3)
driver.quit()
