from __future__ import unicode_literals

from django.db import models

# Create your models here.

class InputForm(models.Model):
    name = models.TextField()