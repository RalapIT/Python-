import pymysql

# 增删改

def get_con():
    con = pymysql.connect("localhost", "root", "123456")
    cur = con.cursor()
    return con, cur

def chang1(sql, con, cur, database="atm"):
    sql0 = "use " + database
    cur.execute(sql0)
    cur.execute(sql)

def chang(sql,database="atm"):
    con = pymysql.connect("localhost","root","123456")
    cur = con.cursor()
    sql0 = "use "+database
    cur.execute(sql0)
    cur.execute(sql)
    con.commit()
    con.close()

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

def regis(self):
    while True:
        print("请输入用户名:")
        username = input("用户名:")
        sql = "select username from woniu_atm where username = '%s'" % (username)
        source = py_select(sql, 0, "python")
        print(source)

        if len(source) == 0:
            # 没有查询到内容可以注册
            print("名字可以注册")
            print("请输入密码:")
            passwd = input("密码:")
            sql1 = "insert into woniu_atm (username,password) values ('%s','%s')" % (username, passwd)
            # 添加到数据库中
            chang(sql1, "python")  # 将数据插入到数据库中
            print("注册成功")
            return
        else:
            print("对不起: 名字已经存在")

def chang_money(username):  # 调用的时候需要存入用户名
    while True:
        print("请输入对方用户名")
        name = input("对方的用户名")
        sql = "select * from woniu_atm where username = '%s'" % (name)
        source = py_select(sql, 0, "python")
        print(source)
        if len(source) != 0:
            print("对方账户存在可以转账")
            print("请输入转账金额!")
            try:
                momey = float(input("金额:"))
                # 需要判断转账金额是否小于自己的余额
                # 查询余额
                sql1 = "select count from woniu_atm where username = '%s'" % (username)
                username_money = py_select(sql1, 0, "python")
                print(username_money)
                if momey <= username_money[0][0]:
                    print("请转账")
                    # 将自己的余额减少  将对方的余额增加
                    sql2 = "update woniu_atm set count = count - %f where username = '%s'" % (momey, username)
                    sql3 = "update woniu_atm set count = count + %f where username = '%s'" % (momey, name)

                    # 数据库异常处理  事务
                    con, cur = get_con()
                    sql0 = "use python"
                    try:
                        chang1(sql2, con, cur)
                        # 1/0
                        chang1(sql3, con, cur)
                    except Exception:
                        print("转账失败")
                        # 如果中途发生异常 应该回滚
                        con.rollback()
                    finally:
                        con.commit()
                        con.close()
                    return
                else:
                    print("对不起: 你的余额不足!")




            except Exception as e:
                print(e)
                print("请注意你的言辞")

        else:
            print("对方账户不存在,请输入正确的账户")






