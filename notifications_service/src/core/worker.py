import json

from db.rabbitmq_consumer import RabbitMQConsumer
from models.email import Email
from senders.email_sender import EmailSender, get_email_sender
from core.logger import logger
from core.settings import get_settings

TEMPLATE_TYPE_TO_PATH = {
    'common': 'templates/common.html',
    'stats': 'templates/stats.html',
    'custom': 'templates/custom.html'

}


def create_worker(
    queue_name: str,
    email_sender: EmailSender = get_email_sender()
) -> None:
    def callback(ch, method, properties, body):
        message = json.loads(body.decode('utf-8'))
        logger.info(f'Start processing message for {message["receiver"]}')
        template_path = TEMPLATE_TYPE_TO_PATH[message['template']]
        email = Email(
            receiver=message['receiver'],
            template_path=template_path,
            subject=message['subject'],
            content=message['content']
        )
        email_sender.send_notification(email)
        logger.info(f'Email for {email.receiver} sended!')

    mq_consumer = RabbitMQConsumer(rabbitmq_settings=get_settings().rabbitmq)
    mq_consumer.register_consumer(queue_name=queue_name, callback=callback)
    logger.info(f'Worker for {queue_name} created!')
    mq_consumer.start_consuming()
