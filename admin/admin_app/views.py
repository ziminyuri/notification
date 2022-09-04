from django.http import HttpResponse
from .models import MailTask, Status
from datetime import datetime
import requests


def admin_notification_crud(request):
    mail_tasks = MailTask.objects.filter(scheduled_datetime__lte=datetime.now(), status=Status.waiting)
    for task in mail_tasks:
        # MailTask.objects.filter(id=task.id).update(status=Status.processing)
        process_sending(task.id)

    return HttpResponse(request, status=200)


def process_sending(id):
    task = MailTask.objects.get(id=id)
    users = get_users(task.category)


def get_users(category):
    if category == 'Все пользователи':
        print("Все пользователи")
    else:
        response = requests.get('http://127.0.0.1:5000/api/v1/role/3/user')
        data = response.json()

    return []



