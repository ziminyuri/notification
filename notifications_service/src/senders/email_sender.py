from typing import Any

from jinja2 import Template
import yagmail

from core.settings import EmailSettings, get_settings
from senders.base import AbstractSender
from models.email import Email


class EmailSender(AbstractSender):
    def __init__(self, email_settings: EmailSettings):
        self.yag = yagmail.SMTP(email_settings.gmail_username, email_settings.gmail_password)

    def send_notification(self, email: Email) -> Any:
        with open(email.template_path) as _file:
            template = Template(_file.read())
        content = template.render(**email.content)
        self.yag.send(email.receiver, email.subject, contents=[content])


def get_email_sender() -> EmailSender:
    return EmailSender(get_settings().email)
