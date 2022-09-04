from django.apps import AppConfig


class AdminAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_app'
    verbose_name = "Панель администратора"

    def ready(self):
        from django_celery_beat.models import IntervalSchedule, PeriodicTask
        schedule, created = IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS)

        PeriodicTask.objects.get_or_create(
            task='admin_app.tasks.mail_task_poller',
            interval=schedule,
            name='Search mail task'
        )


