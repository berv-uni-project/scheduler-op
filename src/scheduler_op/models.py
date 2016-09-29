from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=Document)
def document_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)