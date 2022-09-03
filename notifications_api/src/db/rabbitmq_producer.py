from functools import lru_cache

import pika
from pika.exceptions import AMQPConnectionError
import backoff

from core.settings import get_settings, RabbitMQSettings


class RabbitMQProducer:
    def __init__(self, rabbitmq_settings: RabbitMQSettings):
        self.settings = rabbitmq_settings
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.settings.host, self.settings.port))
        self.channel = self.connection.channel()

    def create_queue(self, queue_name: str):
        self.channel.queue_declare(queue=queue_name)

    def send_message_to_queue(self, message: str, queue_name: str, ttl_hours: int = 12):
        ttl_millisecs = ttl_hours * 60 * 60 * 1000
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            properties=pika.BasicProperties(expiration=str(ttl_millisecs)),
            body=message)


@lru_cache
@backoff.on_exception(backoff.expo,
                      AMQPConnectionError)
def get_rabbitmq_producer():
    return RabbitMQProducer(rabbitmq_settings=get_settings().rabbitmq)
