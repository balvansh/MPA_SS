import socket
import time
from threading import Thread
from socketserver import ThreadingMixIn

class clientSentShare(Thread):
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip=ip
        self.port=port

    def run(self):
        data=conn.recv(1024)
        print(data,port)

ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
threads=[]  #no idea why this is there!
ss.bind(('127.0.0.1',9909))
ss.listen(10)
t_end=time.time()+60*5
while time.time()<t_end:    #socket closes in 5 minutes
    (conn,(ip,port))=ss.accept()
    newthread=clientSentShare(ip,port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()    
    