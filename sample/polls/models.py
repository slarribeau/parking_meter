from __future__ import unicode_literals

from django.db import models

#Steps to populate Meter table:
# Django:
#  q=Meter(active='true', area='DOWNTOWN-CBD', longitude='-118.491760', latitude='34.01633', meter_id='MAI1612', street_address='1600 MAIN ST')
#q.save()
#
# SQL
#insert into polls_meter values(3,'true', 'DOWNTOWN-CBD', 34.01639, -118.49171, 'MAI1662', '1696 MAIN ST');


class Meter(models.Model):
  active = models.CharField(max_length=48);
  area = models.CharField(max_length=48);
  latitude = models.FloatField();
  longitude = models.FloatField();
  meter_id = models.CharField(max_length=48);
  street_address = models.CharField(max_length=48);

#Steps to populate Events table:
#from polls.models import Meter
#m = Meter.objects.get(pk=1)
#e1=Events(event_id='42846099', event_time='20160414T161824Z', event_type='SE', meter_id=m1, ordinal='41163977', session_id='264999866') 
#e.save()
class Events(models.Model):
  event_id = models.CharField(max_length=48);
  event_time = models.CharField(max_length=48);
  event_type = models.CharField(max_length=48);
  #meter_id = models.CharField(max_length=48);
  meter_id = models.ForeignKey(Meter, related_name='meters');
  ordinal = models.CharField(max_length=48);
  session_id = models.CharField(max_length=48);
 
  def __unicode__(self):
        return '%s: %s' % (self.event_type, self.event_time)


