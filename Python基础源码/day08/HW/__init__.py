
# 使用面向对象:思想写一个 猜拳游戏
#
# 对象
# 	属性: 存储比分
# 	方法: 对比 输赢


class Game() :
    score = 0
    def __init__(self,score=0):
        self.score = score
    def gm (self) :
        rule = {"剪刀":1,"锤头":0,"布":2}
        n = 0
        while n <10:
            try:
                for i in rule :
                    a = rule[i]
                    str = input("请出拳(剪刀,锤头,布)")
                    b = rule[str]

                    if  b == 1 and a == 2 :
                        self.score += 1
                        print('对方出的是'+i)
                        print("YOU WIN~")
                        print("您现在的分数是%s"%(self.score))
                    elif b == 1 and a == 1 :
                        print("平局")
                    elif b == 0 and a == 1:
                        self.score += 1
                        print('对方出的是' + i)
                        print("YOU WIN~")
                        print("您现在的分数是%s" % (self.score))
                    elif b == 0 and a == 0 :
                        print("平局")
                    elif b == 2 and a == 0 :
                        self.score += 1
                        print('对方出的是' + i)
                        print("YOU WIN~")
                        print("您现在的分数是%s" % (self.score))
                    elif b == 2 and a == 2 :
                        print("平局")
                    else:
                        self.score -= 1
                        print('对方出的是' + i)
                        print("YOU LOST~")
            except Exception as reason :
                        print("您的输入有误" ,end = " ")
                        print(reason)
                        print("不符合规则")
            n+=1

