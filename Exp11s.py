
# RSA Server


import socket
def decrypt(encrypted_message,private_key):
    n,d=private_key
    decrypted_message=[chr(pow(int(char),d,n)) for char in encrypted_message]
    return ''.join(decrypted_message)
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost',12347))
server_socket.listen(1)
print("Server is listening...")
conn,addr=server_socket.accept()
print(f"Connection from {addr}")
private_key=(187,23)
while True:
    data=conn.recv(1024).decode()
    if not data:
        break
    print("Received:",data)
    encrypted=[int(char) for char in data.split()]
    decrypted=decrypt(encrypted,private_key)
    print("Decrypted:",decrypted)
conn.close()


#OUTPUT

#Server is listening...
#Connection from ('127.0.0.1', 53198)
#Received: 30 84 48 48 155
#Decrypted: Hello
