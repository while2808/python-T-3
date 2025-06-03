import socket
host=socket.gethostname()
port=5700
udp_server=socket.socket(type=socket.SOCK_DGRAM)
udp_server.bind((host,port))
while True:
    print('waiting for message')
    data,addr=udp_server.resvform(1024)
    print('recieved',data.decode(),'from',addr)
udp_server.close()
