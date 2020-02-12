import itertools
import multiprocessing
from threading import Thread

from src.Tools.HashGenerator import HashGenerator


def fred(queue, proc):
    while True:
        xy = queue.get()
        proc.join()
        print("xyz")
        print(xy)
        # sleep(3)


def task():
    1 + 1


def worker(queue, hash, charset, startChar, hashType):
    hg = HashGenerator()

    for i in range(1, 7):
        for j in map("".join, itertools.product(charset, repeat=i)):

            if hg.getHash(startChar + j, hashType) == hash:
                # print(j)
                cracked = startChar + j
                break
    try:
        #print(cracked)
        queue.put(cracked)

    except:

        queue.put(None)


def initProc(charset):
    queue = multiprocessing.Queue()
    procs = []
    processes = 0
    for i in charset:
        proc = multiprocessing.Process(target=worker, args=(queue,
                                                            "d716a4188569b68ab1b6dfac178e570114cdf0ea3a1cc0e31486c3e41241bc6a76424e8c37ab26f096fc85ef9886c8cb634187f4fddff645fb099f1ff54c6b8c",
                                                            charset, i, "SHA512"))
        procs.append(proc)
        processes = processes + 1
        proc.daemon = True
        proc.start()

    res = []
    for i in range(processes):
        res.append(queue.get())
    for i in procs:
        t = Thread(target=fred, args=(queue, i))
        t.start()

    for i in procs:
        i.join()
    for i in procs:
        # i.terminate()
        pass
    return res


x = initProc("abcdefghij")

for i in x:
    if not i == None:
        #print(i)
        pass