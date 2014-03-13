from __future__ import with_statement
import urllib2
from BeautifulSoup import BeautifulSoup
import simplejson as json
from pyquery import PyQuery as pq
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8') 
HEADERS = {'User-Agent':'Mozilla/5.0'}
key = 'c5073-%E7%89%99%E8%86%8F'
search_template = "http://www.yhd.com/ctg/s2/%s/b/a-s1-v0-p%s-price-d0-f0-m1-rt0-pid-mid0-k/"
productIds = []
for id in xrange(1,32):
    url = search_template%(key,id)
    print url
    req = urllib2.Request(url, None, HEADERS)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    l = soup.findAll('search_item')
    inputValue = soup.find('input',{"id":"jsonValue"})
    jsonValue = inputValue.get('value')
    search_result = json.loads(jsonValue)
    with open("yhd_pt_ids.csv",'a') as f:
        f.write('%s\n'%search_result['extField7']) 
    print 'page %s done'%id, search_result['currentPage']