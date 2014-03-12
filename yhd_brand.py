from __future__ import with_statement
import urllib2
from BeautifulSoup import BeautifulSoup
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8') 
HEADERS = {'User-Agent':'Mozilla/5.0'}

def get_head_row():
    req = urllib2.Request("http://item.yhd.com/item/1810581", None, HEADERS)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    l = soup.findAll('input')
    with open("yhd_data.csv",'a') as f:
        f.write('%s\n'%','.join([i.get('id') for i in l[1:37]]))

def get_data_row(url):
    req = urllib2.Request(url, None, HEADERS)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    l = soup.findAll('input')
    #toothpaste categoryId=5073, l[10]
    if int(l[10].get('value'))==5073:
        with open("yhd_data.csv",'a') as f:
            f.write('%s\n'%','.join([i.get('value') for i in l[1:37]]))
        return 1
    return 0

url_prefix = "http://item.yhd.com/item/%s"
get_head_row()
id_base = 1000000
count = 0
hit = 0
for i in xrange(1000000):
    count += 1
    try:
        id = id_base + i
        r = get_data_row(url_prefix%id)
        if r:
            hit += 1
    except Exception, e:
        #print id, 'shit', e, e.message
        pass
    if i%10 == 1:
        print '%s/%s'%(hit,count)
    if i%30 == 1:
        time.sleep(0.3)
    print '============>',i, 'done'


			
