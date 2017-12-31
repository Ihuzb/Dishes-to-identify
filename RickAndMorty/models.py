# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Foods(models.Model):
    def __str__(self):
        return '{} {} {}'.format(self.name, self.nutritive, self.adapt)

    name = models.CharField(max_length=10)
    nutritive = models.CharField(max_length=50)
    adapt = models.CharField(max_length=100)
