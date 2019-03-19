# 控制结构

# a = 5
# b = 6
# if b > a :
#     print("对了")
# else:
#     print("错了")
# print("程序结束")

# if b < a :
#     print("错了")
# else :
#     print('对了')
# print("程序结束")


# num = input("请输入您的年龄:")
# # 转换他的类型
# if(num < "12") :
#     print("您还是一个孩子")
# elif ("13"<num<"60"):
#     print("缺钱真的不好受")
# else :
#     print("休息~")

# str1 = "abcderg"
# #for循环
# for i in str1 :
#     print(i)



#使用for循环输出 1到10
#range函数 它有参数 如果传入两个参数 第一个表示开始的位置 第二个表示结束的位置 左闭右开
#第三个参数是步长
# num = 0
# sum = 0
# print(range(10,101))
# for i in range(10,101):
#     sum = sum + i
# print(sum)

#100以内的奇数的和
# for i in range(1,100,2) :#第一个参数是闭的
#     print(i)

for i in range(0,-101,-1):
    print(i)
#跳出当前循环 break
#跳出本次循环 continue