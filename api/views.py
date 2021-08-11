from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Currency, DateRate
from .serializers import CurrencySerializer
import requests
from django.http.response import HttpResponse


class CurrencyViewSet(ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


def test(request, add_time):
    from dateutil import parser
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    currencies = data['Valute']

    for letter_code, currency_data in currencies.items():
        name = currency_data['Name']
        currency, created = Currency.objects.get_or_create(
            name=name, letter_code=letter_code
        )
        rate = currency_data['Value']
        date = parser.parse(data['Date']).date()
        DateRate.objects.get_or_create(currency=currency, rate=rate, date=date)

    return HttpResponse('Ok')
