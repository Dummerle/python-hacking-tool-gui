from PyQt5.Qt import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

from src.Tools.DenialOfService import DenialOfService


class DosTab(QWidget):
    running = False
    dos = None

    def __init__(self, console):
        super().__init__()
        self.console = console
        self.layout = QVBoxLayout(self)

        self.titleText = QLabel()
        self.titleText.setText("<H1>Denial of service</h1>\nIp Adresse")
        self.layout.addWidget(self.titleText)

        self.ipField = QLineEdit("127.0.0.1")
        self.layout.addWidget(self.ipField)

        self.portLabel = QLabel()
        self.portLabel.setText("Port")
        self.layout.addWidget(self.portLabel)

        self.portField = QLineEdit()
        self.layout.addWidget(self.portField)

        self.startButton = QPushButton()
        self.startButton.setText("Starte Attacke")

        self.dos = DenialOfService(self.console)

        self.startButton.clicked.connect(self.start)
        self.layout.addWidget(self.startButton)

        self.layout.addStretch(1)

    def start(self):
        if not self.running:
            self.running = True
            self.startButton.setText("Stoppe Attacke")
            self.console.log("Angrff gestartet")
            self.dos.setIp(self.ipField.text())
            self.dos.setPort(int(self.portField.text()))
            if not self.dos.start():
                self.start()

        else:
            self.startButton.setText("Starte Attacke")
            self.running = False
            self.console.log("Angrff gestoppt")
            self.dos.stop()
