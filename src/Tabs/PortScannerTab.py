import time

from PyQt5.Qt import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal

from src.Tools.PortScanner import PortScanner
from src.other.Console import Console


class PortScanThread(QThread):
    portadd = pyqtSignal(str)

    def __init__(self, args, parent=None):
        super().__init__(parent)
        self.startPort = args[0]
        self.endPort = args[1]
        self.scanIp = args[2]

    def run(self):
        timestart = time.time()
        self.active = True
        self.portScanner = PortScanner()
        try:

            for i in range(self.startPort, self.endPort + 1):
                ergebnis = self.portScanner.scan(self.scanIp, i)
                if ergebnis:
                    self.portadd.emit("Offener Port bei: " + str(i))
                if not self.active:
                    self.portadd.emit("Scan abgebrochen")
                    return
        except:
            self.portadd.emit("Ein Fehler ist passiert")
            return
        # self.startButton.setDisabled(False)
        self.portadd.emit("Scan abgeschlossen in " + str(int(time.time() - timestart)) + " Sekunden")

    def kill(self):
        self.active = False


class PortScannerTab(QWidget):

    def __init__(self, console):
        self.console = console
        self.openPorts = []

        super().__init__()
        self.layout = QVBoxLayout(self)

        self.titleText = QLabel("<H1>Portscanner</H1>\nIP-Adresse")
        self.layout.addWidget(self.titleText)

        self.ipField = QLineEdit("192.168.178.1")
        self.layout.addWidget(self.ipField)

        self.hbox = QHBoxLayout()

        self.startLabel = QLabel("Von Port")
        self.endLabel = QLabel("Bis Port")

        self.startField = QLineEdit("1")
        self.endField = QLineEdit("65535")

        self.hbox.addWidget(self.startLabel)
        self.hbox.addWidget(self.startField)
        self.hbox.addWidget(self.endLabel)
        self.hbox.addWidget(self.endField)

        self.layout.addLayout(self.hbox)

        self.startButton = QPushButton()
        self.startButton.setText("Starte Scan")

        self.portScanner = PortScanner()
        self.startButton.clicked.connect(self.btnClicked)
        self.layout.addWidget(self.startButton)

        self.output = Console("Output")
        self.layout.addWidget(self.output)

        # self.layout.addStretch(1)

    def btnClicked(self):
        if self.startButton.text() == "Starte Scan":
            self.output.clear()
            self.thread = PortScanThread(
                args=(int(self.startField.text()), int(self.endField.text()), self.ipField.text()))
            self.thread.portadd.connect(self.logPort)
            self.thread.start()
            self.startButton.setText("Beende Scan")
        else:
            self.startButton.setText("Starte Scan")
            self.thread.kill()

    def logPort(self, port):

        self.output.log(port)
