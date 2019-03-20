#作业1
# str = " alex "
# str1 = str.replace(" ","")
# # str2 = str1.replace("l","p")
# # print(str1)
# # ls = str1.split("l") list列组
# # up  = str1.upper()
# # low = str1.lower()
# # print(low)
# print(str1[2])
# print(str1[0:4])
# print(str1[-1:-3:-1])
# print(str1.index("e"))

#作业2
# li = ['alex','eric','rain']
#
# li.append("seven")#改变原来的值
#
# li.insert(1,"tony")
# li[1]="Kelly"
# # del li[1]
# # li.remove("eric")
# # del li[2:5]
# # del li[3]
#
# li.sort()#直接改变原有顺序
#
# for i in range (len(li)) :
#     print(li[i],end="")
#     print(i)

#作业3
# li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
# li1 = li[2]
# li2 = li1[1]
# # print(li2[1])
# print(li1.index("all"))
# li1[2] = "ALL"
# print(li)


#作业3
# tu=("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44])
# #有序且可重复 不能增删改
# #不可修改
# #一个列表["age","name"]
# tu1 = tu[1]
# tu2 = tu1[2]
# tu2["k2"] ="seven"
# #元组类型 ,不可修改
# print(type(tu2["k3"]))


# #作业4
# dic={'k1':"v1","k2":"v2","k3":[11,22,33]}
# # for i,j in dic.items() :
# # for i in dic :
# #     print(dic[i]) 不要多想 就是这么简单那
# dic["k4"] = "kk"
# dic["k1"] = "alex"
# dic["k3"].append(44)
# dic["k3"].insert(0,1)
# print(dic)

#作业5
#使用while循环实现输出2-3+4-5+6.....+100的和
# i=1
# sum3 = 0
# sum1 = 0
# while True :
#     i+=1
#     if i < 101:
#         if i % 2 != 0:
#             sum3 = sum3 -i
#         else:
#             sum1 = sum1 + i
#         sum2 = sum1 + sum3
#         print(sum2)

res=0
count=2
while count <= 100:
    if count%2 == 1:
        res-=count
    else:
        res+=count
    count+=1
print(res)
