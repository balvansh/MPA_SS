import socket
import getpass
from Crypto.Cipher import AES
import hashlib
def decrypt_file(key):
    key=hashlib.sha256(key.encode('utf-8')).digest()
    with open("/home/thbr/MPA_SS/kfl.enc","rb") as dta:
        IV=16 * '\x00'
        decryptor=AES.new(key,AES.MODE_CFB,IV)
        return(decryptor.decrypt(dta.read()))  
SERVER='127.0.0.1'
PORT=9909
key=getpass.getpass('Enter password: ')
#decrypt_file(key)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((SERVER,PORT))
s.send(decrypt_file(key))

#unencrypt data