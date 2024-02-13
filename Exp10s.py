
# DES Server


import socket
def decrypt(message,key):
    decrypted_message=""
    for char in message:
        if char.isalpha():
            shifted=ord(char)-key
            if char.isupper():
                decrypted_message+=chr((shifted-ord('A'))%26+ord('A'))
            else:
                decrypted_message+=chr((shifted-ord('a'))%26+ord('a'))
        else:
            decrypted_message+=char
    return decrypted_message
def start_server():
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('localhost',12345))
    server_socket.listen(1)
    print("Server is listening for incoming connections...")
    while True:
        conn, addr=server_socket.accept()
        print("Connection from",addr)
        encrypted_message=conn.recv(1024).decode('utf-8')
        key=int(input("Enter the decryption key:"))
        decrypted_message=decrypt(encrypted_message,key)
        print("Decrypted message:",decrypted_message)
        conn.close()
if __name__=="__main__":
    start_server()


#OUTPUT

#Server is listening for incoming connections...
#Connection from ('127.0.0.1', 50586)
#Enter the decryption key:3
#Decrypted message: Hello
