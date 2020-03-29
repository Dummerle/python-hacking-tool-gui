from PyQt5.QtWidgets import QTextEdit


class Console(QTextEdit):
    def __init__(self, starttext):
        super().__init__()
        self.setReadOnly(True)
        self.starttext = starttext
        self.setText(self.starttext)

    def log(self, text: str):
        self.setText(self.toPlainText() + "\n" + text)

    def clear(self):
        self.setText(self.starttext)
