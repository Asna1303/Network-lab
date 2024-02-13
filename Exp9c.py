
# Ceaser Cipher Client

import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('localhost',12346))
while True:
    message=input("Enter the message:")
    if message.lower()=='exit':
        break
    client_socket.sendall(message.encode())
    data=client_socket.recv(1024).decode()
    print("Received encrypted message:",data)
client_socket.close()


#OUTPUT

#Enter the message:Hello
#Received encrypted message: Khoor
