'''
多任务 线程(重点) 协程
执行任务的时候每一个核同一时间只能执行一个任务
8核可以同时8个任务  真正的多任务
假设一个核心(同时)执行8个任务  这是并发

时间片轮转: cpu随机分配给每个任务(线程),让他们轮流执行,但是
因为cpu速度很快,给人的错觉好像是一起执行

'''
'''
1.进程:每一个运行起来的程序就可以称为一个进程
运行起来的程序包括(源代码,资源:内存,硬盘,摄像头)

2.一个进程中最少有一个线程

3.进程就是系统分配资源的一个基本单位

4.多进程:同时运行多个qq,每个进程的数据是分开的,不能共享

'''

'''
1.线程:一个进程运行起来之后一定有个东西去执行指令,执行指令的这个
东西可以离理解为一个线程

2.线程是系统调用资源的最小单位

3.多线程 可以理解成一个qq中打开多个聊天窗口,和多个人同时聊天
'''

'''
1.协程:  一个线程中可以添加多个任务,
核心实现:(线程如果遇到耗时操作就去执行其他任务)
协程相当于一个线程在函数之间跳转,占用资源非常少
切换速度快


'''

import time
import threading
'''
#要实现边唱边跳  使用多任务中的 多线程
def sing() :
    for i in range(5):
        time.sleep(0.5)
        print(i,"你唱的真好听")

def dance():
    for i in range(5):
        time.sleep(0.5)
        print(str(i)+"你跳的真好看")


if __name__ == '__main__':
    #创建一个子线程
    #创建一个子线程的目的是需要 执行其他的任务,
    # 函数名不能加(),如果传入()是调用了一个函数
    t1= threading.Thread(target=sing)
    t2= threading.Thread(target=dance)
    t1.start()
    t2.start()
    print("主线程执行完毕")
    for i in range(5):
        time.sleep(0.5)
        print("主线程执行")

#cpu会随机分配时间给3个线程去执行


'''


'''
参数问题 :如果函数需要传入参数,注意参数必须是一个元组args = (i,)
def sing(a) :
    print(a)
    for i in range(5):
        time.sleep(0.5)
        print(i,"你唱的真好听")

def dance(b):
    print(b)
    for i in range(5):
        time.sleep(0.5)
        print(str(i)+"你跳的真好看")


if __name__ == '__main__':
    #创建一个子线程
    #创建一个子线程的目的是需要 执行其他的任务,
    # 函数名不能加(),如果传入()是调用了一个函数
    t1= threading.Thread(target=sing,args=(5,))
    t2= threading.Thread(target=dance,args=(6,))
    t1.start()
    t2.start()
    print("主线程执行完毕")
'''





'''
主线程等待子进程结束join()
def sing(a) :
    print(a)
    for i in range(5):
        time.sleep(0.5)
        print(i,"你唱的真好听")

def dance(b):
    print(b)
    for i in range(5):
        time.sleep(0.5)
        print(str(i)+"你跳的真好看")


if __name__ == '__main__':
    #创建一个子线程
    #创建一个子线程的目的是需要 执行其他的任务,
    # 函数名不能加(),如果传入()是调用了一个函数
    t1= threading.Thread(target=sing,args=(5,))
    t2= threading.Thread(target=dance,args=(6,))
    t1.start()
    t2.start()
    t1.join()
    #设置主线程等待子线程结束后再结束
    # t1.join(n)参数是执行等待t1的时间,如果时间到了
    #t2还没执行完,也直接执行主线程
    t2.join(10)#如果参数时间大于线程执行时间,则会线程执行完毕就
    #执行主线程
    print("主线程执行完毕")
'''
'''
设置一个守护线程,主线程结束,所有子线程结束
def sing(a) :
    print(a)
    for i in range(5):
        time.sleep(0.5)
        print(i,"你唱的真好听")

def dance(b):
    print(b)
    for i in range(5):
        time.sleep(0.5)
        print(str(i)+"你跳的真好看")

if __name__ == '__main__':
    
    t1= threading.Thread(target=sing,args=(5,))
    t2= threading.Thread(target=dance,args=(6,))
    t1.setDaemon(True)
    t2.setDaemon(True)
    #↑这两句话需要放在start之前
    t1.start()
    t2.start()
    print("主线程执行完毕")
'''


'''
常用的函数跟方法



'''
'''
进程中的数据很多
线程中的数据很少,很多数据来自于进程中的
多个线程通信  可以通过全局变量
多个线程可以通过共享全局变量通信,因为这个全局变量是属于进程的
多线程的是一个进程中有多个变量
'''

'''
多线程共享全局变量问题
num = 0

def sum (a):
    global num
    for i in range(0,100):
       num = num + a
       num = num - a




if __name__ == '__main__':
    for i in range(10):

        t1 = threading.Thread(target=sum, args=(5,))
        t2 = threading.Thread(target=sum, args=(10,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(num)

'''

'''

使用同步锁 解决同步变量问题

'''
num = 0

def sum (a):
    global num
    lo.acquire()#枷锁,加了锁之后,只有一个线程进入锁里面
    #必须等这个锁释放后其他线程才能进入
    for i in range(0,10000000):
       num = num + a
       num = num - a
    lo.release()#释放锁,如果不释放其他线程不能进入



if __name__ == '__main__':
    lo = threading.Lock()
    for i in range(10):
        t1 = threading.Thread(target=sum, args=(5,))
        t2 = threading.Thread(target=sum, args=(10,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(num)
