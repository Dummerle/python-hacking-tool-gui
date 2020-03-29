import _hashlib
import itertools
import os


class RainbowTableGen():

    def getHash(self, string, hash):

        if hash == "SHA512":
            return _hashlib.openssl_sha512(string.encode()).hexdigest()
        elif hash == "SHA265":
            return _hashlib.openssl_sha256(string.encode()).hexdigest()
        elif hash == "SHA1":
            return _hashlib.openssl_sha1(string.encode()).hexdigest()
        elif hash == "SHA224":
            return _hashlib.openssl_sha224(string.encode()).hexdigest()
        elif hash == "MD5":
            return _hashlib.openssl_md5(string.encode()).hexdigest()
        elif hash == "SHA384":
            return _hashlib.openssl_sha384(string.encode()).hexdigest()

    def genRtFull(self, charset, sAnzahlZeichen, eAnzahlZeichen, hashType="SHA512", filename="Rainbowtable.txt"):

        rtFile = open(filename, "w")

        myLetters = charset
        for i in range(sAnzahlZeichen, eAnzahlZeichen + 1):
            for j in map("".join, itertools.product(myLetters, repeat=i)):
                rtFile.write(str(self.getHash(j, hashType)) + "#" + j + os.linesep)
        rtFile.close()
        print("Gen Abgeschlossen")
    def genRtFile(self, file, hashType="SHA512", wfilename="RainbowTable.txt"):

        readfile = open(file, "r")
        newFile = open(wfilename, "w")
        for i in readfile:
            newFile.write(self.getHash(i, hashType) + "#" + i)
        newFile.close()
        print("Generierung abgeschlossen")
