import sys

from PyQt5.Qt import QWidget, QMainWindow, QApplication, QVBoxLayout, QTabWidget

from src.Tabs.CPUStressTab import CPUStressTab
from src.Tabs.DosTab import DosTab
from src.Tabs.HashGeneratorTab import HashGeneratorTab
from src.Tabs.PortScannerTab import PortScannerTab
from src.Tabs.RainbowGeneratorTab import RainbowGeneratorTab
from src.other.Console import Console


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

        self.console = Console("Superconsole")

        self.tabs = QTabWidget()

        self.ddosTab = DosTab(self.console)
        self.portscannerTab = PortScannerTab(self.console)
        # self.hashcrackerTab = HashcrackerTab(self.console)
        self.hashGeneratorTab = HashGeneratorTab(self.console)
        self.rtGenTab = RainbowGeneratorTab(self.console)
        self.stressTab = CPUStressTab(self.console)

        # self.tabs.resize(800, 600)

        self.tabs.addTab(self.ddosTab, "Denial of Service")
        self.tabs.addTab(self.portscannerTab, "Portscanner")
        self.tabs.addTab(self.hashGeneratorTab, "HashGenrator")
        # self.tabs.addTab(self.hashcrackerTab, "Hashcracker (Not Working)")
        self.tabs.addTab(self.rtGenTab, "Rainbowtable Generator")
        self.tabs.addTab(self.stressTab, "CPU Stress")

        self.layout.addWidget(self.tabs)

        self.layout.addStretch(1)
        self.layout.addWidget(self.console)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
