  
from django.core.management.base import BaseCommand

from filer.models import MyFile

import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        MyFile.delete_expired()
