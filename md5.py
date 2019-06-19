from experiment import *


class Md5Hasher(Hasher):

    def hash(self, string: str):
        return f"md5 of {string}"
