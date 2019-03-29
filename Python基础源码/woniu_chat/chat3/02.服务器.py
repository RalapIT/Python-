import socket
import threading
class Socket():
    def __init__(self):
        self.li = []
    def accpet(self):
        self.s = socket.socket()

        print("服务器已经启动,等待客户链接")
        self.s.listen(5)
        self.con, self.addr = self.s.accept()
        self.li.append(self.con)


    def sr(self):
        while True:
            for i in self.li:
                self.source = i.recv(1024).decode("utf8")
                for j in self.li:
                    j.send(self.source.encode("utf8"))








if __name__ == '__main__':
    a = Socket()
    t0 = threading.Thread(target=a.accpet())
    t0.start()
    t1 = threading.Thread(target=a.sr)
    t1.start()


