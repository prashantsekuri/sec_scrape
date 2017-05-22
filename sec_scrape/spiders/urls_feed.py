#code to extract the list of urls for form 4s from the rss feed
#make the feedparser code more generic. try to pass the url as an argument to the fumction.
import feedparser
get_urls_from_feed() :
  start = 0
  count = 100
  url_list = []
  #url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=4&company=&dateb=&owner=include&start='+str(start)+'&count='+str(count)+'&output=atom'
  #f = feedparser.parse(url)
  #print(len(f.entries))
  while(start < 2001) : 
    url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=4&company=&dateb=&owner=include&start='+str(start)+'&count='+str(count)+'&output=atom'
    f = feedparser.parse(url)
    for i in range(len(f.entries)) :
      #print(f.entries[i].link)
      #print(f.entries[i].title)
      if (f.entries[i].title[0:2] == '4 '):    #to ensure forms 425 etc are not considered- do we need to consider 4/a - make a list of all different form types 
        url_list.append(f.entries[i].link)     #starting with 4 - use sets
        #print(f.entries[i].title)
        #print(f.entries[i].link)
    start = start + 100
  #print(len(url_list))
  #print(url_list)
  return url_list
  #we need to reduce redundancy in calling already called links. How do we do it?Maintain a list of already called links. if 4-5 continuous 'already called's #then stop executing and reload the feed.  Look for a better way of doing this. Maybe multi threading.
  #Do we need to send headers while sending request to each url ??
  #Use generator to generate and process individual urls