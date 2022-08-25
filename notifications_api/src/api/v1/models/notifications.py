from enum import Enum

from pydantic import BaseModel


class NotificationSendType(str, Enum):
    email = 'email'
    phone_push_ios = 'phone_push_ios'
    phone_push_android = 'phone_push_android'
    phone_sms = 'phone_sms'


class NotificationRequestModel(BaseModel):
    user_id: str
    user_name: str
    content: str
    notification_send_type: NotificationSendType
    send_immediate: bool = False
    notification_lifetime_hours: int = 24 
