from functools import lru_cache
from enum import Enum


class Queues(str, Enum):
    email_low_priority = 'email_low_priority'
    email_medium_priority = 'email_medium_priority'
    email_high_priority = 'email_high_priority'


@lru_cache
def get_queues_list() -> list[str]:
    return [Queues.email_low_priority, Queues.email_medium_priority, Queues.email_high_priority]
