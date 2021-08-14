from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100, unique=True)
    letter_code = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name


class DateRate(models.Model):
    currency = models.ForeignKey(
        Currency,
        related_name='date_rates',
        on_delete=models.CASCADE
    )
    rate = models.FloatField()
    date = models.DateField()

    class Meta:
        unique_together = ['currency', 'date']
