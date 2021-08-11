from django.contrib import admin

from .models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'rate', 'date')


admin.site.register(Currency, CurrencyAdmin)
