from datetime import datetime

from config.celery import app
from .models import MailTask, Status
from .sercvices.send_notifications import process_sending
from django.utils import timezone


@app.task
def mail_task_poller():
    mail_tasks = MailTask.objects.filter(scheduled_datetime__lte=datetime.now(tz=timezone.utc), status=Status.waiting)
    for task in mail_tasks:
        MailTask.objects.filter(id=task.id).update(status=Status.processing)
        if process_sending(task.id):
            MailTask.objects.filter(id=task.id).update(status=Status.done, execution_datetime=datetime.now(tz=timezone.utc))
        else:
            MailTask.objects.filter(id=task.id).update(status=Status.cancelled, execution_datetime=datetime.now(tz=timezone.utc))

