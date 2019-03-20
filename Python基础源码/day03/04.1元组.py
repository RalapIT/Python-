#int float string list tuple set dictionary


#1.创建一个元祖
#和列表差不多,创建后其不可修改
#有序,且可重复
# tu = (4,5,9)
# print(type(tu))
# #元组依然可以切片
print(tu[3])
print(tu[-3])
print(tu[-2:-7:-2])
tu = ()
print(tu)
#注意如果一个元组中只有一个元素 需要在元素的后面添加一个逗号
#元组常用函数 len max min
# print(len(tu))
#增删改在这里都是非法操作
#可以删除整个元组
# print(tu.index(4))#查找该元素的下标
tu = (1,2,3,4,5,6,7,8)
for i in range(len(tu)-1,-1,-1):
    print(tu[i])
for i in range(-1,-len(tu)-1,-1):
    print(tu[i])