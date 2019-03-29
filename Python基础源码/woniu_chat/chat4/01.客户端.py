import socket
import threading
class server() :
    s = ""
    def __init__(self):
        self.s = socket.socket()
        self.s.connect(("127.0.0.8", 555))
        #开启子线程
        t1 =threading.Thread(target=self.send)
        t1.start()
        self.rev()

    def send(self):
        while 1:
            print("输入quit退出")
            a =input("请输入")
            if a == 'quit':
                break
            else :
                self.s.send(a.encode("utf8"))

    def rev(self):
        while 1:
            source = self.s.recv(1024).decode("utf8")
            print(source)







if __name__ == '__main__':
    a = server()


