import uuid

from ab_test.hasher import Hasher


class Experiment:
    variations = []
    id = ""
    hasher = Hasher()

    def __init__(self):
        self.variations = [Variation(50, "variation1"), Variation(50, "variation2")]
        self.id = uuid.uuid4()

    def __init__(self, hasher: Hasher):
        self.variations = [Variation(50, "variation1"), Variation(50, "variation2")]
        self.id = uuid.uuid4()
        self.hasher = hasher

    def __init__(self, hasher: Hasher, *args):
        self.variations = [Variation(50, "variation1"), Variation(50, "variation2")]
        if args:
            id = args[0]
            self.id = f'{id:06d}'
        else:
            self.id = uuid.uuid4()
        self.hasher = hasher

    def assign(self, user):
        string = f"{self.id}{user.id}"
        hash_int = self.hasher.hash(string)
        return self.get_variation(hash_int)

    def get_variation(self, number: int):
        # this is okay just for our test, since we'll only use experiments with 2 variations
        # but for more variations it would not work at all
        self.variations.sort(key=lambda v: v.name)
        if (number % 100) < self.variations[0].traffic:
            return self.variations[0]
        else:
            return self.variations[1]


class Variation:
    traffic = 0
    name = ""

    def __init__(self, traffic, name):
        self.traffic = traffic
        self.name = name
