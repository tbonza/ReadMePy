# Debug chron_job.py
import chron_job as cj

count = len(cj.get_tablenames(RSS_link_list))
print count

def test_1(count):
  '''
  When running the table function like this:
  a = table(RSS_link_list) 
  print a[0]
  
  Error Message returned: 
  UnicodeEncodeError: 'ascii' codec can't encode character 
  u'\u2019' in position 162: ordinal not in range(128)
  '''
  for number in range(count):
    try:  
      if articles(cj.RSS_link_list, number) > 0:
        print True, cj.get_tablenames(RSS_link_list)[number]
      elif cj.articles(RSS_link_list, number) < 0:
        print False, cj.get_tablenames(RSS_link_list)[number]
    except: 
      print cj.get_tablenames(RSS_link_list)[number], "returns an exception"


def test_2(count):
  '''
  When running test_1:
    NYTBusinessDay returns an exception
    NYTHomePage returns an exception
    NYTWorld returns an exception
  
  Finding those exceptions so they can be fixed.
  '''
  

