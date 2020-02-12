from PyQt5.Qt import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal

from src.Tools.PortScanner import PortScanner
from src.other.Console import Console


class PortScanThread(QThread):
    changeValue = pyqtSignal([])

    def run(self):
        try:
            for i in range(self.start, self.end + 1):

                ergebnis = self.portScanner.scan(self.ip, i)
                if ergebnis:
                    # self.console.log("Offener Port bei: " + str(i))
                    self.openPorts.append(i)
                    print(i)
                    self.valueChanged.emit(self.openPorts)
        except:
            self.console.log("Ein Fehler ist passiert")
        # self.console.log("Scan Abgeschlossen")
        for i in self.openPorts:
            # self.output.log("Offener Port bei: "+str(i))
            pass


class PortScannerTab(QWidget):

    def __init__(self, console):
        self.console = console
        self.openPorts = []

        super().__init__()
        self.layout = QVBoxLayout(self)

        self.titleText = QLabel("<H1>Portcanner</H1>\nIP-Adresse")
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
        self.startButton.clicked.connect(self.initScanThread)
        self.layout.addWidget(self.startButton)

        self.output = Console()
        self.layout.addWidget(self.output)

        self.layout.addStretch(1)

    def initScanThread(self):

        ip = self.ipField.text()

        start = int(self.startField.text())
        end = int(self.endField.text())
        self.console.log("Starte Scan")
        print("Noch gut")

        self.thread = PortScanThread()

        self.thread.changeValue.connect(self.valueChanged)

        self.startButton.setDisabled(True)

        # self.output.moveToThread(t)

    def scan(self, ip: str, start: int, end: int):

        try:
            for i in range(start, end + 1):

                ergebnis = self.portScanner.scan(ip, i)
                if ergebnis:
                    # self.console.log("Offener Port bei: " + str(i))
                    self.openPorts.append(i)
                    print(i)
        except:
            self.console.log("Ein Fehler ist passiert")
        # self.console.log("Scan Abgeschlossen")
        for i in self.openPorts:
            # self.output.log("Offener Port bei: "+str(i))
            pass
        self.startButton.setDisabled(False)

    def valueChanged(self, openPorts: []):
        for i in openPorts:
            self.output.setText(self.output.toPlainText() + "Offener Port bei " + i)
