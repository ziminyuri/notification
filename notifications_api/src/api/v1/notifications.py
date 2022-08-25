from fastapi import APIRouter

from api.v1.models.notifications import NotificationRequestModel

router = APIRouter(prefix='/notifications')


@router.post('/send-notification')
def send_notification(notification: NotificationRequestModel):
    return notification 


@router.post('/send-notification-batched')
def send_notification_batched(notifications: list[NotificationRequestModel]):
    return notifications
