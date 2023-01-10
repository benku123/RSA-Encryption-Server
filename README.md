# RSA Encryption Server

## Abstract
This code provides a simple implementation of a socket server that uses RSA encryption to secure data sent over the network. The server listens for incoming connections on a specified host and port and uses RSA encryption to encrypt and decrypt data sent over the socket.

## Introduction
This server demonstrates how to use the RSA encryption algorithm from the Pycryptodome library to encrypt and decrypt data sent over a socket. It uses the `Crypto` library for the encryption and decryption process. the code generates RSA keypair of 2048 bit and then exports the public key and private key to `public.pem` and `private.pem` respectively.

## How to run the code

This code requires python 3+ to be installed and the following libraries: `socket`, `Crypto`, `base64`. You can install them by running the command `pip install -r requirements.txt` on the command line.

To run the server, first make sure you are in the same directory as the `server.py` file, then execute the following command on the command line: 

You can also configure the server by modifying the values of the `host` and `port` variables at the beginning of the script.

## How to use

1. Run the code and it will display the listening on a specific port.
2. Use a client to connect to the server and send data.
3. The server will use the public key to encrypt the data before sending it back to the client.
4. Similarly, when it receives the data from the client, it uses the private key to decrypt the received data.
5. The code also provides the functionality of sending files over the network.

## Requirements
- Python 3+
- socket library
- Pycryptodome library

## Note

Please note that the code is for demonstration purposes only and is not suitable for use in a production environment as it does not include proper error handling or security measures.

