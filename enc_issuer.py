import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5


# hostname and port number of encryption issuer
host = '127.0.0.1'
port = 8888

# create an instance
server_socket = socket.socket()
server_socket.bind(('', port))


while True:
    # listen for the incoming connections
    server_socket.listen(2)
    print("Listening on port {}".format(port))

    # accept new connection
    connectionSocket, addr = server_socket.accept()
    print('Connection from ' + str(addr))

    with open('public.pem', 'rb') as file:
        publicKey = RSA.importKey(file.read())
        connectionSocket.send(publicKey)
    #close the connection socket after sending the public key
    connectionSocket.close()