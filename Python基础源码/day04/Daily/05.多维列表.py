多维列表
li = [1,5,6,(1,5,6,[1,{"aa":"bb"},67,8],6),3]
print(li[3][3][1]['aa'])
li[2][2][2]['bb'][1]

# 学生
# #学号 名字 年龄 性别 爱好
#  001  小明  18  男  玩球
#  002  小刚  18  男  玩球

#数据类型的转换
aa = '55'
print(int(aa))#转化成整数

bb = 55
print(type(str(bb)))

cc = "555"
print(list(cc))#列表
print(tuple(cc))#元组
# print(dict(cc))#字典
print(set(cc))#集合
