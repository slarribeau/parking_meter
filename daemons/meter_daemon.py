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


   processed = 0;
   for each in raw_json:
      processed = processed + 1;
      active = each.get('active', 'xxx');
      area = each.get('area', 'xxx');
      latitude = each.get('latitude', 'xxx');
      longitude = each.get('longitude', 'xxx');
      meter_id = each.get('meter_id', 'xxx');
      street_address = each.get('street_address', 'xxx');
      #print active, street_address, meter_id, longitude, latitude

      # id | active |     area     | latitude | longitude  | meter_id | street_address 



      innerList=[]
      innerList.append(processed)
      innerList.append(active)
      innerList.append(area)
      innerList.append(latitude)
      innerList.append(longitude)
      innerList.append(meter_id)
      innerList.append(street_address)
      print innerList


   print "PROCESSED from API: %d" % (processed)


#loop();
conn = psycopg2.connect("dbname='django' user='djangouser' host='localhost' password='dbpass'")
cur = conn.cursor()
cur.execute("""SELECT * from polls_meter""")
rows = cur.fetchall()

for row in rows:
    print "   ", row[0]
