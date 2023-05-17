import json
import pika
import django
import os
import sys
from django.core.mail import send_mail


sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "presentation_mailer.settings")
django.setup()

while True:
    try:
        def process_approval(ch, method, properties, body):
            print(" [x] Received %r" % body)
            jbody = json.loads(body)
            p_name = "presenter_name"
            title = "title"
            send_mail(
                "Your presentation has been accepted",
                f"{jbody[p_name]}, we're happy to tell you that your presentation {jbody[title]} has been accepted",
                "admin@conference.go",
                [jbody["presenter_email"]],
                fail_silently=False,
            )


        def process_rejection(ch, method, properties, body):
            print(" [x] Received %r" % body)
            jbody = json.loads(body)
            p_name = "presenter_name"
            title = "title"
            send_mail(
                "Your presentation has been rejected",
                f"{jbody[p_name]}, we regret to tell you that your presentation {jbody[title]} has been rejected",
                "admin@conference.go",
                [jbody["presenter_email"]],
                fail_silently=False,
            )


        parameters = pika.ConnectionParameters(host="rabbitmq")
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue="presentation_rejection")
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
    except AM
