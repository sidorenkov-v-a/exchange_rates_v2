from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100, unique=True)
    letter_code = models.CharField(max_length=3, unique=True)


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
