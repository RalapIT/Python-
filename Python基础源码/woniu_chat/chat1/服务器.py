'''
#socket
#什么是socket 也叫套接字
作用: 在电脑之间  通过网络传输数据
socket 的本质其实就是两个进程之间的通信  他是通过网络来通信的
写一个服务器  接受客户端发送的消息
'''
import socket
#创建一个socket对象
s = socket.socket()
#给服务器绑定一个ip和端口号
s.bind(("127.0.0.1",555))
#设置监听 参数等待链接的最大值
s.listen(5)

#链接客户端
print("服务器已经启动,等待客户链接")

con,addr = s.accept()

print("全体注意,有人来了")

#客户端给用户发送消息
while 1 :
    str = input("请发送")
    con.send(str.encode("utf8"))
    aa = con.recv(1024).decode("utf8")
    print(aa)


con.close()
