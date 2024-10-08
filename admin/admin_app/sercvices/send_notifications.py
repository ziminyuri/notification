import requests

from config.settings import GATEWAY_BACKEND_URL, NOTIFICATION_BACKEND_URL

from ..models import MailTask


def process_sending(id):
    task = MailTask.objects.get(id=id)
    emails = _get_emails(task.category)
    return _send_notification(task, emails)


def _send_notification(task, emails):
    batch = 2
    if not emails:
        return True
    else:
        try:
            batched_emails = emails[:batch]
            payload = _prepare_payload(batched_emails, task)
            requests.post(
                f'{NOTIFICATION_BACKEND_URL}/api/v1/notifications/send-email-notification-batched',
                json=payload
            )
            return _send_notification(task, emails[batch:])
        except Exception:
            return False


def _prepare_payload(batched_emails, task):

    payload = []
    for email in batched_emails:
        payload.append({
            "receiver": email,
            "template": "custom",
            "subject": task.template.subject,
            "content": {"title": task.template.title,
                        "text": task.template.template},
            "notification_priority": task.priority,
            "notification_lifetime_hours": task.lifetime_hours
        })
    return payload


def _get_emails(category):
    if category == 'Все пользователи':
        response = requests.get(f'{GATEWAY_BACKEND_URL}/api/v1/users')
    else:
        response = requests.get(f'{GATEWAY_BACKEND_URL}/api/v1/role/{category.category_id}/user')
    data = response.json()
    return _extract_email(data)


def _extract_email(response):
    emails = []
    for row in response:
        emails.append(row['profile']['email'])
    return emails
