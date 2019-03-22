#函数/数据类型补充/迭代器/使用python操作数据库
#实现的一些功能的代码的集合
#js中 fuction函数名(参数){函数体}
#语法:关键字def 函数名 ():
#程序从上到下执行 函数必须要调用才会执行
# def sum(x):
# print(x*20)
# sum("❤")函数体内输出的,外面调用的人看不见
#函数的生命周期:调用的时候函数执行完毕,执行完毕后函数就销毁了
# def sum (a):
#     sum1 = 0
#     for i in range(a+1):
#         sum1 += i
#     return sum1
# print(sum(100))

# a = int(input("请输入数字"))
# b = int(input("请输入数字"))
# def sum (x,y):
#     sum1 = 0
#     for i in range(x,y):
#         sum1 += i
#     return sum1
# sum(a,b)

#全局变量和局部变量
#函数中的变量一般都是局部变量
#函数中有局部变量的时候,就不会使用到全局变量的c
#如果非要使用全局变量 就要使用global

# def test ():
#     print("1")
#     return "1"
# print(test()+"2")
from day04.函数工具包 import paixu
li = [3,7,9,4,10]
print(paixu(li))