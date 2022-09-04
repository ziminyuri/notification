from datetime import datetime

from config.celery import app
from .models import MailTask


@app.task
def mail_task_poller():
    mail_tasks = MailTask.objects.filter(scheduled_datetime__lte=datetime.now())
    for task in mail_tasks:
        task.objects.update(status='processing')


