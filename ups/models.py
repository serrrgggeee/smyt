# -*- coding: utf-8 -*-

from django.db import models

class Grain(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Grain_weight(models.Model):
    question = models.ForeignKey(Grain)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)