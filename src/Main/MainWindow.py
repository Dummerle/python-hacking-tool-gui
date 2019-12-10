import sys

from PyQt5.Qt import QWidget, QMainWindow, QApplication, QVBoxLayout, QTabWidget, QTextEdit

from Tabs.DosTab import DosTab
from Tabs.PortScannerTab import PortScannerTab
from Tabs.HashcrackerTab import HashcrackerTab
from Tabs.HashGeneratorTab import HashGeneratorTab
from Tabs.RainbowGeneratorTab import RainbowGeneratorTab



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hacking Gui")
        self.setGeometry(0, 0, 800, 600)
        self.setCentralWidget(Tabs(self))
        self.show()


class Tabs(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        self.tabs = QTabWidget()
        
        self.ddosTab = DosTab()
        self.portscannerTab = PortScannerTab()
        self.hashcrackerTab = HashcrackerTab()
        self.hashGeneratorTab=HashGeneratorTab()
        self.rtGenTab = RainbowGeneratorTab()
        
        #self.tabs.resize(800, 600)
        
        self.tabs.addTab(self.ddosTab, "Denial of Service")
        self.tabs.addTab(self.portscannerTab, "Portscanner")
        self.tabs.addTab(self.hashGeneratorTab, "HashGenrator")
        self.tabs.addTab(self.hashcrackerTab, "Hashcracker")
        self.tabs.addTab(self.rtGenTab, "Rainbowtable Generator")
        
        
        self.layout.addWidget(self.tabs)
        
        self.layout.addStretch(1)
        self.ausgabe = QTextEdit()
        self.ausgabe.setReadOnly(True)
        self.ausgabe.setText("Console is Comming Soon")
        
        # self.s=open("log.txt", "w", True, "UTF-8")
        # sys.stdout=self.s
        self.layout.addWidget(self.ausgabe)
        self.setLayout(self.layout)
  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
