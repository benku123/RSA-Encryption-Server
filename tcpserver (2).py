import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5

host = '127.0.0.1'
port = 4444

#load public key
def encrypt_data(data):
    with open('public.pem', 'rb') as file:
        publicKey = RSA.importKey(file.read())
    cipher = Cipher_PKCS1_v1_5.new(publicKey)
    return cipher.ecdncrypt(data.encode())

#decrypt the message using private key
def decrypt_data(data):
    with open('private.pem', 'rb') as k:
        key = RSA.importKey(k.read())
    decipher = Cipher_PKCS1_v1_5.new(key)
    return decipher.decrypt(data, None).decode()

#get instance
server_socket = socket.socket()
server_socket.bind(('', port))

server_socket.listen(2)
print("Listening on port {}".format(port))

#accept new connection
connectionSocket, addr = server_socket.accept()
print('Connection from ' + str(addr))
connectionSocket.close()
print('Connection closed')

connectionSocket, addr = server_socket.accept()
print('Connection from ' + str(addr))

while True:
    message = connectionSocket.recv(1024)
    decrypted = decrypt_data(message)

    #if the message contains the . symbol, we received the file with extension
    if decrypted.find('.') != -1:
        #receiving the filename from the server
        file = open(decrypted, 'w')
        print('Received the filename {}'.format(decrypted))
        encrypted = encrypt_data('The filename {} received'.format(decrypted))
        connectionSocket.send(encrypted)

        #receiving the file data from the server
        data = connectionSocket.recv(1024)
        decoded = decrypt_data(data)
        print('Receiving the file data')
        file.write(decoded)
        file.write('to assure that the file has not been rewritten')
        print('The file data received successfully')
        file.close()

        sentence = 'The file data of {} received successfully!'.format(decrypted)
        encrypted = encrypt_data(sentence)
        connectionSocket.send(encrypted)

        sentence = input('Enter sentence: ')
        encrypted = encrypt_data(sentence)
        connectionSocket.send(encrypted)
    elif decrypted == 'bye':
        print('Client closed the connection')
        connectionSocket.close()
    else:
        print(decrypted)

        sentence = input('Enter sentence: ')
        encrypted = encrypt_data(sentence)
        connectionSocket.send(encrypted)


connectionSocket.close()

