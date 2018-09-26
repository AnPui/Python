from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',8888))
f=open('send.jpg','rb')
while True:
    data=f.read(1024)
    if not data:
        break
    s.send(data)
f.close()
s.close()