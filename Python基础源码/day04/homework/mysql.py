#引用数据库
import pymysql
#连接mysql
con = pymysql.connect("localhost","root","123456")
#建立游标
cur = con.cursor()
#sql语句
# sql = "create database pymysql character set  utf8"
sql = "use pymysql"
# sql1 = "create table stu (sid int primary key,sname char(20),ssex int)"
# sql2 = "create table student (sid int,cid int,score int)"
# sql1 = 'insert into stu values ("02","李四","1"),("03","王五","1"),("01","王二麻子","1")'
# sql1 = 'insert into stu value ("04","阿呆","1")'
# sql1 = 'alter table student  add foreign key (sid)  references stu (sid)'
# sql1 = 'alter table student rename student1'修改表名
# sql1 = 'alter table student1 add column address char(20) '增加表名
# sql1 = 'update student1 set address="潍坊" where sid = "3"'
sql1 = 'delete from stu where sid="04"'
#执行sql语句
cur.execute(sql)
cur.execute(sql1)
#提交事件
con.commit()
#关闭连接
con.close()