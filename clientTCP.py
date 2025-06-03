import socket
host=socket.gethostname()
port=3600
client_socket=socket.socket()
client_socket.connect((host,port))
message=input("-")
while message!=' ':
    client_socket.send(message.encode())
    dat=client_socket.recv(1024).decode()
    print('Recieved from server',dat)
    message=input('-')
client_socket.close()
