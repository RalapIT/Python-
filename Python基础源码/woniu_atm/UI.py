'''
这是蜗牛取款机的主界面
'''

from woniu_atm.login import log
from woniu_atm.register import regis
from woniu_atm.转账 import chang_money
def ui():
    print("===================================================")
    print("***********欢迎来到蜗牛我限制取款机*******************")
    print("===================================================")
    while True:
        print("请选择您需要的操作:")
        print("1. 登录      2. 注册      3. 退出")

        str = input("请输入:")

        if str == "1":
            print("登录")
            # 调用登录函数
            source = log()

            if source == 1:
                pass
            else:
                # 登录成功 ,进入二级界面
                print("登录成功")
                while True:
                    print("请输入需要的操作: ")
                    print("1. 查询余额  2. 取钱   3. 存钱   4. 转账   5.返回主界面   6.退出系统")
                    str2 = input("请输入:")
                    if str2 == "1":
                        print("查询余额")
                    elif str2 == "2":
                        print("取钱")
                    elif str2 == "3":
                        print("存钱")
                    elif str2 == "4":
                        chang_money(source)  # source 是登录后的用户名
                        print("转账")
                    elif str2 == "5":

                        print("返回主菜单")
                        break
                    elif str2 == "6":
                        print("退出系统")
                        exit()   # python提供的函数 ,退出这个应用
                    else:
                        print("输入有误,请从新输入")

        elif str == "2":
            print("注册")
            # 调用注册模块
            regis()

        elif str == "3":
            print("退出")
            break
        else:
            print("大兄弟,输入有误,请从新输入!")




if __name__ == '__main__':
    ui()



































