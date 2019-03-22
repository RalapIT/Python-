from day05.ATM.函数封装数据库操作代码 import *

def ui () :
    print("❤"*20)
    print("$"*9,"欢迎来到做梦银行","$"*9)
    print("❤"*20)
    while True :
        print("❤"*20)
        print("❤       请输入您需要的操作         ❤")
        print("❤1.登陆  ❤  2.注册   ❤   3.退出  ❤")
        num = str(input("请输入您的选择"))
        if num == "1":

           sorce =log()
           print(sorce)
           if sorce == 1:
               pass
           else:
               print("登录成功")
               while True:
                   print("请输入需要的操作: ")
                   print("1. 查询余额  2. 取钱   3. 存钱   4. 转账   5.返回主界面   6.退出系统")
                   str2 = str(input("请输入:"))
                   if str2 == "1":
                        print(py_select("select money from admin where username = '%s'"%(sorce),0)[0][0])
                   elif str2 == "2":
                      mon = input("请输入要取的金额:")
                      mon2 = py_select("select money from admin where username = '%s'" % (sorce), 0)[0][0]
                      chang("update admin set money = (%s-%s) where username = '%s'"%(mon2,mon,sorce))
                      el = int(mon2) - int(mon)
                      print("您现在的余额为%d"%(el))
                   elif str2 == "3":
                       mon = input("请输入要存的金额:")
                       mon2 = py_select("select money from admin where username = '%s'" % (sorce), 0)[0][0]
                       chang("update admin set money = (%s+%s) where username = '%s'" % (mon2, mon, sorce))
                       el = int(mon2) + int(mon)
                       print("您现在的余额为%d" % (el))
                   elif str2 == "4":
                        hu = str(input("请输入转账账户"))
                        pw = py_select("select * from admin where username = '%s'"%(hu))
                        if len(pw) == 0:
                             mon3 = int(input("您将转入外部账户,转入外账户的金额为:"))
                             el = py_select("select money from admin where username = '%s'" % (sorce), 0)[0][0]
                             el1 = int(el) - mon3
                             if el1 < 0 :
                                 print("???您现在没这些钱")
                             else:
                                 print("您现在的余额为%s" % (el1))
                        elif pw[0][0] == hu:
                            y1 = input("是否转入账户%s,确认请输入:'❤'"%(hu))
                            if y1 == "❤":
                                ai = int(input("请输入转账金额:"))
                                el = py_select("select money from admin where username = '%s'" % (sorce), 0)[0][0]
                                el2 = py_select("select money from admin where username = '%s'" % (hu), 0)[0][0]
                                chang("update admin set money = (%s+%s) where username = '%s'" % (ai, el2, hu))
                                el1 = int(el) - ai
                                if el1 < 0:
                                    print("???您现在没这些钱")
                                else:
                                    print("您现在的余额为%s" % (el1))
                            else:
                                print("爱心装填失败,无法转账❤")
                   elif str2 == "5":
                       print("返回主菜单")
                       break
                   elif str2 == "6":
                       print("退出系统")
                       exit()  # python提供的函数 ,退出这个应用
                   else:
                       print("输入有误,请从新输入")
        elif num == "2":
            sign ()
        elif num =="3" :
            print("退出")
            break
        else:
            print("您的输入有误,您还想做梦吗?")
if __name__ == '__main__':
    ui()



