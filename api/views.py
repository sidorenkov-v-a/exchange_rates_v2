import datetime

from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Currency
from .serializers import RateSerializer
import requests

from django.http.response import HttpResponse


class RateViewSet(ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = RateSerializer


def test(request, add_time):
    from dateutil import parser
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = response.json()
    date = parser.parse(data['Date']).date() + datetime.timedelta(days=add_time)
    currencies = data['Valute']

    for currency in currencies.values():
        name = currency['Name']
        rate = currency['Value']
        defaults = {'name': name, 'rate': rate, 'date': date}
        Currency.objects.update_or_create(
            name=name, date=date, defaults=defaults
        )

    return HttpResponse('Ok')
