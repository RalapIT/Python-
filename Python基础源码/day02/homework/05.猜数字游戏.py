import random
num2 = random.randint(1,999)
for i in range(10,0,-1):
    num = int(input("请输入一个数字:"))
    if(num < num2):
        print("小了")
    elif(num > num2):
        print("大了")
    else:
        print("正确")
        break