from PyQt5.Qt import QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, \
    QHBoxLayout, QLineEdit, QFileDialog

from src.Tools.RainbowTableGen import RainbowTableGen


class RainbowGeneratorTab(QWidget):

    def __init__(self, console):
        super().__init__()

        self.rtGen = RainbowTableGen()

        self.layout = QVBoxLayout(self)
        self.titleText = QLabel("<H1>Rainbowtable Generator</H1>")
        self.layout.addWidget(self.titleText)

        self.selectHash = QComboBox(self)
        self.selectHash.addItems(["SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "MD5"])
        self.selectHash.setCurrentText("SHA512")
        self.layout.addWidget(self.selectHash)

        self.selectList = QPushButton("Wähle Liste aus")
        self.selectList.clicked.connect(self.selectFile)
        self.layout.addWidget(self.selectList)

        self.selectedFile = QLabel("Wähle eine Datei aus")
        self.layout.addWidget(self.selectedFile)

        self.generateButton = QPushButton("Generiere Rainbow Table aus Liste")
        self.layout.addWidget(self.generateButton)

        self.fullLabel = QLabel("<H2>Generiere ganze RainbowTable</H2>")
        self.layout.addWidget(self.fullLabel)

        self.charset = QLabel("Charset")
        self.layout.addWidget(self.charset)

        self.charsetLine = QLineEdit()
        self.layout.addWidget(self.charsetLine)

        self.hbox = QHBoxLayout()
        self.startLabel = QLabel("Anzahl Zeichen von")
        self.startField = QLineEdit("1")
        self.endLabel = QLabel("bis")
        self.endField = QLineEdit("8")

        self.hbox.addWidget(self.startLabel)
        self.hbox.addWidget(self.startField)
        self.hbox.addWidget(self.endLabel)
        self.hbox.addWidget(self.endField)
        self.layout.addLayout(self.hbox)
        self.filenameLabel = QLabel("Dateiname")
        self.filenameField = QLineEdit("RainbowTable.txt")
        self.layout.addWidget(self.filenameLabel)
        self.layout.addWidget(self.filenameField)

        self.genFullButton = QPushButton("Generiere RainbowTable komplett (Große Dateien möglich)!")
        self.genFullButton.clicked.connect(self.genFull)
        self.layout.addWidget(self.genFullButton)

        self.layout.addStretch(1)

    def genList(self):
        pass

    def selectFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open FIle', '/home/lennard/Downloads', '*')
        self.selectedFile.setText(self.filename)

    def genFull(self):
        charset = self.charsetLine.text()
        startZeichen = int(self.startField.text())
        endZeichen = int(self.endField.text())
        hashType = self.selectHash.currentText()
        filename = self.filenameField.text()

        print("Starte Generierung")
        self.rtGen.genRtFull(charset, startZeichen, endZeichen, hashType, filename)
