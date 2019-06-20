import uuid
from hasher import Hasher


class Experiment:

    variations = []
    id = ""
    hasher = Hasher()


    def __init__(self):
        self.variations = [Variation(50, "variation1"), Variation(50, "variation2")]
        self.id = uuid.uuid4()

    def assign(self, user):
        string = f"{self.id}{user.id}"
        hash_str = self.hasher.hash(string)
        # obtain number from hash_str
        number = self.hash_to_number(hash_str)
        return self.get_variation(number)

    def get_variation(self, number: int):
        # this is okay just for our test, since we'll only use experiments with 2 variations
        # but for more variations it would not work at all
        self.variations.sort(key=lambda v: v.name)
        if (number % 100) < self.variations[0].traffic:
            return self.variations[0]
        else:
            return self.variations[1]

    def hash_to_number(self, string: str):
        return int(string, 16)

class Variation:
    traffic = 0
    name = ""

    def __init__(self, traffic, name):
        self.traffic = traffic
        self.name = name
