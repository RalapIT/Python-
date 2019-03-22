'''
输入用户名和密码
根据输入的用户名取数据库中查询相应的密码
判断是否查到了数据,如果没有查询到数据,说明用户名是错的,请重新输入
如果查询到了数据:说明用户名存在 在判断密码是否正确
如果密码正确 跳转到二级界面  如果密码错误 然后冲新输入登录名密码
'''
from day05.ATM.函数封装数据库操作代码 import *
def log():
    while True:
        print("请输入用户名和密码",end=",")
        print("如果需要退出>请输入quit")
        name = str(input("请输入您的用户名"))
        if name == "quit":
            break
        passwd = str(input("请输入您的密码"))
        #写sql 根据输入的的密码查询密码
        sql = "select password,money from admin where username ='%s'"%(name)
        pw = py_select(sql,0,"atm")
        if len(pw) == 0:
            print("用户名错误")
        elif pw[0][0] == passwd :
            print("登陆成功")
        else :
            print("密码错误")
