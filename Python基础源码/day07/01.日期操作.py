'''
今天的安排;
1.时间的操作
2.包和模块
3.面向对象
'''
#时间操作
import time
#这个时间是一个时间戳,表示1970年1月1号1秒到现在的面数
# #这个东西是一个时间戳,表示1970年1月1号0:0:0到现在的参数
# print(time.time())
#
# print(time.asctime()) #当前时间,可视化时间
#
# print(time.localtime(10000000000.0))#时间元组,没有传参默认获取的就是当地时间
# #传入的参数类型是一个时间戳,将时间戳
# #
# # #输出一个可视化时间
# # print(time.asctime())#如果没有传入参数.默认返回当前时间(美式的)
# print(time.asctime(time.localtime(4553568150.949439)))#参数类型
#
# #输出一个习惯的格式
# # print(time.strftime("%Y-%m-%d %H:%M:%S"))#默认的是当前时间
# # #可以传入一个参数,时间元组,将时间元组转化成一个可视化时间
# str_time = "2019-3-26 11:20:30"
# print(time.strptime(str_time,'%Y-%m-%d %H:%M:%S'))#必须传参
# print(time.localtime())
#练习  算出1980年1月5号 15点20分 向前5天的一个日期#转化为时间元组
# a = (time.mktime(time.strptime(str_time,'%Y-%m-%d %H:%M:%S')))
# str_time = "2017-5-12 11:11:11"
# str_time1 = "2012-5-12 11:11:11"
# print(str((time.mktime(time.strptime(str_time,'%Y-%m-%d %H:%M:%S'))-time.mktime(time.strptime(str_time1,'%Y-%m-%d %H:%M:%S')))/60/60/24)+"天")#默认的是当前时间
# # # #可以传入一个参数,时间元组,将时间元组转化成一个可视化时间
# print(time.clock())#获取第一次使用的时间
# print(1)
# time.sleep(5)#堵塞
# print(1)
# print(time.clock())
#第二次使用的时候相当于第一次到第二次执行的时间间隔
str_time = "1997-06-30 11:11:11"
a =(time.mktime(time.localtime()))-time.mktime(time.strptime(str_time,'%Y-%m-%d %H:%M:%S'))
print(a/60/60/24//1)
