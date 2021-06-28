from django.db import models
from django.utils.timezone import now

import os
import uuid

def get_file_path(instance, file):
    _, ext = os.path.splitext(file)
    data = {
        'hash': uuid.uuid4().hex[:10] + ext,
    }
    return '{hash}'.format(**data)

class MyFile(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    expire_on = models.DateTimeField()
    myfile = models.FileField(upload_to=get_file_path)

    @classmethod
    def delete_expired(cls):
        files = cls.objects.filter(expire_on__lte=now())

        for f in files:
            print("deleting... ", f)
            f.delete()
