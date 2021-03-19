import uuid

from django.db import models


class Account(models.Model):
    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        verbose_name='Уникальный ИД',
        editable=False,
    )
    owner = models.ForeignKey(
        'User',
        verbose_name='Владелец',
        on_delete=models.RESTRICT
    )
    number = models.CharField(
        verbose_name='Номер',
        max_length=25,
        unique=True,
    )
