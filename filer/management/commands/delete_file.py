  
from django.core.management.base import BaseCommand
from django.utils.timezone import now


from filer.models import MyFile

import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        files = MyFile.objects.filter(expire_on__lte=now())

        for f in files:
            print("deleting... ")
            logger.debug("deleting... ", f)
            f.delete()