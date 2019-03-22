#迭代器
# iter() next
li=[1,2,3,4,5,6]

# 1.创建一个可迭代对象
i_li = iter(li)
# 2.取值,逐个取,可以记住上一次取值的位置
print(next(i_li))
print(next(i_li))
print(next(i_li))
print(next(i_li))

