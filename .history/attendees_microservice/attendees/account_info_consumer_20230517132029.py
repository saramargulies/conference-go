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
  updated = convert updated_string from ISO string to datetime
  if is_active:
      Use the update_or_create method of the AccountVO.objects QuerySet
          to update or create the AccountVO object
  otherwise:
      Delete the AccountVO object with the specified email, if it exists