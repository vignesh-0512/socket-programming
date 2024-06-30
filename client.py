import socket
tcp_socket = socket.create_connection(('localhost',30))
try:
    while True:
        text = input("Enter any text:")
        data = str.encode(text)
        tcp_socket.sendall(data)
    
finally:
    tcp_socket.close()
