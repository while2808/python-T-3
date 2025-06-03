import socket 
host=socket.gethostname()
port=3600
server_socket=socket.socket()
server_socket.bind((host,port))
server_socket.listen()
conn,addr=server_socket.accept()
print('connection from',str(addr))
while True:
    data=conn.recv(1024).decode()
    if not data:
        break
    print(data)
    data=input("-")
    conn.send(data.encode())
conn.close()
