import socket
import threading

class Servece:
    li = []
    def __init__(self):
        self.s = socket.socket()#创建一个socket对象
        self.s.bind(("127.0.0.8",555))#为socket对象绑定一个ip地址和端口号
        self.s.listen(5)
        print("服务器启动成功")
        self.accept1()
    def accept1(self):
        while 1:
            con,addr = self.s.accept()
            print("有人来了")
            self.li.append(con)
            t1 = threading.Thread(target=self.chat1,args=(con,))
            t1.start()
            print("主线程跟子线程开始工作>>>>")
    def chat1(self,con):
        con.send("用户名".encode("utf8"))
        name = con.recv(1024).decode("utf8")+":"

        while 1:
            source = con.recv(1024).decode("utf8")
            for i in self.li:
                i.send((name +source).encode("utf8"))




if __name__ == '__main__':
    a = Servece()