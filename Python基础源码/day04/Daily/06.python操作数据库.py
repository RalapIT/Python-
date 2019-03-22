import pymysql
# # 1.连接上数据库
# con = pymysql.connect('localhost','root','123456')
# #2.创建一个游标,游标可以操作数据库 执行数据库命令
# cur = con.cursor()
# #3.通过SQL语句操作数据库
# #创建一个数据库
# sql = "create database py_test"
# #执行数据库
# cur.execute(sql)
# #提交事物
# con.commit()
# #关闭连接
# con.close()
#建立一个连接
con = pymysql.connect("localhost","root","123456")
#建立一个游标
cur = con.cursor()
#写sql语句
sql = "use py_woniu19"
sql1 = "create table stu1(sid int,sname char(20),age int)"
cur.execute(sql)
cur.execute(sql1)#每执行一个sql语句 都要给sql建立一个新的变量
#提交事物
con.commit()
#关闭连接
con.close()