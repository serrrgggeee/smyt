from __future__ import unicode_literals

from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)

class Count(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    class Meta:
       unique_together = ("title", "name")
