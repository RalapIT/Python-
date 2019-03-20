#set集合
#创建一个集合
# se1 = set()#小括号代表空集合
# print(type(se1))
#特点 : 不可重复,且无序,自动去重
#增删改查
# se.add("小泽玛利亚")#增加
# se1 = {2,9,4,7}
# li = [1,2,9,4]
# se.update(range(13))#将其他的数据更新到我们的集合中
# print(se)
#删除
#del se删除整个集合
#清空
# se.remove(5)#没有找到对应的内容就会报错
# se.discard(6)#删除指定的内容,如果没有找到也不会报错
# print(se)

#查
#我放弃查 我不查了

#遍历
se = {1,5,6,8,"ad"}
se1 = {1,5,6,9,10}
print(se.intersection(se1))
# print(se.union(se1))
# for i in se:
#     print(i)

