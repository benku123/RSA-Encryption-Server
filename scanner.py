import pyfiglet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from base64 import b64encode, b64decode
import socket
import urllib.request
import json
from datetime import datetime
import rsa

#target = input('Enter the target ip: ')
target = '127.0.0.1'

#load public key
def encrypt_data(data):
    with open('public.pem', 'rb') as file:
        publicKey = RSA.importKey(file.read())
    cipher = Cipher_PKCS1_v1_5.new(publicKey)
    return cipher.encrypt(data.encode())

#decrypt the message using private key
def decrypt_data(data):
    with open('private.pem', 'rb') as k:
        key = RSA.importKey(k.read())
    decipher = Cipher_PKCS1_v1_5.new(key)
    return decipher.decrypt(data, None).decode()

# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)


#get information about ip-address
print('Information about target: ')
data = urllib.request.urlopen('https://ipapi.co/json/').read().decode('utf8')
json_data = json.loads(data)
country_name = json_data['country_name']
city = json_data['city']
print('Country: ' + country_name)
print('City: ' + city)


for port in range(1, 65535):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(100)

        # returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print("{} is open".format(port))

        s.close()
    except:
        print('The error occurred')


port = int(input('Which port do you want to connect to? \n -> '))

clientSocket = socket.socket()
clientSocket.connect((target, port))

#anchor to close the connection
a = 0

while a == 0:
    choice = int(input('To send the message choose 1 \nTo send the file choose 2 \nTo quit enter "bye"): '))
    if choice == 1:
        message = input('Enter the message: ')
        if message != 'bye':
            encrypted = encrypt_data(message)
            clientSocket.send(encrypted)  # .encode())
            print('Waiting for the response...')

            sentence = clientSocket.recv(1024)
            decrypted = decrypt_data(sentence)
            print(decrypted)
        elif message == 'bye':
            encrypted = encrypt_data(message)
            clientSocket.send(encrypted)
            print('Connection closed')
            a = 1

    elif choice == 2:
        name = input('Enter the name of the file: ')
        file = open('{}'.format(name), 'r')
        data = file.read()

        # sending the filename to the server
        encrypted_name = encrypt_data(name)
        clientSocket.send(encrypted_name)
        print('File name was sent')
        msg = clientSocket.recv(1024)
        decrypted = decrypt_data(msg)
        print(f'[SERVER]: {decrypted}')

        # sending the file data to the server
        encrypted_data = encrypt_data(data)
        clientSocket.send(encrypted_data)
        msg = clientSocket.recv(1024)
        decrypted = decrypt_data(msg)
        print(f'[SERVER]: {decrypted}')

        # close the file
        file.close()

        print('Waiting for the response...')

        sentence = clientSocket.recv(1024)
        decrypted = decrypt_data(sentence)
        print(decrypted)