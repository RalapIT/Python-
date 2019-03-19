# 3. 输入三个整数, xyz, 将这三个数由小到大输出 (冒泡排序)
num1 = int(input("请输入一个整数"))
num2 = int(input("请输入一个整数"))
num3 = int(input("请输入一个整数"))
arr = [num1,num2,num3]
length = len(arr)
for i in range(length):
    for j in range(length-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)

