#字符串的切片

#按照字符串下标来取,下标从截取,左闭右开
# str1 = "abcdefghijk"
# print(str1[1:])
# print(str1[0:])
# print(str1[:5])
# print(str1[1::2])最后一个数字为步长.1不跨 ,2跨1,以此类推
# print(str1[:0:-1])#倒序输出
# print(str1[5:1:-1])
# print(str1[-1::-2])

#字符串常用的内建函数

#字符串的长度 len()
# print(len(str2))

#查找一个字符串是否在另一个字符中

# print(str2.find("b")) # 查询一个字符串在另一个串中第一次出现的位置
# print(str2.find("b"),n) #从下标为n的位置开始查找
# print(str2.find("b"),2,5) #从下标为2开始到下标为5之前的位置


#查询index  查询的是索引
# print(str2.index("b撒打算的撒")) #找不到时会报错

#输出一个固定长度的字符串
# print(str2.center(20,"*"))

#统计一个串在另一个串中出现的次数
# print(str2.count("bc"))
str2 = 'abc123123'
print(str2.count("bc",3,5))#从下标为3 查询bc出现的次数 输出0

#切割字符串  将参数删除 改成列表
print(str2.split("1"))
print(str2.split("1",2)) #第二个参数表示最多分割的次数

# 判断串是数字还是字母还是数字字母的组合
str2 = 'abc123123'
print(str2.isalnum())#是否为数字和字母组合,也可以全是数字,也可以全是字母
print(str2.isalpha())#是否为字母
print(str2.isnumeric())#是否为数字

#字母大小写转换
str3 = 'AZsxsaZD'
print(str3.lower())#小写
print(str3.upper())#大写

#判断是否全是大写字母还是全是小写
print(str3.isupper())#大写
print(str3.islower())#小写

#判断字符串是否以某个字串开头或结尾

print(str3.startswith("A"))#后面的参数代表从哪里开始  到哪里结束
print(str3.endswith("A",3,5))#判断某个字符串是否以某个字串结尾

#替换 将串中的某些内容替换成其他内容
str3 = 'AZ$____$aZD'
#print(str3.replace("$","****",n)); #将串中某些子串替换成其他子串 n代表最多替换几次
#没找到后不会替换跟报错
