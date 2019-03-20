#字典 dict

#1.创建一个字典
#字典的每一个元素,都是由一个key和一个value组成的 键值
#键是唯一的,且键是不可改变的数据类型
#值可以是任意的 数据类型任意,且值可以重复\
#set的空集 为 set = set ()
#读取数据


# print(dic["aa"])
# print(dic.get("aa"))

#添加
# dic["dd"]="dd的值"
# #修改
# dic["aa"] = "aa修改后的值"
#删除整个字典
#dic.clear()
# for i in dic:
#     print(i+":"+dic[i])
# print(list(dic.keys()))
# keys =list(dic.keys())
# for i in keys:
#     print(i+":"+dic[i])

dic  = {"aa":"aa的值","bb":"bb的值","cc":"cc的值" }
for i,j in dic.items():
     print(i,j)