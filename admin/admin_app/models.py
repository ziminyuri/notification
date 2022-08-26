from django.db import models
from django.db.models import JSONField
from django.utils import timezone


class TemplateType(models.TextChoices):

    common = 'common', 'Обычное письмо'
    personal_statistic = 'personal_statistic', 'Персональная статистика'


class Template(models.Model):
    title = models.CharField('Наименование', max_length=250)
    type = models.CharField('Тип', choices=TemplateType.choices, max_length=50)
    template = models.TextField('Шаблон')
    subject = models.TextField('Тема', blank=True, null=True)

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'


class Status(models.TextChoices):
    waiting = 'waiting', 'Ожидает отправки'
    done = 'done', 'Отправлено'
    cancelled = 'cancelled', 'Отменено'


class Priority(models.TextChoices):
    high = 'high', 'Высокий'
    medium = 'medium', 'Средний'
    low = 'low', 'Низкий'


class MailTask(models.Model):
    status = models.CharField(
        max_length=250,
        choices=Status.choices,
        default=Status.waiting,
    )

    priority = models.CharField(
        max_length=250,
        choices=Priority.choices,
        default=Priority.low
    )
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)
    context = JSONField(default={})

    scheduled_datetime = models.DateTimeField(blank=True, null=True)
    execution_datetime = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Задача на рассылку'
        verbose_name_plural = 'Задачи на рассылку'
