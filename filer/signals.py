from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import MyFile


@receiver(pre_delete,sender=MyFile)
def created_myuser(sender,instance=None,**kwargs):
    instance.myfile and instance.myfile.delete(False)