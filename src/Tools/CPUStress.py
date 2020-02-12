import multiprocessing


class CPUStress:

    def __init__(self):
        self.procs = []

    def stress(self):
        while True:
            1 + 1

    def run(self, processes: int = 0):
        self.procs.clear()
        for i in range(processes):
            proc = multiprocessing.Process(target=self.stress)
            self.procs.append(proc)
            proc.daemon = True
            proc.start()

    def stop(self):
        for i in self.procs:
            i.terminate()
