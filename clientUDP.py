import socket
host=socket.gethostname()
port=5700
udp_socket=socket.socket(type=socket.SOCK_DGRAM)
while True:
    message=input("-")
    if not message:
        break
    udp_client.sendto(msg.encode(),(host,port))
    print('Ready to recieve data')
    data,addr=udp_client.recvfrom(1024)
    if not data:
        break
    print('received',data.decode())
udp_client.close()
