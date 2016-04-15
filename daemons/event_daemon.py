import xml.etree.ElementTree as ET
import urllib
import urllib2
import json
import time
import datetime
import copy
import pytz
#import operator
#outerList.sort(key=operator.itemgetter(3,1)) #sort by column 3 then 1 L(meter id)

def utc2pst(str):
   naive_date=datetime.datetime.strptime(str,'%Y%m%dT%H%M%SZ')
   tz = pytz.timezone('UTC')
   utc_date = tz.localize(naive_date, is_dst=None).astimezone(pytz.utc)
   pst_date=utc_date.astimezone(pytz.timezone('US/Pacific'))
   pretty_date = pst_date.strftime('%Y %b %d : %H %M %S')
   return pretty_date


def pretty(exit=-1):
  exit_count=0
  count=0
  for i in outerList:
    print i[0], i[1], i[2], i[3], i[4], i[5], count
    count=count+1
    if exit==exit_count:
      return
    exit_count+=1

def available():
  total_meters=0
  available_meters=0
  prev=outerList[0][3]
  state=''
  for i in outerList:
     if prev != i[3]:
        if state == 'SE':
           print prev, count, exit_count,print_count, 'state=',state
           available_meters+=available_meters
        prev = i[3]
     exit_count+=1
     state=i[2]
  

def ugly(exit=-1):
  print_count=1
  exit_count=0
  count=0
  prev=outerList[0][3]
  state=''
  for i in outerList:
     #print i, prev, i[3]
     if prev == i[3]:
        count+=1
     else :
        print prev, count, exit_count,print_count, 'state=',state
        prev = i[3]
        count=1
        print_count+=1
     if exit==exit_count:
        return
     exit_count+=1
     state=i[2]
  
def audit():
  prev = (outerList[0][5])-1
  for i in outerList:
   if (i[5])-prev > 1:
     print prev
     print i
   prev=i[5]
    

def peek(beg, end):
   i = beg
   while i<end:
      raw_date = outerList[i][1]
      pretty_date = utc2pst(raw_date)
      print outerList[i][0], pretty_date, outerList[i][2], outerList[i][3], outerList[i][4], outerList[i][5]
      i+=1

def loop():
 count=1
 while 1:
   print "Processing API"
   file=urllib.urlopen('https://parking.api.smgov.net/meters/events')
   raw_string = file.read()
   raw_json = json.loads(raw_string)


   before=len(S)
   beforeL=len(outerList)
   processed = 0;
   for each in raw_json:
      processed = processed + 1;
      ordinal = each.get('ordinal', 'xxx');
      if ordinal not in S:
         S.add(ordinal)

         event_id = each.get('event_id', 'xxx');
         event_time = each.get('event_time', 'xxx');
         event_type = each.get('event_type', 'xxx');
         meter_id = each.get('meter_id', 'xxx');
         session_id = each.get('session_id', 'xxx');
         #print ordinal, session_id, meter_id, event_type, event_time

         innerList=[]
         innerList.append(event_id)
         innerList.append(event_time)
         innerList.append(event_type)
         innerList.append(meter_id)
         innerList.append(session_id)
         innerList.append(ordinal)
         copyList = copy.deepcopy(innerList)
         outerList.append(copyList)
         print innerList

         after=len(S)
         afterL=len(outerList)

   print "SET Before count=%d After count=%d" % (before, after)
   print "LIST Before count=%d After count=%d" % (beforeL, afterL)
   print "PROCESSED from API: %d" % (processed)
   print "Sleeping for %d time" % (count)
   print datetime.datetime.now()
   count+=1
   time.sleep(30)

#S=set()
#outerList=[]
print "Terminating"

