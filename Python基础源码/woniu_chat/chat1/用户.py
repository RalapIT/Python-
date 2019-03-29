import socket



s = socket.socket()

s.connect(("127.0.0.2", 555))

source = s.recv(1024).decode("utf8")
print(source)
while 1:
    str = input(">>>>请输入")
    s.send(str.encode("utf8"))

print("链接成功")

s.close()
