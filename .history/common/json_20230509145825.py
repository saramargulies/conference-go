from json import JSONEncoder

class ModelEncoder(JSONEncoder):
    def default(self, obej):
        if isinstance(object, self.model):
            dictionary = {}
            for property in self.properties:
                value = getattr(obj, property)