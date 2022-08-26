from django.contrib import admin

from .models import MailTask, Template


@admin.register(Template)
class TemplatesAdmin(admin.ModelAdmin):
    """Admin interface for Template."""


@admin.register(MailTask)
class MailTaskAdmin(admin.ModelAdmin):
    """Admin interface for Task."""
