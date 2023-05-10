from json import JSONEncoder

class ModelEncoder(JSONEncoder):
    def default(self, obejct):
        if isinstance(o, self.model):
            d =