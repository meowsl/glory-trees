from django.db import models
from django.utils.translation import gettext_lazy as _
from .applications import Application

class Archive(models.Model):

    class ApplicationStatus(models.IntegerChoices):
        APPROVED = 1, _("Одобрено")
        REJECTED = 2, _("Отклонено")

    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        verbose_name=_("Заявка")
    )
    reason = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Причина")
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Дата")
    )

    status = models.PositiveIntegerField(
        choices=ApplicationStatus.choices,
        editable=False,
        verbose_name=_("Статус заявки")
    )

    def __str__(self):
        return f'{self.application.lastname} {self.application.firstname} ({self.date})'

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Архив")
        verbose_name_plural = _("Архив")