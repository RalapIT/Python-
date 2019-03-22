import pymysql
con = pymysql.connect("localhost","root","123456")
cur = con.cursor()
con.commit()
def add (sid,sname,age):#向表中添加数据
    str1 = "insert into stu1 values "
    tu = (sid,sname,age)
    sql = str1 + str(tu)
    cur.execute(sql)
    con.commit()
def create1 (name):#创建数据库
    str1 = "create database "
    tu = name
    sql = str1 + tu
    cur.execute(sql)
    con.commit()
def use1 (name):#切换数据库
    str1 ="use "
    tu = name
    sql = str1 + tu
    cur.execute(sql)
    con.commit()
def del1 (name):#删除数据库
    str1 ="drop database "
    tu = str(name)
    sql = str1 + tu
    cur.execute(sql)
    con.commit()
def del2 (table1,id1):#删除一行
    str1 ="delete from "
    tu = str(table1)
    str2 = " where sid = "
    tu1 = str(id1)
    sql = str1 + tu +str2 + tu1
    cur.execute(sql)
    con.commit()

def delt (name):#删除表
    str1 ="drop table "
    tu = str(name)
    sql = str1 + tu
    cur.execute(sql)
    con.commit()
def up2 (tb1,num,num1):#修改数据
    str1 ="update "
    tu = str(tb1)
    str2 = " set "
    tu1 = str(num)
    str3 = " = "
    tu2 = str(num1)
    sql = str1 + tu +str2+tu1+str3+tu2
    cur.execute(sql)
    con.commit()
