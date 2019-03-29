#1. 向某个文件中输入1万条数据
#2. 开启10个线程添加这1万条数据  对比他们之间的效率
import time
t = time.time()
with open("../TEST/bb.txt","w",encoding="utf8") as f:#这里的相对路径依然有用
    li = []
    for i in range(1000000):
        li.append('10000条数据\n')
        f.write(li[i])
t1 = time.time()
print(t1-t)

