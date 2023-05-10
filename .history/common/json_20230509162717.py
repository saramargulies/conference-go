from json import JSONEncoder
from datetime import datetime
from django.db.models import QuerySet


class QuerySetEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return list(o)
        else:
            return super().default(o)


class DateEncoder(JSONEncoder):
    def default(self, obj):
        if type(obj) == datetime:
            return obj.isoformat()
        else:
            return super().default(obj)


class ModelEncoder(QuerySetEncoder, DateEncoder, JSONEncoder):
    def default(self, obj):
        if isinstance(obj, self.model):
            dictionary = {}
            if obj 
            for property in self.properties:
                value = getattr(obj, property)
                dictionary[property] = value
            return dictionary
        else:
            return super().default(obj)
