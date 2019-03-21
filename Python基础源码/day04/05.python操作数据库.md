# python操作数据库
1. 首先检查自己的pip命令是否已经安装
2. 安装pymysql
3. 引入pymysql

` import pymysql `

4. 连接数据库

` con = pymysql.connect('localhost','root','123456')`

5.创建游标

`cur = con.cursor`

6.sql语句

 `sql = "create database Test character utf8"`
 
 `sql1 = "use Test"`
 
 `sql2 = "create table test1(sid int,sname char(20),sex int)`
 
 7.执行sql语句
 ```
 cur.execute(sql)
 con.execute(sql1)
 con.execute(sql2)
 ```
 8.提交事物
 
 ` con.commit()`
 
 9.切断连接
 
 `con.close()`
 
 
 
 
 
