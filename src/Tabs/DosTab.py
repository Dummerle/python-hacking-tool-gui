from PyQt5.Qt import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

from src.Tools.DenialOfService import DenialOfService


class DosTab(QWidget):

    running=False
    dos=None

    def __init__(self):
        super().__init__()
        
        self.layout=QVBoxLayout(self)
        
        self.titleText = QLabel()
        self.titleText.setText("<H1>Denial of service</h1>\nIp Adresse") 
        self.layout.addWidget(self.titleText)
        
        self.ipField = QLineEdit()
        self.layout.addWidget(self.ipField)
        
        self.portLabel = QLabel()
        self.portLabel.setText("Port")
        self.layout.addWidget(self.portLabel) 
        
        self.portField = QLineEdit()
        self.layout.addWidget(self.portField)
        
        self.startButton = QPushButton()
        self.startButton.setText("Starte Attacke")
        self.dos=DenialOfService()
        self.startButton.clicked.connect(self.start)
        self.layout.addWidget(self.startButton)
        
        self.layout.addStretch(1)
                
    def start(self):
        if not self.running:
            self.running=True
            self.startButton.setText("Stoppe Attacke")
            
            self.dos.setIp(self.ipField.text())
            self.dos.setPort(int(self.portField.text()))
            self.dos.start()
            
        else:
            self.startButton.setText("Starte Attacke")
            self.running=False
            self.dos.stop()
        
        
        
