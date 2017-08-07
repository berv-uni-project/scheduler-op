from __future__ import unicode_literals

from django.db import models
from django.conf import settings

import os


# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.docfile.name))
        super(Document, self).delete(*args, **kwargs)
