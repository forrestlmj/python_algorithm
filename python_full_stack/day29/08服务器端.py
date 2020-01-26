import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8080))

phone.listen(5)
# 等链接
print('------->')
conn,addr=phone.accept()
print('------->')

msg = conn.recv(1024) #收消息

print('客户端发来的信息是：'+msg.decode('utf-8'))
conn.send(msg) # 发消息

conn.close()
phone.close()