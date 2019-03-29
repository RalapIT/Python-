import socket
import threading
def sd ():
    while 1 :
        source = s.recv(1024).decode("utf8")
        print(source)

def accpet1():

    while 1:
        str = input(">>>>请输入")
        s.send(str.encode("utf8"))






if __name__ == '__main__':
    s = socket.socket()
    s.connect(("127.0.0.1", 555))
    print("链接成功")
    t1= threading.Thread(target=accpet1)
    t2= threading.Thread(target=sd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    s.close()