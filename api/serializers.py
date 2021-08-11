from rest_framework.serializers import ModelSerializer
from .models import Currency, DateRate

class DateRateSerializer(ModelSerializer):
    class Meta:
        model = DateRate
        fields = ['date', 'rate']


class CurrencySerializer(ModelSerializer):
    date_rates = DateRateSerializer(many=True)

    class Meta:
        model = Currency
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['history'] = data.pop('date_rates')
        return data


