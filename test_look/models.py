from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
	Comment = models.CharField(max_length=100)
	stats = models.BooleanField(default=True)