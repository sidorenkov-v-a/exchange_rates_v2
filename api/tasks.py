from celery import shared_task
import requests
from .models import Currency, DateRate
from dateutil import parser

CBR_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


@shared_task
def update_rates():
    data = requests.get(CBR_URL).json()
    currencies = data['Valute']

    for letter_code, currency_data in currencies.items():
        name = currency_data['Name']
        currency, created = Currency.objects.get_or_create(
            name=name, letter_code=letter_code
        )
        rate = currency_data['Value']
        date = parser.parse(data['Date']).date()
        DateRate.objects.get_or_create(
            currency=currency, rate=rate, date=date
        )
