from enum import Enum

from pydantic import BaseModel


class NotificationPriority(str, Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'


class TemplateType(str, Enum):
    stats = 'stats'
    common = 'common'
    custom = 'custom'


class Email(BaseModel):
    receiver: str
    template: TemplateType
    subject: str
    content: dict
    notification_priority: NotificationPriority = NotificationPriority.low
    notification_lifetime_hours: int = 12
