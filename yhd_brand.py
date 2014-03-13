from __future__ import with_statement
import urllib2
from BeautifulSoup import BeautifulSoup
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8') 
HEADERS = {'User-Agent':'Mozilla/5.0'}
RESULT_DATA_CSV = 'yhd_data%s.csv'%int(time.time())
def get_head_row():
    req = urllib2.Request("http://item.yhd.com/item/1810581", None, HEADERS)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    l = soup.findAll('input')
    with open(RESULT_DATA_CSV,'a') as f:
        f.write('%s\n'%','.join([i.get('id') for i in l[1:37]]))

def get_data_row(url):
    req = urllib2.Request(url, None, HEADERS)
    page = urllib2.urlopen(req,None,5.0)
    soup = BeautifulSoup(page)
    l = soup.findAll('input')
    #toothpaste categoryId=5073, l[10]
    if int(l[10].get('value'))==5073:
        with open(RESULT_DATA_CSV,'a') as f:
            f.write('%s\n'%','.join([i.get('value') for i in l[1:37]]))
        return 1
    return 0

URL_PREFIX = "http://item.yhd.com/item/%s"
def foo():
    #get_head_row()
    id_base = 1222620
    count = 0
    hit = 0
    for i in xrange(20000):
        count += 1
        try:
            id = id_base + i
            r = get_data_row(URL_PREFIX%id)
            if r:
                hit += 1
        except Exception, e:
            #print id, 'shit', e, e.message
            pass
        if i%10 == 1:
            print '%s/%s'%(hit,count)
        print '============>',i, 'done', 'id:', id

def get_toothpaste():
    get_head_row()
    productIds = []
    count = 0
    hit = 0
    with open("yhd_pt_ids.csv") as f:
        content = f.readlines()
        for l in content:
            l=l.strip('\n').strip('\r')
            productIds.extend(l.split(','))
    for id in productIds:
        count+=1
        try:
            r = get_data_row(URL_PREFIX%id)
            if r:
               hit += 1
        except Exception, e:
            print id, 'shit', e, e.message
        if count%10 == 1:
            print '%s/%s'%(hit,count)
        print '============> done', 'id:', id

get_toothpaste()

