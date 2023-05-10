from json import JSONEncoder

class ModelEncoder(JSONEncoder):
    def default(self, obejct):
        if isinstance(object, self.model):
            dictionary = {}
            for property in self.properties:
                value = getattr(object, property)