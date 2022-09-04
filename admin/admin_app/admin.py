from django.contrib import admin

from .models import MailTask, Template, CategoryUsers


@admin.register(Template)
class TemplatesAdmin(admin.ModelAdmin):
    """Admin interface for Template."""


@admin.register(CategoryUsers)
class CategoryUsersAdmin(admin.ModelAdmin):
    """Admin interface for CategoryUsers."""


@admin.register(MailTask)
class MailTaskAdmin(admin.ModelAdmin):
    """Admin interface for Task."""
