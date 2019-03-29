
# 进程池子 Pool
# 进程数量固定切少的情况下不适用进程池,使用多进程

# 为什么要使用进程池: 程序在创建和销毁的时候会花费大量时间和资源,
# 减少进程的创建和销毁次数提高程序的执行效率

import multiprocessing
import os,time,random

def worker(msg):
    print("这是执行的任务")
    t_start = time.time()
    print("%s开始执行,进程号%d"%(msg,os.getpid()))
    time.sleep(1)
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕,耗时%0.2f"%(t_stop-t_start))


if __name__ == '__main__':
    po = multiprocessing.Pool(3)  # 创建一个进程池, 最多进程数量为3 注意: 使用的时候再创建

    for i in range(0,8):
        # 参数1: 要调用的目标, 参数二 传递给目标的参数元祖
        # 每次循环将会用空闲出来的子进程去调用目标
        print("循环体内")
        po.apply_async(worker,(i,))   # 添加任务时开始调用目标,  添加任务不会等到目标调用结束再继续添加, 任务就算没有结束,会先添加完,多余的任务排队
        # time.sleep(0.1)
    print("----开始-----")
    print("当前进程号:",os.getpid())  # 获取当前进程编号
    time.sleep(2)

    po.close() # 关闭进程池, 关闭后po不在接受新的请求

    time.sleep(2)
    print("========时间停止0.1========")
    po.join() # 等待po中所有子进程执行完成, 必须放在close之后
    print("----end----")







































