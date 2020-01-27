from socket import *
ip_port = ('127.0,0,1',8080)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(backlog=back_log)
print('服务端开始运行了')
conn,addr = tcp_server.accept()
print('双向链接是',conn)
print('客户端地址',addr)

data = conn.recv(buffer_size)
print('客户端发来的信息是',data.decode('utf-8'))

conn.send(data.upper())
conn.close()
tcp_server.close()