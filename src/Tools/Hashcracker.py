import itertools

from src.Tools.HashGenerator import HashGenerator


class Hashcracker():

    def __init__(self):
        pass

    def setFile(self, file):
        self.file = file

    def setHash(self, hash: str):
        self.hash = hash

    def crackFull(self, charset: str, numberChars: int, hashType: str, hash: str, increment: bool = False):

        hg=HashGenerator()

        if increment:

            for i in range(1, numberChars + 1):
                for j in map("".join, itertools.product(charset, repeat=i)):
                    if hg.getHash(j, hashType)==hash:
                        print(j)
                        return j
        else:
            for j in map("".join, itertools.product(charset, repeat=numberChars)):
                if hg.getHash(j, hashType) == hash:
                    print(j)
                    return j


hc = Hashcracker()
hc.crackFull("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 4, "SHA512", "d85924ad1060aac7704c620354fe7cb779fb32be08b82c6da450c3c8d0df5ecdfc4ad2baa7778e75db78c6ff809d16c2fba48b3ce4a9c440cef924ed1d538efd", True)
