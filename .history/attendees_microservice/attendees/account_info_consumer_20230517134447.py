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
            first_name=first_name,
            last_name=last_name,
            email=email,
            defaults=None,
        )
    else:
        AccountVO.objects.filter(email=email).delete()


while True:
    try:
        parameters = pika.ConnectionParameters(host="rabbitmq")
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.exchange_declare(exchange="account_info", exchange_type="fanout")
        result = channel.queue_declare(queue='', exclu)
        channel.basic_consume(
            queue="presentation_rejection",
            on_message_callback=process_rejection,
            auto_ack=True,
        )
        channel.queue_declare(queue="presentation_approval")
        channel.basic_consume(
            queue="presentation_approval",
            on_message_callback=process_approval,
            auto_ack=True,
        )
        channel.start_consuming()
    except AMQPConnectionError:
        print("Could not connect to RabbitMQ")
        time.sleep(2.0)
