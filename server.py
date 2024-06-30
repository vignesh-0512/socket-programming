import socket
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = ('localhost',30)
tcp_socket.bind(address)
tcp_socket.listen(1)
while True:
    print('waiting for connection...')
    connection,client = tcp_socket.accept()
    try:
        print("Connected to ip:{}".format(client))
        while True:
            data = connection.recv(32)
            print("received data:"(data))
            if not data:
                break
    finally:
        connection.close()
