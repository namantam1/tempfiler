from django.db import models

import os
from django.utils import timezone
import uuid

def get_file_path(instance, file):
    now = timezone.now()
    _, ext = os.path.splitext(file)
    data = {
        'year': str(now.year)[:2],
        'month': now.strftime('%b'),
        'hash': uuid.uuid4().hex[:8] + ext,
    }
    return '{year}/{month}/{hash}'.format(**data)

class MyFile(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    expire_on = models.DateTimeField()
    myfile = models.FileField(upload_to=get_file_path)

