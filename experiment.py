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
        result = self.hasher.hash(string)
        return result


class Variation:
    traffic = 0
    name = ""

    def __init__(self, traffic, name):
        self.traffic = traffic
        self.name = name
