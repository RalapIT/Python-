#列表存储多个数据,相当于js中的数组
li = [1,5,9,8,2,1]#有序,且可重复,增删改查
li1 = []
print(type(li1))
print(li[2])
print(li[-2])
print(li[::-1])
print(li[1::3])
print(li[3::-2])
#调方法
#列表的常用函数
#1.长度
li = [1,5,9,8,2,1]
print(len(li))
#最大值
print(max(li))
#增加,插入的内容
li.append(56)
li.insert(len(li),55)
print(li)
#将一个列更新到另一个列表中,被更新的表会改变
li1 = [1,4,9]
li.extend(li1)
print(li+li1) #将两个列表合并成一个
print(li)
