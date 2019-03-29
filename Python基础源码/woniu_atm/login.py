'''
这是登录模块

分析:
1. 输入用户名 和密码,
2. 根据输入的用户名去数据库中查旬相应的密码
3. 判断是否查到了数据, 如果没有查询到数据,说明用户名是错的, 请从新输入
4. 如果查询到了数据: 说明用户名存在,  在判断密码是否正确,
5. 如果密码正确, 跳转到二级界面
6. 如果密码错误, 提示,然后从新输入

'''

from woniu_atm.函数封装数据库操作代码 import *

def log():
    while True:
        print("亲,请输入用户名和密码!")
        print("如果需要退出:请输入quit")
        name = input("这里来输入用户名,兄弟:")
        if name == "quit":
            break
        password = input("这里来输入密码,兄弟:")
        #2.写sql 根据输入的用户名查询密码
        sql = "select password from woniu_atm where username ='%s'"%(name)

        pw = py_select(sql,0,"python")
        print(pw)

        if len(pw) == 0:   # 说明没有查询到数据, 也就是该用户不存在
            print("用户名错误")
        elif pw[0][0] == password:
            print("登录成功")
            return name

        else:
            print("密码错误,请从新输入!")



    return 1








