from json import JSONEncoder

class ModelEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, self.model):
            d =