from enum import Enum


class Queues(str, Enum):
    email_low_priority = 'email_low_priority'
    email_medium_priority = 'email_medium_priority'
    email_high_priority = 'email_high_priority'
