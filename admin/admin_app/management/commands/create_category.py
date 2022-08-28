from config.settings import GATEWAY_BACKEND_URL
import requests
from admin_app.models import CategoryUsers
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create category for mailing'

    def handle(self, *args, **options):
        response = requests.get(f"{GATEWAY_BACKEND_URL}/api/v1/role")
        response.raise_for_status()

        for d in response.json():
            CategoryUsers.objects.get_or_create(name=d['name'])