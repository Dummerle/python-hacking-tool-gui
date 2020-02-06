import socket


class PortScanner():

    def scan(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((ip, port))
        if res == 0:
            sock.close()
            return True
        else:
            return False


