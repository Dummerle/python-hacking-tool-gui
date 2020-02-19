import itertools
import multiprocessing
import os


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
        # print(cracked)
        queue.put(cracked)

    except:

        queue.put(None)


def initProc(charset):
    queue = []
    procs = []
    processes = 0
    for i in charset:
        queue.append(multiprocessing.Queue())
        proc = multiprocessing.Process(target=worker, args=(queue[queue.__len__()],
                                                            "ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a2192992a274fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f",
                                                            charset, i, "SHA512"))
        procs.append(proc)
        processes = processes + 1
        proc.daemon = True
        proc.start()

    res = []
    for i in range(processes):
        res.append(queue.get())

    for i in procs:
        i.join()
    for i in procs:
        # i.terminate()
        pass
    return res


CPU_Pct = str(round(
    float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),
    2))

# print results
print("CPU Usage = " + CPU_Pct)

'''
x = initProc("abcdefghij")

for i in x:
    if not i == None:
        print(i)
        pass
'''
