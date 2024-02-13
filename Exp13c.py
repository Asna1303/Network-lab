

# MOD5HASH Client


import socket
def decrypt(encrypted_message):
    decrypted_message=''.join(chr(ord(char)-1) for char in encrypted_message)
    return decrypted_message
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port=12349
client_socket.connect((host,port))
md5_hash_received=client_socket.recv(1024).decode('utf-8')
print(f"MD5 hash received from server:{md5_hash_received}")
client_socket.close()


#OUTPUT

#MD5 hash received from server:9facad096fca1a5977393fdf1f6f7349

