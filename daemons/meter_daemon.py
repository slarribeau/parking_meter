import xml.etree.ElementTree as ET
import urllib
import urllib2
import json
import time
import datetime
import copy
import pytz
import psycopg2


def loop():
   copyList=[];
   outerList=[];

   print "Processing API"
   file=urllib.urlopen('https://parking.api.smgov.net/meters')
   raw_string = file.read()
   raw_json = json.loads(raw_string)
   conn = psycopg2.connect("dbname='django' user='djangouser' host='127.0.0.1' password='dbpass'")
   cur = conn.cursor()


   processed = 0;
   for each in raw_json:
      processed = processed + 1;
      active = each.get('active', 'xxx');
      area = each.get('area', 'xxx');
      latitude = each.get('latitude', 'xxx');
      longitude = each.get('longitude', 'xxx');
      meter_id = each.get('meter_id', 'xxx');
      street_address = each.get('street_address', 'xxx');

      print("""INSERT INTO polls_meter VALUES ('%s', '%s', '%s', %f, %f, '%s', '%s');""" % (processed,  active, area, latitude, longitude, meter_id, street_address));
      #cur.execute("""INSERT INTO polls_meter VALUES ('%s', '%s', '%s', %f, %f, '%s', '%s');""" % (processed,  active, area, latitude, longitude, meter_id, street_address));
      #conn.commit()

   print "PROCESSED from API: %d" % (processed)


loop();

#cur.execute("""SELECT * from polls_meter""")
#rows = cur.fetchall()

#for row in rows:
#    print "   ", row[0], row

