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
        content, created = AccountVO.objects.update_or_create(
            first_name = content["first_name"],
            last_name = content["last_name"],
            email = content["email"],
            defaults=None
        )
    else:
        AccountVO.objects.filter(email=content["email"])
    otherwise:
        Delete the AccountVO object with the specified email, if it exists