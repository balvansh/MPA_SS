import socket
from threading import Thread
from socketserver import ThreadingMixIn
shares=[]
class clientSentShare(Thread):
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip=ip
        self.port=port

    def run(self):
        data=conn.recv(1024)
        print(data,port,type(data))
        conn.send(b'Share has been shared')
        conn.close()
        shares.append([data[:5],data[5:]]) #assuming that the id is 5 digits long
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
threads=[]  #no idea why this is there!
ss.bind(('127.0.0.1',9909))
ss.listen(10)
#TODO: check HOW timeout works
ss.settimeout(5)    #socket closes in 5 minutes
try:
    while True:    
        (conn,(ip,port))=ss.accept()
        newthread=clientSentShare(ip,port)
        newthread.start()
        threads.append(newthread)
except socket.timeout:
    print("Timed out!")

for t in threads:
    t.join()

print(shares)
#TODO :take shares and perform the regeneration
    