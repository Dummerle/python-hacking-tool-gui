from PyQt5.Qt import QWidget, QVBoxLayout, QLabel, QTextEdit, \
    QPushButton, QComboBox

from src.Tools.HashGenerator import HashGenerator


class HashGeneratorTab(QWidget):

    def __init__(self, console):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.titleText = QLabel("<H1>HashGenerator</H1>\nText Einfügen")
        self.layout.addWidget(self.titleText)

        self.textField = QTextEdit()
        self.layout.addWidget(self.textField)

        self.selectHash = QComboBox(self)
        self.selectHash.addItems(["SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "MD5"])
        self.selectHash.setCurrentText("SHA512")
        self.layout.addWidget(self.selectHash)

        self.genButton = QPushButton("Generiere Hash")
        self.hashGenerator = HashGenerator()
        self.genButton.clicked.connect(self.generateHash)
        self.layout.addWidget(self.genButton)

        self.output = QTextEdit("Output")
        self.output.setReadOnly(True)
        self.layout.addWidget(self.output)

        self.layout.addStretch(1)

    def generateHash(self):
        text = self.textField.toPlainText()
        hash = self.selectHash.currentText()

        self.output.setText(self.hashGenerator.getHash(text, hash))
