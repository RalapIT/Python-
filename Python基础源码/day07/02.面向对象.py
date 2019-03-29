# 什么是对象
#如何描述这个对象,但是是静态的
#对象还可以后动作:比如一个人可以做饭 睡觉
#在程序中需要描述这些动作,使用函数来表示

#创建一个类
# class person():
#     name = "人"
#     age =1
#     sex="男"
#     def eat(self):
#         print("吃饭了")
#     def walk(self):
#         print("走一个")
#     def cange_money(self,a,b):
#         print("转账")
#         return 2
#根据类来创建对象
# person1 = person()
# person2 = person()
#给对象的属性赋值
# person1.name ="qinins"
# person1.age = 20
# print(person1.name)
# print(person1.age)
# #调自己方法
# person1.cange_money(5,6)
# print(person1.cange_money(5,6))

# class person():
#     name = "人"
#     age =1
#     sex="男"
#     money = 100
#     def __init__(self,name,age,sex,money):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.money = money
#     def eat(self):
#         print("吃饭了")
#     def walk(self):
#         print("走一个")
#     def reduce(self):
#         self.money = self.money -5
#         return self.money
#     def add (self):
#         self.money = self.money +5
#         return self.money
#
#
#
# person1 = person("小明",20,"男",300)
# person2 = person("小明",20,"男",300)
# #实例化对象
# # person1 = person 实例化对象
# #构造方法
# #特点
#
# print(person1.reduce())
# print(person2.add())
'''
面向对象3大特征
1.封装 
2.继承
3.多态

'''
class person():
    name = "人"
    age = 1
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("吃饭了")
    def walk(self):
        print('走一个')
class sing():
    sname = "艺名"
    age = 20
    def __init__(self,name,age1):
        self.sname = name
        self.age1 = age1
    def sin(self):
        print("优美的歌声")
class stu(person,sing):
    sid = 1
    def __init__(self,sid,name,sname,age,age1):
        self.sid =sid
        # person.name = name
        # person.age = age
        person.name=name
        person.age = age
        sing.sname = sname
        sing.age1 = age1
    def study(self):
        print("学习")
    def eat(self):#对父类的方法的重写
        print("我在优雅的吃饭")

#实例一个对象
print(stu(1,"赵四","小王",18,19).sname)


#父类的方法满足不了我们的需求时  我们可以在子类中进行重写
#多继承
#self:代表调用方法的这个对象,对象调用自己的方法都会将字级传入进去
#多继承 ,对象访问自己的属性跟方法时,如果有,则访问自己的,如果没有自己没有,那从父类寻找,按照从左到右的顺序
#多态
#封装继承重写
#私有化属性
class stu():
    __sid = 100
    __age = 1

    def get_age(self):
        return self.__age
    def set_age(self,age):#对父类的方法的重写
        self.__age = age
stu1 = stu()

stu1.set_age(50)
print(stu1.get_age())