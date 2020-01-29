import _hashlib


class HashGenerator():

    def getHash(self, string, type):
        if type == "SHA512":
            return _hashlib.openssl_sha512(string.encode()).hexdigest()
        elif type == "SHA256":
            return _hashlib.openssl_sha256(string.encode()).hexdigest()
        elif type == "SHA1":
            return _hashlib.openssl_sha1(string.encode()).hexdigest()
        elif type == "SHA224":
            return _hashlib.openssl_sha224(string.encode()).hexdigest()
        elif type == "MD5":
            return _hashlib.openssl_md5(string.encode()).hexdigest()
        elif type == "SHA384":
            return _hashlib.openssl_sha384(string.encode()).hexdigest()
