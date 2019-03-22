'''
可以直接调用的函数
'''
#求和的参数,参数是从哪里开始到哪里结束
# def sum(a,b):
#     su = 0
#     for i in range(a,b+1):
#         su += i
#     return su
def paixu (x):
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j]<x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    return x
