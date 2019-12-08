import itertools
import _hashlib


class RainbowTableGen():

    def getHash(self, string, hash):
    
        if hash == "SHA512":
            return _hashlib.openssl_sha512(string.encode()).hexdigest()
        elif hash == "SHA265":
            return _hashlib.openssl_sha256(string.encode()).hexdigest()
        elif hash == "SHA1" :
            return _hashlib.openssl_sha1(string.encode()).hexdigest()
        elif hash == "SHA224":
            return _hashlib.openssl_sha224(string.encode()).hexdigest()
        elif hash == "MD5":
            return _hashlib.openssl_md5(string.encode()).hexdigest()
        elif hash == "SHA384":
            return _hashlib.openssl_sha384(string.encode()).hexdigest()
    
    def genRtFull(self, charset, sAnzahlZeichen, eAnzahlZeichen, hashType="SHA512"):
        
        rtFile = open("RainbowTable.txt", "w")
        
        myLetters = charset
        for i in range (sAnzahlZeichen, eAnzahlZeichen):
            for j in map ("".join, itertools.product(myLetters, repeat=i)):
                rtFile.write(j + " # " + str(self.getHash(j, hashType)) + "\n")          
        rtFile.close()
        
    def genRtFile(self, file, hashType="SHA512"):
        
        readFile = open(file, "r")
        rtFile = open("RainbowTable.txt", "w")
        for line in readFile:
            rtFile.write(line.rstrip() + " # " + str(self.getHash(line.rstrip(), hashType)) + "\n")
        readFile.close()
        
        rtFile.close()
  
