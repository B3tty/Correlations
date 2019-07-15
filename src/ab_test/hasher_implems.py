import hashlib

from ab_test.hasher import Hasher


class Md5Hasher(Hasher):
    def hash(self, string: str):
        m = hashlib.md5()
        m.update(string.encode("utf-8"))
        return int(m.hexdigest(), 16)


class Sha256Hasher(Hasher):
    def hash(self, string: str):
        m = hashlib.sha256()
        m.update(string.encode("utf-8"))
        return int(m.hexdigest(), 16)


class BuiltInHasher(Hasher):
    def hash(self, string: str):
        return hash(string)
