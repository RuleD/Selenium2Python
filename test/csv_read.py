import csv #导入csv包

#定义整改状态
rectificationState = {"无需整改":"0","已完成":"1","未完成":"2","开发已修复":"3","测试验证":"4","暂缓":"5"}
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

print(rectificationState.items())
print(projectDicts.items())
print(projectLeaders)