from django.core.management.base import BaseCommand, CommandError
from stats.models import Stats


class Command(BaseCommand):
    help='Update the Messages Stats'

    def handle(self, *args, **kwargs):
        Stats.update()
