传参:可变类型和不可变类型
a = 6#修改a的值,重新创建了一个对象,然后让a重新指向创建的对象
#a = 5#创建一个变量,然后让变量A 指向这个5
print(id(a))#返回参数的id
b = 5#a和b指向了同一个值
print(id(b))

#字符串不可变
c = "aa"
d = "aa"
print(id(c))
print(id(d))

#可变数据类型
#修改数据之后,数据id不变
li = [1,5,6,7,8,9]
print(id(li))
li.append(10)
print(id(li))

se = {1,2,3,5,6}
print(id(se))
se.add(9)
print(id(se))

dic = {'a':1,'b':2}
print(id(dic))
dic["c"]=3
print(id(dic))
#首先内存中创建了一个10,然后将var1指向10
#将var1作为参数传入的时候,形参a指向var1的指向位置10
# 如果函数中需要修改形参a.那么就是创建新的对象,然后修改a的指向
# def sum(a):
#     print("❤"*20)
#     print(a)
#     a.append(55)
#     return a
# li = [1,5,8,9,3]
# sum(li)
# print(li)#注意将可变数剧类型传入函数后,如果对其进行修改
#相当于操作了一个全局变量
# print(id(var1))
# sum(var1)
# print(var1)

参数 : 必须参数 关键字参数  默认值参数  不定长参数
#1.必须参数
# def sum(a,b) :
#     print("这是参数a",a)
#     print("这是参数b",b)
# sum(10,20)
#必须传参 而且参数的位置和数据类型是一一对应的关系

#2.关键字参数
# def sum(a,b) :
#     print("这是参数a",a)
#     print("这是参数b",b)
# sum(b=10,a=20)
#可以交换位置 必须传参  参数的个数不能少

#3.默认值参数
# def sum(a="❤",b='◎') :
#     print("这是参数a",a)
#     print("这是参数b",b)
# sum()
#可以少传  可以不传  或者都传 或者使用关键字  改变顺序传
#如果调用的时候传入了参数就就使用传入的参数,如果没有传入就使用默认值

#不定长参数
#可以使用*去接受多余参数
# def sum(a,b,*c) :
#     print('这是参数a',a)
#     print('这是参数b', b)
#     print(*c)
# sum(5,8,9,10,20,30)
#匿名函数
la = lambda x,y:[x+y,x*y]
print(la(5,6))
#函数后面点的表达式会自动给我们return回来
#只能返回一个值,但是这个值可以是一个表达式,如果需要返回多个表达式的值
#需要将他添加到列表,集合中

