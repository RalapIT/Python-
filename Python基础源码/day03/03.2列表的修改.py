
#改
# li[3] = "小米"

#删除
# for i in range(len(li)):
#     del li[0]
# print(li)
# li.clear()删除所有元素
# li.remove(2)#删除第一个匹配到的元素
# print(li)
#pop()
#默认删除最后一个,并且返回删除的内容

# print(li.pop(2))#传参后从左往右开始
# #队列 先进先出
# #查询
# print(li.index(8,2,6))#后面跟的两个参数 从哪个下标开始到哪个下标结束
# print(li)
# #计数
# print (li.count(2))

# 遍历
# for i in li :
#     print(i)
#     if i == 5 :
#         li.remove(i)
# print(li)
#
# # 排序:升序
# # li.sort()
# # li.sort()
# # li.reverse()#倒序
# li.sort(reverse=True)
# print(li)

li = [1,5,9,8,5,2,1]
li1 = li*3
print(li1)

# li1 = li.copy()
