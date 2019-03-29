
import time
import multiprocessing

# def test1():
#     while True:
#         print("函数1执行")
#         time.sleep(1)
#
#
# def test2():
#     while True:
#         print("函数2执行")
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     # 创建进程
#     p1 = multiprocessing.Process(target=test2)
#     p2 = multiprocessing.Process(target=test1)
#     p1.start()
#     p2.start()
#     print(p1.name) # 进程名字
#     print(p1.pid)
#     print(p2.name)
#     print("主进程执行完毕")



# 队列常用方法
# Queue.qsize()：返回当前队列包含的消息数量；
#
# Queue.empty()：如果队列为空，返回True，反之False ；
#
# Queue.full()：如果队列满了，返回True,反之False；
#
# Queue.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，
#
# Queue.get_nowait()：相当Queue.get(False)；
#
# Queue.put(item,[block[, timeout]])：将item消息写入队列，block默认值为True；



'''
# queue 队列  先进先出
# 栈: 先进后出

import multiprocessing
q = multiprocessing.Queue(3)  # 在内存中创建一个长度为3的队列对象
# q = multiprocessing.Queue()  # 如果不传参数则长度是变的
print(q)

q.put("111")  # 向队列中存放数据 , 如果队列满了会等着
q.put(22)
q.put([11,22,33])
q.put([11,22,33])
q.put([11,22,33])
q.put([11,22,33])

print(q.get())  #取值,  如果里面没有值之后,会一直等着

q.put([11,22,33])

print(q.full()) # 判断队列是否满了
print(q.empty()) # 判断队列是否为空
'''


'''
# 多进程之间通过Queue 来实现通信

import multiprocessing
def download_from_web(q):
    #模拟网上下载的数据
    data = [11,22,33,55]
    # 向队列中写入数据
    for temp in data:
        q.put(temp)
    print("下载器已经将下载的数据存入到队列中")


def analysis_data(q):
    #数据处理
    #问题来了 两个进程之间数据是不共享的, 需要共享需要使用队列
    source = []
    #从队列中获取数据
    while True:
        data = q.get()
        source.append(data)

        if q.empty(): # 如果队列中取完后退出
            break
        print(source)

def main():
    #1.  队列 在创建进程执行创建一个队列,
    q = multiprocessing.Queue()
    #2. 创建多个进程, 将队列的引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target=download_from_web,args=(q,))
    p2 = multiprocessing.Process(target=analysis_data,args=(q,))
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()

'''
'''
# Queue的使用  给队列存消息的问题

import multiprocessing
q = multiprocessing.Queue(2)
q.put("1")
q.put("2")

try:
    # q.put("消息4")  # 消息队列满的,会一直停在这里等待
    # q.put("消息4",True,2)  # 等待两秒, 如果消息队列还是满的则抛出异常
    q.put("消息",False) # 立即抛异常
    # q.put_nowait("消息队列已满会立即抛出异常") # 立即抛异常
except:
    print("消息队列已满,消息数量:%s"%(q.qsize()))
'''

'''
import multiprocessing
q = multiprocessing.Queue(2)
q.put("1")
q.put("2")

try:
    print(q.get())
    print(q.get())
    # print(q.get()) # 如果消息队列中没有了会一直等待知道读取到消息为止
    # print(q.get(False))  # 如果消息队列没有类容,会立即报错 等价于q.get_nowait()
    print(q.get_nowait())
except:
    print("消息队列读取问题")
'''
