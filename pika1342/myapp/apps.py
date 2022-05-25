import pika
from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    credentials = pika.PlainCredentials(username='guest', password='guest')
    parameters = pika.ConnectionParameters()
    conn = pika.BlockingConnection(parameters)
    conn.close()
