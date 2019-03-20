# 9. 输入一个数判断是否是质素，一个大于1的自然数，除了1和它本身外，
# 不能被其他自然数（质数）整除（2, 3, 5, 7等），换句话说就是该数除了1和它本身以外不再有其他的因数。
# 输出指定范围的质素
# num = int(input("请输入一个大于1的正整数"))
# flag = True
# for i in range(2,num):
#     if num % i == 0:
#         flag = False
# if flag:
#     print("这个是质数")
# else:
#     print("这个数不是质数")


x = int(input("请输入起点"))
y = int(input("请输入终点"))

for i in range(x,y+1):
    flag = True
    for j in range(2,i):
        if i % j == 0:
             flag = False
    if flag :
        print(i)




