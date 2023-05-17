import json
import pika
import django
import os
import sys
from django.core.mail import send_mail


sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "presentation_mailer.settings")
django.setup()

def process_message(ch, method, properties, body):
    print("  Received %r" % body)


parameters = pika.ConnectionParameters(host='rabbitmq')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='tasks')
channel.basic_consume(
    queue='tasks',
    on_message_callback=process_message,
    auto_ack=True,
)
channel.start_consuming()

send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)