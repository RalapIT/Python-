import pymysql

# 增删改

def chang(sql,database="atm"):
    con = pymysql.connect("localhost","root","123456")
    cur = con.cursor()
    sql0 = "use "+database
    cur.execute(sql0)
    cur.execute(sql)
    con.commit()
    con.close()
    return
# chang("insert into admin values ('王五','123456','123456','123456')")

# 查
def py_select(sql,num=0,database="atm"):
    con = pymysql.connect("localhost","root","123456")
    cur = con.cursor()
    sql0 = "use "+database
    cur.execute(sql0)
    cur.execute(sql)
    if num == 0:
        source = cur.fetchall()
    else:
        source = cur.fetchmany(num)
    con.commit()
    con.close()
    return source  # 将查询的结果放回给调用者

from day05.ATM.函数封装数据库操作代码 import *
def log():#登陆用户
    while True:
        print("请输入用户名和密码",end=",")
        print("如果需要退出>请输入quit")
        name = str(input("请输入您的用户名"))
        if name == "quit":
            break
        passwd = str(input("请输入您的密码"))
        #写sql 根据输入的的密码查询密码
        sql = "select password from admin where username ='%s'"%(name)
        pw = py_select(sql,0,"atm")
        if len(pw) == 0:
            print("用户名错误")
        elif pw[0][0] == passwd :
            return name
        else :
            print("密码错误")
    return 1
#####注册用户
def sign (database="atm"):
    con = pymysql.connect("localhost", "root", "123456")
    cur = con.cursor()
    sql0 = "use " + database
    cur.execute(sql0)
    print("欢迎注册我行用户哟~")
    ad = input("请输入账户名")
    sql = "select * from admin where username ='%s'" % (ad)
    pw = py_select(sql, 0, "atm")
    if len(pw) == 0:
        passwd = input('请输入你的密码')
        no = input("请输入手机号")
        sql1 = "insert into admin values('%s','%s','%s','0')"%(ad,passwd,no)
        cur.execute(sql1)
        con.commit()
        print("添加成功")
    elif pw[0][0] == ad:
        print("用户已注册")
###存钱
def add1 (database="atm"):
    con = pymysql.connect("localhost","root","123456")
    cur = con.cursor()
    sql0 = "use "+database
    cur.execute(sql0)
    mon = input("请输入要取的金额:")
    mon2 = py_select("select money from admin where username = '%s'" % (sorce), 0)[0][0]
    sql="update admin set money = (%s-%s) where username = '%s'"%(mon2,mon,sorce)
    cur.execute(sql)
    el = int(mon2) - int(mon)
    print("您现在的余额为%d" % (el))
    con.commit()

# add1()


