from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Channel(models.TextChoices):

    email = "email", _("email")
    sms = "sms", _("sms")


class TimeStampedMixin(models.Model):
    """Mixin to extend class models with date fields create and modified."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TemplateType(models.TextChoices):

    common = 'common', _('Обычное письмо')
    personal_statistic = 'personal_statistic', _('Персональная статистика')


class Template(TimeStampedMixin):
    title = models.CharField(_('Наименование'), max_length=250)
    type = models.CharField(_('Тип'), choices=TemplateType.choices, max_length=50)
    template = RichTextField(_('Шаблон'))
    subject = models.TextField(_('Тема'), blank=True, null=True)
    channel = models.TextField(_("Cпособ передачи"), choices=Channel.choices, max_length=8)

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
    waiting = 'waiting', _('Ожидает отправки')
    processing = 'processing', _('В процессе отправки')
    done = 'done', _('Отправлено')
    cancelled = 'cancelled', _('Отменено')


class Priority(models.TextChoices):
    high = 'high', _('Высокий')
    medium = 'medium', _('Средний')
    low = 'low', _('Низкий')


class CategoryUsers(models.Model):
    name = models.CharField(max_length=250)
    category_id = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория пользователей'
        verbose_name_plural = 'Категории пользователей'


class MailTask(TimeStampedMixin):
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
    category = models.ForeignKey(CategoryUsers, on_delete=models.SET_NULL, null=True, blank=True)
    lifetime_hours = models.IntegerField(_('Актуальность сообщения'), default=1)

    scheduled_datetime = models.DateTimeField(blank=True, null=True)
    execution_datetime = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Задача на рассылку'
        verbose_name_plural = 'Задачи на рассылку'
