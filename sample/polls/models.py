from __future__ import unicode_literals

from django.db import models

class Meter(models.Model):
  active = models.CharField(max_length=48);
  area = models.CharField(max_length=48);
  latitude = models.FloatField();
  longitude = models.FloatField();
  meter_id = models.CharField(max_length=48);
  street_address = models.CharField(max_length=48);

class Events(models.Model):
  event_id = models.CharField(max_length=48);
  event_time = models.CharField(max_length=48);
  event_type = models.CharField(max_length=48);
  meter_id = models.ForeignKey(Meter,on_delete=models.CASCADE)
  ordinal = models.CharField(max_length=48);
  session_id = models.CharField(max_length=48);

