import socket
import sys


class PortScanner():
  
    def __init__(self):
        print("Portscanner Ready")
        
    def setRange(self, start,stop):
        self.rangeStart=start
        self.rangeStop=stop+1
   
    def scan(self,ip):
        try:
            for p in range(self.rangeStart, self.rangeStop):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = sock.connect_ex((ip, p))
                if res == 0:
                    print("Offene Verbindung in Port " + str(p))
                sock.close()
        except Exception:
            print("There was an error.")
            sys.exit()
        



    