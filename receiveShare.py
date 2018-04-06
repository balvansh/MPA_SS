'''
have to receive the share from VIS, then encrypt it
'''
from Crypto.Cipher import AES
import hashlib
IV = 16 * '\x00'           # Initialization vector: discussed later
mode = AES.MODE_CFB
key='alicelovesbob'
key=hashlib.sha256(key.encode('utf-8')).digest()
text=input("put some text here:")
encryptor = AES.new(key, mode, IV)
ciphertext = encryptor.encrypt(text)
with open("/home/thbr/MPA_SS/kfl.enc","wb") as dta:
    dta.write(ciphertext)    
