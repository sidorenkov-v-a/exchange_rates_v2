from django.core.management import BaseCommand
from api.tasks import update_rates


class Command(BaseCommand):
    def handle(self, *args, **options):
        update_rates()
