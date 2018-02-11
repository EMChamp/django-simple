# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AnimeSeries(models.Model):
    title = models.CharField(max_length=200)
    score = models.IntegerField(max_length=5)
    watchers = models.IntegerField(max_length=20)

    def __str__(self):
        return self.title