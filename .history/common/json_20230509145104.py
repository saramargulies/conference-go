from json import JSONEncoder

class ModelEncoder(JSONEncoder):
    def default(self, o):
        pass