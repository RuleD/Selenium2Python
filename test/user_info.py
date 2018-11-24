user_info = open('user_info.txt','r')
lines=user_info.readlines()
user_info.close()

for line in lines:
    username = line.split(',')[0]
    password = line.split(',')[1]
    print(username,password)
rectificationState = {"1":"0","已完成":"1","未完成":"2","开发已修复":"3","测试验证":"4","暂缓":"5"}
for i in range(4):
    if str(i) not in rectificationState.keys():
        continue
    print("获取总页数："+i)
name = "王菊(新点软件 - 研发群 - 电子交易产品研发群 - 评标研发2部);"   
name1 = "戴健（评标研发2部）(新点软件 - 研发群 - 电子交易产品研发群 - 评标研发2部);" 
print(name.split('(')[0])
print(name1.replace('（','(').split('(')[0].replace(' ',''))