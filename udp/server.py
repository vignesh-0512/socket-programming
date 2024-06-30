import socket
import datetime

s = socket.socket()
host = 'localhost'
port = 333

s.bind((host,port))

s.listen(1)

while True:
    c, addr = s.accept()
    print("got connection",addr)
    date = datetime.datetime.now()
    c.send(str(date).encode())
    c.close()
