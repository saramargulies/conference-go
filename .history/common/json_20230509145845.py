from json import JSONEncoder

class ModelEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, self.model):
            dictionary = {}
            for property in self.properties:
                value = getattr(obj, property)
                dictionary[property] = value