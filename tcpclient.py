import socket

serverName = '192.168.200.186'
serverPort = 4444

clientSocket = socket.socket()
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('Enter sentence: ')
    clientSocket.send(sentence.encode())

    modifiedSentence = clientSocket.recv(1024).decode()
    if modifiedSentence == '':
        while modifiedSentence == '':
            sentence = input('Enter sentence: ')
            clientSocket.send(sentence.encode())
            modifiedSentence = clientSocket.recv(1024).decode()
    print('From server: ', modifiedSentence)

clientSocket.close()

