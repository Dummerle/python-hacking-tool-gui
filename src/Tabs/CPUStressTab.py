import os

from PyQt5.Qt import QWidget, QLabel, QSpinBox, QVBoxLayout, QPushButton

from src.Tools.CPUStress import CPUStress


class CPUStressTab(QWidget):
    def __init__(self, console):
        super().__init__()
        self.console = console
        self.cpustress = CPUStress()

        self.stress = False

        self.layout = QVBoxLayout(self)

        self.title = QLabel("<h1>CPU Stress</h1>\nAnzahl der Kerne (0 Cores = Anzahl der Systemkerne")
        self.layout.addWidget(self.title)
        self.cpuCoresSpin = QSpinBox()
        self.layout.addWidget(self.cpuCoresSpin)

        self.startButton = QPushButton("Start")
        self.startButton.clicked.connect(self.start)
        self.layout.addWidget(self.startButton)

        self.layout.addStretch(1)

    def start(self):
        if not self.stress:
            self.stress = True
            self.startButton.setText("Beende Stress")
            cpucores = int(self.cpuCoresSpin.text())
            if cpucores == 0:
                cpucores = os.cpu_count()
            self.console.log("Starte Stress mit " + str(cpucores) + " Kernen")
            self.cpustress.run(cpucores)
        else:
            self.stress = False
            self.startButton.setText("Start")
            self.cpustress.stop()
            self.console.log("Beendet")
