# Debug chron_job.py
import chron_job as cj

count = len(cj.get_tablenames(RSS_link_list))
print count

for number in range(count):
  try  
    if cj.articles(RSS_link_list, number) > 0
      print True, cj.get_tablenames(RSS_link_list)[number]
    elif cj.articles(RSS_link_list, number) < 0
      print False, cj.get_tablenames(RSS_link_list)[number]
  except 
    print cj.get_tablenames(RSS_link_list)[number], "returns an exception"
      

