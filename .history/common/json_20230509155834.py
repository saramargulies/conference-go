from json import JSONEncoder
from datetime import datetime


class ModelEncoder(DateEncoder, JSONEncoder):
    def default(self, obj):
        if isinstance(obj, self.model):
            dictionary = {}
            for property in self.properties:
                value = getattr(obj, property)
                dictionary[property] = value
            return dictionary
        else:
            return super().default(obj)
