from django.urls import path
from .views import admin_notification_crud

urlpatterns = [
    path('', admin_notification_crud),
]
