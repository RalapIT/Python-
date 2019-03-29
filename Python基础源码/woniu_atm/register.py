'''
注册模块
1. 然后用户输入需要注册的用户名
2. 去数据库中查询这个用户名是否可用
3. 如果存在, 提示然后从新输入
4. 如果不存在, 继续让用户输入密码等其他信息
5. 保存到数据库中
'''

from woniu_atm.函数封装数据库操作代码 import *

def regis():
    while True:
        print("请输入用户名:")
        username = input("用户名:")
        sql = "select username from woniu_atm where username = '%s'"%(username)
        source = py_select(sql,0,"python")
        print(source)

        if len(source) ==  0:
            # 没有查询到内容可以注册
            print("名字可以注册")
            print("请输入密码:")
            passwd = input("密码:")
            sql1 = "insert into woniu_atm (username,password) values ('%s','%s')"%(username,passwd)
            # 添加到数据库中
            chang(sql1,"python")  # 将数据插入到数据库中
            print("注册成功")
            return
        else:
            print("对不起: 名字已经存在")

























