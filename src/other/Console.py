from PyQt5.QtWidgets import QTextEdit


class Console(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setText("Console Version 0.1")

    def log(self, text: str):
        self.setText(self.toPlainText() + "\n" + text)
