import pymysql

# 增删改

#这个函数专门用于获取连接和游标
def get_con():
    con = pymysql.connect("localhost","root","123456")
    cur = con.cursor()
    return con,cur


def chang1(sql,con,cur,database="python"):
    sql0 = "use "+database
    cur.execute(sql0)
    cur.execute(sql)



# 查
def py_select(sql,num=0,database="py_woniu19"):
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


