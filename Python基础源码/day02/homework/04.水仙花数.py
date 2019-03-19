# 4. 求1000以内水仙花数: 如果一个3位数等于其各位数字的立方和,这个数就是水仙花数
for i in range(100,1000):
    a = int(i/100)
    b = int((i%100)/10)
    c = int((i%10))
    if a*a*a+b*b*b+c*c*c == i:
        print(i)

