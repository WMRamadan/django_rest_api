# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class shipment(models.Model):
    description = models.CharField(max_length=255)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    date_shipped = models.DateTimeField(blank=False)
    date_arrived = models.DateTimeField(blank=True)

    def __str__(self):
        return self.description

