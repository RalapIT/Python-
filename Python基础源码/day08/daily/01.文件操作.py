'''
今日安排:
1.文本操作:读写文件内容
2.多任务多线程
3.进程 协程
'''
# li = [1,"xx",33,"sadf",4,"陈光"]
#文件操作 w:写,如果有文件就打开这个文件,没有就创建一个文件

# with open('aa.txt',"r",encoding="utf8") as f:
#     str1 = f.read()
# with open('TEST/bb.txt',"w",encoding="utf8") as f:
#       f.write(str1)
# #     print(f.readline())
# #     print(f.readline(6))
# #     print(f.readline(6))
# # #迭代器
# #     print(f.readlines())
#
#     print(f.read().splitlines())

#写入的内容不会自动换行,除非使用转义字符
#文件直接创建在项目文件夹中
#写入的内容会覆盖以前的内容
#写入的内容必须是字符串
#w 覆盖  追加
# 解决中文乱码的问题
# a 追加 r 打开文件 读取内容
#参数是表示读取几个字符,都会从上一次的位置接着读
#读出所有的内容.以列表的形式返回,每一行都是以个元素,每个元素后面都会跟\n
li=''
with open("git.jpg","rb") as f:
    li = f.read()
    print(li)

with open('TEST/git.jpg',"wb") as f :
    f.write(li)