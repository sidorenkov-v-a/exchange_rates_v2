import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchange_rates.settings')

app = Celery('exchange_rates')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_exchange_rate': {
        'task': 'api.tasks.update_rates',
        'schedule': crontab(hour=11, minute=31)
    }
}

