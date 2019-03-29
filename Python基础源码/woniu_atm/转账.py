'''
这是转账模块:

转账之前的登录,  从登录后 调用转账模块需要 传入用户名


1.  输入转入对象
2.  查看这个对象是否存在, 且不能是自己
3.  如果对象存在, 请输入转账金额
4.  查询自己的余额是否大于等于转账的金额
5.  如果钱够 就实现转账功能,
6.  减去自己的余额,  增加对方的余额
7.  然后返回
'''

from woniu_atm.函数封装数据库操作代码 import *

def  chang_money(username):   # 调用的时候需要存入用户名
    while True:
        print("请输入对方用户名")
        name = input("对方的用户名")



        sql = "select * from woniu_atm where username = '%s'"%(name)
        source = py_select(sql,0,"python")
        print(source)
        if len(source) != 0:
            print("对方账户存在可以转账")
            print("请输入转账金额!")

            try:
                momey = float(input("金额:"))
                # 需要判断转账金额是否小于自己的余额
                # 查询余额
                sql1 = "select count from woniu_atm where username = '%s'"%(username)
                username_money = py_select(sql1,0,"python")
                print(username_money)

                if momey  <= username_money[0][0]:
                    print("请转账")
                    # 将自己的余额减少  将对方的余额增加
                    sql2 = "update woniu_atm set count = count - %f where username = '%s'"%(momey,username)
                    sql3 = "update woniu_atm set count = count + %f where username = '%s'"%(momey,name)
                    chang(sql2,"python")
                    # 1/0  # 使用同一个游标执行这两句sql
                    chang(sql3,"python")
                    print("转账成功")
                    return
                else:
                    print("对不起: 你的余额不足!")




            except Exception as e:
                print(e)
                print("请注意你的言辞")



        else:
            print("对方账户不存在,请输入正确的账户")


chang_money("aa")


























