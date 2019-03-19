#7 . 抓球问题， 5个红球， 8个黑球，7个白球， 随机取出10个， 且白球不少于2个黑球不大于3个， 计数可能的颜色组合
count=0
for r in range(0,6):
    for b in range(0,9):
        for w in range(0,8):
            if r+b+w ==10 and w>=2 and b<3:
                print(r,b,w)
                count+=1
print(count)