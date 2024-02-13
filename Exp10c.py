
# DES Client


import socket
def encrypt(message,key):
    encrypted_message=""
    for char in message:
        if char.isalpha():
            shifted=ord(char)+key
            if char.isupper():
                encrypted_message+=chr((shifted-ord('A'))%26+ord('A'))
            else:
                encrypted_message+=chr((shifted-ord('a'))%26+ord('a'))
        else:
            encrypted_message+=char
    return encrypted_message
def start_client():
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(('localhost',12345))
    user_message=input("Enter the message to encrypt:")
    encryption_key=int(input("Enter the encryption key:"))
    encrypted_message=encrypt(user_message,encryption_key)
    print("Encrypted message:",encrypted_message)
    client_socket.send(encrypted_message.encode('utf-8'))
    client_socket.close()
if __name__=="__main__":
    start_client()


#OUTPUT

#Enter the message to encrypt:Hello
#Enter the encryption key:3
#Encrypted message: Khoor
