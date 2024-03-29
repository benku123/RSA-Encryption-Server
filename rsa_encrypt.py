from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64

key = RSA.generate(2048)

private_key = key.export_key()
with open('private.pem', 'wb') as f:
    f.write(private_key)

public_key = key.publickey().export_key()
with open('public.pem', 'wb') as f:
    f.write(public_key)


print('> Encryption')

public_key = RSA.import_key(open('public.pem').read())
private_key = RSA.import_key(open('private.pem').read())

print(f'> Public key: {public_key}')
print(f'> Private key: {private_key}')


