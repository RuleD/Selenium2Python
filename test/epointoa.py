from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
import time,sys
import csv #导入csv包

print("开始时间："+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#定义 是否整改完成 状态
rectificationState = {"无需整改":"0","已完成":"1","未完成":"2","开发已修复":"3","测试验证":"4","暂缓":"5"}
#内部复查结果
reviewStatus= {"通过":"1","不通过":"0"}

projectLeaders = []#定义负责人
#读取info.csv中项目信息
#读取本地csv文件
projectDatas = csv.reader(open('info.csv','r',newline='',encoding='GB2312'))
projectDicts = {}
#循环输出每一行的信息
for projectData in projectDatas:
    projectDicts[projectData[0]]=projectData#使用字典存储项目信息：key：项目名称，value：项目名称、负责人、完成时间、整改状态
    if projectData[1] not in projectLeaders:
        projectLeaders.append(projectData[1])

if len(projectLeaders) <= 0:
    print("没有需要执行的项目数据")
    sys.exit()

#启动自动化
driver= webdriver.Ie()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://oa.epoint.com.cn/epoint-sso-web/login/oauth2login")
'''
print("Before login=========================")
#打印当前页面的title
title = driver.title
print(title)
#打印当前页面的url
now_url=driver.current_url
print(now_url)
'''
driver.find_element_by_id("KEY").click()
driver.find_element_by_id("usbpsd").clear()
driver.find_element_by_id("usbpsd").send_keys("18795650445ya")
driver.find_element_by_class_name("submit").click()
time.sleep(3)
'''
print("After login=========================")
#再次打印当前页面的title
title = driver.title
print(title)
#打印当前页面的url
now_url=driver.current_url
print(now_url)
'''

try:
    #QA-T-PB-1809-009【重大共性整改】评标系统后台数据表管理去除数据增删改查功能 
    kfzUrl="https://fdoc.epoint.com.cn/dev/KFZknowledge/Pages/ProjectRecitify/Recitify_Detail.aspx?RowGuid=4ccc505c-2c4a-43c4-a7fc-0f2aab0dd6e3"
    driver.get(kfzUrl)
    parent_window = driver.current_window_handle
    #print(parent_window)
    pageTotal = 0
    try:
        pageTotal =int(driver.find_element_by_css_selector("div#ctl00_ContentPlaceHolder1_Pager>table>tbody>tr>td>font:nth-child(2)>b").text)
    except Exception:
        driver.refresh()
        time.sleep(5)
        pageTotal =int(driver.find_element_by_css_selector("div#ctl00_ContentPlaceHolder1_Pager>table>tbody>tr>td>font:nth-child(2)>b").text)
    #获取总页数
    print("获取总页数："+str(pageTotal))

    for page in range(pageTotal):
        pagecurrent=page+1
        print("当前所在页："+str(pagecurrent))
        if pagecurrent > 1:
            #翻页
            jsPage = "__doPostBack('ctl00$ContentPlaceHolder1$Pager','"+str(pagecurrent)+"')"
            driver.execute_script(jsPage)
            time.sleep(10)
        #获取当前页所有的项目循环遍历
        projects = driver.find_elements_by_css_selector("table#ctl00_ContentPlaceHolder1_Datagrid1>tbody>tr")
        #print(len(projects))
        for project in projects:
            if(project.get_attribute("class") == "RowItemsStyle" or project.get_attribute("class") == "RowStyle"):
                tds = project.find_elements_by_tag_name("td")#获取单挑项目行的所有信息
                #for td in tds:
                #    print(td.text)
                if tds[1].text not in projectDicts.keys():#如果当前遍历的项目不是需要更改的项目，直接跳过
                    continue
                name = tds[2].text.replace('（','(').split('(')[0].replace(' ','')#当前遍历项目的负责人
                if name not in projectLeaders:#如果当前遍历项目的负责人和需要更改项目的负责人不一致，直接跳过
                    continue

                project = projectDicts[tds[1].text]#当前需要更改的项目信息
                ddlIsComplete = rectificationState[project[3]]#是否整改完成
                dtbYuJiTime = project[2]#预计整改完成时间
                ddlZiChaJieGuo = reviewStatus[project[4]]#内部复查结果

                #进入编辑页面
                tds.pop().click()
                time.sleep(3)
                #print(len(driver.window_handles))
                for handle in driver.window_handles:
                    if handle != parent_window:
                        #print(driver.current_url)
                        driver.switch_to.window(handle)
                        #print(driver.current_url)
                        if ddlIsComplete != "": #是否整改完成
                            Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlIsComplete")).select_by_value(ddlIsComplete)
                        if ddlZiChaJieGuo != "": #内部复查结果
                            Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlZiChaJieGuo")).select_by_value(ddlZiChaJieGuo)
                        if dtbYuJiTime != "": #预计整改完成时间
                            driver.find_element_by_id("ctl00_ContentPlaceHolder1_dtbYuJiTime").clear()
                            driver.find_element_by_id("ctl00_ContentPlaceHolder1_dtbYuJiTime").send_keys(dtbYuJiTime)
                        #js = "var completeDate=document.getElementById('ctl00_ContentPlaceHolder1_dtbYuJiTime'); completeDate.value='"+completedate+"'"
                        #driver.execute_script(js)
                        driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnSave").click()
                        element = WebDriverWait(driver,20,2).until(EC.alert_is_present())#显示等待10s
                        element.accept()
                        driver.switch_to.window(parent_window)
                        print(tds[1].text+","+name)
                        #删除已经遍历的键
                        del projectDicts[tds[1].text]
finally:
    # newline:表示换行，默认情况下都是'\n'
    file = open('info.csv', 'w', encoding='GB2312', newline='')
    writer = csv.writer(file)
    writer.writerows(projectDicts.values())
    driver.quit()
    print("结束时间："+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
