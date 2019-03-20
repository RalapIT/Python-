year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日："))

print("❤" * 20)
day += (month - 1) * 30
if month < 9:
    day += month // 2
else:
    day += (month + 1) // 2

if month > 2:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        day -= 1
    else:
        day -= 2
print(" " *9 ,"是%d的第%d天" %(year,day))
print("❤" * 20)
