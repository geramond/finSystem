from django.db import models


class Currency(models.Model):
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    code = models.CharField(
        verbose_name='Уникальный код валюты',
        max_length=10,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование',
        max_length=255,
    )
    rate = models.DecimalField(
        verbose_name='Курс по отношению к рублю',
        decimal_places=2,
        max_digits=15,
    )

    def __str__(self):
        return f'{self.name} ({self.code})'
