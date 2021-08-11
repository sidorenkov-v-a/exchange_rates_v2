from django.contrib import admin

from .models import Currency, DateRate


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'letter_code')


class DateRateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'currency', 'rate', 'date')


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(DateRate, DateRateAdmin)
