
# RSA Client


import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('localhost',12347))
def encrypt(message,public_key):
    n,e=public_key
    encrypted_message=[(ord(char)**e) % n for char in message]
    return encrypted_message
public_key=(187,7)
while True:
    message=input("Enter the message:")
    if message.lower()=='exit':
        break
    encrypted=encrypt(message,public_key)
    encrypted_str=' '.join(map(str,encrypted))
    client_socket.sendall(encrypted_str.encode())
client_socket.close()


#Output

#Enter the message:Hello

