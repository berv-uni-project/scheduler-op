from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone

import os

def created_path(instance, filename):
    return os.path.join('documents/' + str(timezone.now().timestamp()) + '/', filename)

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to=created_path)
    createdDate = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.docfile.name))
        super(Document, self).delete(*args, **kwargs)
