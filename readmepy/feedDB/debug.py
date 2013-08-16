# Debug chron_job.py
import chron_job as cj
from simpleflake import *
import feedparser
import sqlite3
import re


RSS_link_list = '/home/ty/code/data/feeds_list.txt'
count = len(cj.get_tablenames(RSS_link_list))
print count

def test_1(RSS_link_list, count):
  '''
  When running the table function like this:
  a = table(RSS_link_list) 
  print a[0]
  
  Error Message returned: 
  UnicodeEncodeError: 'ascii' codec can't encode character 
  u'\u2019' in position 162: ordinal not in range(128)
  '''
  numbers = []
  for number in range(count):
    try:  
      if cj.articles(RSS_link_list, number) > 0:
        print True, cj.get_tablenames(RSS_link_list)[number]
      elif cj.articles(RSS_link_list, number) < 0:
        print False, cj.get_tablenames(RSS_link_list)[number]
    except (UnicodeEncodeError):
      print cj.get_tablenames(RSS_link_list)[number], "returns an exception"
      numbers.append(number)
  return numbers

# test_1 will return the numbers parameter for test_2
test_1(RSS_link_list, count)
numbers = test_1(RSS_link_list, count)

def test_2(RSS_link_list, numbers):
  '''
  When running test_1:
    NYTBusinessDay returns an exception
    NYTHomePage returns an exception
    NYTWorld returns an exception
  
  Finding those exceptions so they can be fixed.
  '''
  for number in numbers:
    print "\n", cj.get_tablenames(RSS_link_list)[number], "\n"
    links = cj.get_RSS_link(RSS_link_list)
    d = feedparser.parse(links[number])
    new_list = []
    try:
      # Here I'm breaking out articles(RSS_link_list, number)
      # and running it separately to see where it breaks
      for article in range(len(d)):
        primary_key = str(simpleflake())
        print "\n", primary_key
        title = d.entries[article].title
        print title
        description_junk = str(d.entries[article].description)
        description = cj.strip_garbage(description_junk)
        if len(description) > 40:
          print "check out description: ", number
        elif len(description) < 5:
          print "description seems short", number
        link = d.entries[article].link
        print link
        published = d.entries[article].published
        print published
        new_list.append((primary_key,title,description,link,published))
      return new_list
    except (UnicodeEncodeError):
      print "UnicodeEncodeError", "\n"
    finally:
      print "\t", "this feed is toast"


test_2(RSS_link_list, numbers)
