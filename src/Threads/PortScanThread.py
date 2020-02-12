from PyQt5.QtCore import QThread


class PortScanThread(QThread):

    def run(self):
        try:
            for i in range(self.start, self.end + 1):

                ergebnis = self.portScanner.scan(self.ip, i)
                if ergebnis:
                    # self.console.log("Offener Port bei: " + str(i))
                    self.openPorts.append(i)
                    print(i)
        except:
            self.console.log("Ein Fehler ist passiert")
        for i in self.openPorts:
            self.output.log("Offener dPort bei: "+str(i))
            pass
