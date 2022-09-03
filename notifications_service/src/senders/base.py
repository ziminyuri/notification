from abc import ABC, abstractmethod
from typing import Any


class AbstractSender(ABC):
    @abstractmethod
    def send_notification(self, *args, **kwargs) -> Any:
        pass
