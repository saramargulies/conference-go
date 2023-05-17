from datetime import datetime
import json
import pika
from pika.exceptions import AMQPConnectionError
import django
import os
import sys
import time


sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendees_bc.settings")
django.setup()

from attendees.models import AccountVO


def update_accountVO(ch, method, properties, body):
    content = json.loads(body)
    first_name = content["first_name"]
    last_name = content["last_name"]
    email = content["email"]
    is_active = content["is_active"]
    updated_string = content["updated"]
    updated = datetime.fromisoformat(updated_string)
    
    if is_active:
        try:
    obj = Person.objects.get(first_name="John", last_name="Lennon")
    for key, value in defaults.items():
        setattr(obj, key, value)
    obj.save()
except Person.DoesNotExist:
    new_values = {"first_name": "John", "last_name": "Lennon"}
    new_values.update(defaults)
    obj = Person(**new_values)
    obj.save()
        Use the update_or_create method of the AccountVO.objects QuerySet
            to update or create the AccountVO object
    otherwise:
        Delete the AccountVO object with the specified email, if it exists