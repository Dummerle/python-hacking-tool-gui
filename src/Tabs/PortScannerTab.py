from PyQt5.Qt import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class PortScannerTab(QWidget):
   
    def __init__(self):
        
        super().__init__()
        self.layout=QVBoxLayout(self)
        
        self.titleText=QLabel()
        self.titleText.setText("Portcanner\nIP-Adresse")
        self.layout.addWidget(self.titleText)
        
        self.ipField=QLineEdit()
        self.layout.addWidget(self.ipField)
        
        self.startButton=QPushButton()
        self.startButton.setText("Starte Scan")
        self.startButton.clicked.connect(self.scan)
        self.layout.addWidget(self.startButton)
        
        self.layout.addStretch(1)
        
    def scan(self):
        print("comming soon")
        
        