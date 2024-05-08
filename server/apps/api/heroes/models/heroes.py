from django.db import models
from django.utils.translation import gettext_lazy as _

class Heroes(models.Model):

    class EventKind(models.IntegerChoices):
        GPW = 1, _("Великая Отечественная война")
        SVO = 2, _("Специальная Военная Операция")

    event = models.PositiveIntegerField(
        choices=EventKind.choices,
        verbose_name=_("Событие")
    )

    firstname = models.CharField(
        max_length=128,
        verbose_name=_("Имя")
    )
    lastname = models.CharField(
        max_length=128,
        verbose_name=_("Фамилия")
    )
    midname = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name=_("Отчество")
    )

    photo = models.FileField(
        upload_to="heroes",
        max_length=255,
        verbose_name=_("Фото")
    )

    birthday = models.DateField(verbose_name=_("Дата рождения"))

    birth_place = models.CharField(
        max_length=256,
        verbose_name=_("Место рождения")
    )

    deathdate = models.DateField(verbose_name=_("Дата смерти"))

    grave_place = models.CharField(
        max_length=256,
        verbose_name=_("Место захоронения")
    )

    rank = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name=_("Воинское звание")
    )

    feat = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Описание подвига")
    )

    def __str__(self):
        if self.midname:
            return f'{self.lastname} {self.firstname[0]}. {self.midname[0]}.'
        else:
            return f'{self.lastname} {self.firstname[0]}.'

    class Meta:
        ordering = ["id"]
        verbose_name = _("Герой")
        verbose_name_plural = _("Герои")
