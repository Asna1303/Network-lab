
# Ceaser Cipher Server


import socket
def caesar_cipher(text,shift):
    encrypted_text=""
    for char in text:
        if char.isalpha():
            shifted=ord(char)+shift
            if char.islower():
                if shifted>ord('z'):
                    shifted-=26
                elif shifted<ord('a'):
                    shifted+=26
            elif char.isupper():
                if shifted>ord('Z'):
                    shifted-=26
                elif shifted<ord('A'):
                    shifted+=26
            encrypted_text+=chr(shifted)
        else:
            encrypted_text+=char
    return encrypted_text
def caesar_decipher(text,shift):
    return caesar_cipher(text,-shift)
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost',12346))
server_socket.listen(1)
print("Server is listening...")
conn, addr=server_socket.accept()
print(f"Connection from {addr}")
while True:
    data=conn.recv(1024).decode()
    if not data:
        break
    print("Received:",data)
    encrypted=caesar_cipher(data,3)
    print("Encrypted:",encrypted)
    decrypted=caesar_decipher(encrypted,3)
    print("Decrypted:",decrypted)
    conn.sendall(encrypted.encode())
conn.close()



#OUTPUT

#Server is listening...
#Connection from ('127.0.0.1', 56282)
#Received: Hello
#Encrypted: Khoor
#Decrypted: Hello
