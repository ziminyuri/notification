from typing import List

from fastapi import APIRouter, Depends
from models.email import Email
from services.notifications import (EmailNotificationsService,
                                    get_email_notifications_service)

router = APIRouter(prefix='/notifications')


@router.post('/send-email-notification')
def send_email_notification(
    notification: Email,
    notifications_service: EmailNotificationsService = Depends(get_email_notifications_service)
) -> None:
    notifications_service.send_email_to_queue(notification)


@router.post('/send-email-notification-batched')
def send_email_notification_batched(
    notifications: List[Email],
    notifications_service: EmailNotificationsService = Depends(get_email_notifications_service)
) -> None:
    for notification in notifications:
        notifications_service.send_email_to_queue(notification)
