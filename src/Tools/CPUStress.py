import multiprocessing
import time


class CPUStress:

    def stress(self):
        start = time.time_ns()
        while True:
            1 + 1

    def run(self, processes: int = 0):
        self.procs = []
        for i in range(processes):
            proc = multiprocessing.Process(target=self.stress)
            self.procs.append(proc)
            proc.start()

    def stop(self):
        for i in self.procs:
            i.terminate()
