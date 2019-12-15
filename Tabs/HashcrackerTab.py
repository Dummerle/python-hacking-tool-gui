
from PyQt5.Qt import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox,\
    QPushButton, QHBoxLayout

class HashcrackerTab(QWidget):
    

    def __init__(self):
        super().__init__()
        
        self.layout=QVBoxLayout(self)
        
        self.titleText=QLabel("<H1>Hashcracker</H1>\nHash hier einfügen")
        self.layout.addWidget(self.titleText)
        
        
        self.hashField=QLineEdit()
        self.layout.addWidget(self.hashField)
        
        self.hashSelectionLabel=QLabel("Wähle Hashfunktion aus")
        self.layout.addWidget(self.hashSelectionLabel)
        
        self.selectHash = QComboBox(self)
        self.selectHash.addItems(["SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "MD5"])
        self.selectHash.setCurrentText("SHA-512")
        self.layout.addWidget(self.selectHash)
        
        self.hboxText=QHBoxLayout()
        self.bruteforceLabel=QLabel("<H2>Bruteforce</H2>")
        self.listLabel=QLabel("<H2>Passwort Liste</H2>")
        self.rtLabel=QLabel("<H2>Ranbowtable Crack</H2>")
        self.hboxText.addWidget(self.bruteforceLabel)
        self.hboxText.addWidget(self.listLabel)
        self.hboxText.addWidget(self.rtLabel)
        self.layout.addLayout(self.hboxText)
        
        self.hboxAction=QHBoxLayout()
        self.bruteforceCharset=QLabel("Charset")
        self.hboxAction.addWidget(self.bruteforceCharset)
        self.listSelect=QPushButton("Wähle Datei aus")
        self.hboxAction.addWidget(self.listSelect)
        self.rtSelect=QPushButton("Wähle Ranbowtable aus")
        self.hboxAction.addWidget(self.rtSelect)
        self.layout.addLayout(self.hboxAction)
        
        self.hboxCrackButton=QHBoxLayout()
        self.bruteforceCrack=QPushButton("Crack Bruteforce")
        self.hboxCrackButton.addWidget(self.bruteforceCrack)
        self.listCrack=QPushButton("Crack List")
        self.hboxCrackButton.addWidget(self.listCrack)
        self.rainbowCrack=QPushButton("Crack Rainbowtable")
        self.hboxCrackButton.addWidget(self.rainbowCrack)
        self.layout.addLayout(self.hboxCrackButton)
                
        self.layout.addStretch(1)
        
        