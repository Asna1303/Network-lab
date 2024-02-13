
# MOD5HASH Server


import socket
import hashlib
def encrypt(message):
    encrypted_message=''.join(chr(ord(char)+1) for char in message)
    return encrypted_message
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port=12349
server_socket.bind((host,port))
server_socket.listen(5)
print(f"Server listening on {host}:{port}")
client_socket,addr=server_socket.accept()
print(f"Connection from {addr}")
message_to_send=input("Enter the message:")
encrypted_message=encrypt(message_to_send)
md5_hash=hashlib.md5(encrypted_message.encode('utf-8')).hexdigest()
print(f"Original message:{message_to_send}")
print(f"Encrypted message:{encrypted_message}")
print(f"MD5 hash of encrypted message:{md5_hash}")
client_socket.send(md5_hash.encode('utf-8'))
client_socket.close()


#OUTPUT

#Server listening on 127.0.0.1:12349
#Connection from ('127.0.0.1', 36562)
#Enter the message:Hello
#Original message:Hello
#Encrypted message:Ifmmp
#MD5 hash of encrypted message:9facad096fca1a5977393fdf1f6f7349
