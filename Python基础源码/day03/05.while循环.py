import random
num = random.randint(100,1000)

while True :
    num1 = int(input("请输入一个1000以内的整数"))
    if num > num1 :
        print("小了")
    elif num < num1 :
        print("兄弟大了")
    else:
        print("对了")
        break