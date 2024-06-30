import socket
s = socket.socket()
host = 'localhost'
port = 333

s.connect((host,port))

print(s.recv(1024).decode())
s.close()