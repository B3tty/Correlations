from experiment import *
import hashlib


class Md5Hasher(Hasher):

    def __init__(self):
        pass

    def hash(self, string: str):
        m = hashlib.md5()
        m.update(string.encode("utf-8"))
        return m.hexdigest()


class Sha256Hasher(Hasher):

    def __init__(self):
        pass

    def hash(self, string: str):
        m = hashlib.sha256()
        m.update(string.encode("utf-8"))
        return m.hexdigest()
