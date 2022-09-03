from typing import Callable

import backoff
import pika
from pika.exceptions import AMQPConnectionError, ChannelClosedByBroker

from core.settings import RabbitMQSettings, get_settings


class RabbitMQConsumer:
    def __init__(self, rabbitmq_settings: RabbitMQSettings):
        self.settings = rabbitmq_settings
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.settings.host, self.settings.port))
        self.channel = self.connection.channel()

    def register_consumer(self, queue_name: str, callback: Callable):
        self.channel.basic_consume(
            queue=queue_name,
            auto_ack=True,
            on_message_callback=callback
        )

    def start_consuming(self):
        self.channel.start_consuming()


@backoff.on_exception(backoff.expo,
                      (AMQPConnectionError, ChannelClosedByBroker))
def get_rabbitmq_consumer():
    return RabbitMQConsumer(rabbitmq_settings=get_settings().rabbitmq)
