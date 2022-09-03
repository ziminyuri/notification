from pydantic import BaseModel


class Email(BaseModel):
    receiver: str
    template_path: str
    subject: str
    content: dict
