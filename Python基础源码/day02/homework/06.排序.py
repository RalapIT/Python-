# 5. 对3 . 65 . 22 . 102 . 4  进行升序排序
arr = [3,65,22,102,4]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)
