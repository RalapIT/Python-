import socket
import threading

class Servece :
    li = []
    def __init__(self):#初始化服务器对象
        self.s = socket.socket()
        self.s.bind(("127.0.0.5", 555))
        self.s.listen(5)
        print("等待客户联机")
        self.accpe1()
    def accpe1(self):
        con,addr = self.s.accept()#等待用户链接
        print("有人来了")
        self.li.append(con) #将连接上的用户保存到列表里
        t1 = threading.Thread(target=self.chat,args=con)
        t1.start()
        print("主线程继续杰克,子线程已经可以和用户聊天")
    def chat(self,con):#实现和客户聊天功能
        con.send("链接成功".encode("utf8"))





if __name__ == '__main__':
    a = Servece()
