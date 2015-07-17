import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Custom management command to build frontend"""
    help = 'Custom management to build frontend'

    def handle(self, *args, **options):
        os.system('gunicorn quotoxic.wsgi --log-file -')
