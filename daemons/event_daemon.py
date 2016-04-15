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
   count=1
   print "Processing API"
   file=urllib.urlopen('https://parking.api.smgov.net/meters/events')
   raw_string = file.read()
   raw_json = json.loads(raw_string)
   conn = psycopg2.connect("dbname='django' user='djangouser' host='127.0.0.1' password='dbpass'")
   cur = conn.cursor()


   processed = 0;
   for each in raw_json:
         processed = processed + 1;

         ordinal = each.get('ordinal', 'xxx');
         event_id = each.get('event_id', 'xxx');
         event_time = each.get('event_time', 'xxx');
         event_type = each.get('event_type', 'xxx');
         meter_id = each.get('meter_id', 'xxx');
         session_id = each.get('session_id', 'xxx');
         cur.execute("""SELECT * from polls_meter WHERE meter_id = '%s';""" % (meter_id));
         result=cur.fetchone();
         print("""INSERT INTO polls_events (event_id, event_time, event_type, ordinal, session_id, meter_id_id) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');""" % (event_id, event_time, event_type, ordinal, session_id, result[0]));
         cur.execute("""INSERT INTO polls_events (event_id, event_time, event_type, ordinal, session_id, meter_id_id) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');""" % (event_id, event_time, event_type, ordinal, session_id, result[0]));

         conn.commit()

   print "PROCESSED from API: %d" % (processed)

loop();
