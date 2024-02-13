
# SUBST Client


import socket
def start_client():
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='127.0.0.1'
    port=12344
    client_socket.connect((host,port))
    message=input("Enter the message to be encrypted:")
    print(f"Original message:{message}")
    client_socket.send(message.encode('utf-8'))
    encrypted_message=client_socket.recv(1024).decode('utf-8')
    print(f"Encrypted message:{encrypted_message}")
    client_socket.close()
if __name__=="__main__":
    start_client()


#OUTPUT

#Enter the message to be encrypted:Hello
#Original message:Hello
#Encrypted message:Lipps

