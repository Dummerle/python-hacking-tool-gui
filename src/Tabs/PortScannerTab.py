from PyQt5.Qt import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,\
    QHBoxLayout
from Tools.PortScanner import PortScanner
from threading import Thread

class PortScannerTab(QWidget):
   
    def __init__(self):
        
        super().__init__()
        self.layout=QVBoxLayout(self)
        
        self.titleText=QLabel()
        self.titleText.setText("<H1>Portcanner</H1>\nIP-Adresse")
        self.layout.addWidget(self.titleText)
        
        self.ipField=QLineEdit()
        self.layout.addWidget(self.ipField)
        
        self.hbox=QHBoxLayout()
        
        self.startLabel=QLabel("Von Port")
        self.endLabel=QLabel("Bis Port")
        
        self.startField=QLineEdit("1")
        self.endField=QLineEdit("65535")
        
        self.hbox.addWidget(self.startLabel)
        self.hbox.addWidget(self.startField)
        self.hbox.addWidget(self.endLabel)
        self.hbox.addWidget(self.endField)
        
        self.layout.addLayout(self.hbox)
        
        self.startButton=QPushButton()
        self.startButton.setText("Starte Scan")
        
        self.portScanner=PortScanner()
        self.startButton.clicked.connect(self.initScanThread)
        self.layout.addWidget(self.startButton)
        
        self.layout.addStretch(1)
        
    def initScanThread(self):
        
        ip=self.ipField.text()
        start=int(self.startField.text())
        end=int(self.endField.text())
        t=Thread(target=self.scan, args=(ip, start, end))
        t.start()
        
        
    def scan(self, ip:str, start:int, end:int):
        self.portScanner.setRange(start, end)
        self.portScanner.scan(ip)
        