from __future__ import with_statement
import urllib2
from BeautifulSoup import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

def get_head_row():
    page = urllib2.urlopen("http://item.yhd.com/item/1810581")
    soup = BeautifulSoup(page)
    l = soup.findAll('input')
    with open("data.csv",'a') as f:
        f.write('%s\n'%','.join([i.get('id') for i in l[1:37]]))

def get_data_row(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    l = soup.findAll('input')
    with open("data.csv",'a') as f:
        f.write('%s\n'%','.join([i.get('value') for i in l[1:37]]))

url_prefix = "http://item.yhd.com/item/%s"
#get_head_row()
id_base = 908852
for i in xrange(100000):
    try:
        id = id_base + i
        get_data_row(url_prefix%id)
    except Exception, e:
        print id, 'shit'
    print '============>',i, 'done'
			
