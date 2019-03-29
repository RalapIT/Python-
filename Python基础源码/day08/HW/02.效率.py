# 开启10个线程添加这1万条数据  对比他们之间的效率
import time,threading
def file ():
    with open("../TEST/bb.txt","w",encoding="utf8") as f:#这里的相对路径依然有用
        li = []
        for i in range(1000000):
            li.append('10000条数据\n')
            f.write(li[i])

if __name__ == '__main__':
    t1 = float(time.time())
    for i in range(11):
        t = threading.Thread(target=file)
        t.start()
    t2 = float(time.time())
    print(t2-t1)


