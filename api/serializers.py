from rest_framework.serializers import ModelSerializer

from .models import Currency


class RateSerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
