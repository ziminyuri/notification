from functools import lru_cache

from db.rabbitmq_producer import RabbitMQProducer, get_rabbitmq_producer
from models.email import Email, NotificationPriority
from models.queues import Queues


class EmailNotificationsService:
    EMAIL_PRIORITY_TO_QUEUE = {
        NotificationPriority.low: Queues.email_low_priority,
        NotificationPriority.medium: Queues.email_medium_priority,
        NotificationPriority.high: Queues.email_high_priority,
    }

    def __init__(self, mq_producer: RabbitMQProducer = get_rabbitmq_producer()):
        self.mq_producer = mq_producer

    def send_email_to_queue(self, email: Email) -> None:
        queue_name = self.EMAIL_PRIORITY_TO_QUEUE[email.notification_priority].value
        self.mq_producer.send_message_to_queue(message=email.json(), queue_name=queue_name, ttl_hours=email.notification_lifetime_hours)


@lru_cache
def get_email_notifications_service() -> EmailNotificationsService:
    return EmailNotificationsService()
