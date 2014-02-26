from __future__ import with_statement
import urllib2
from BeautifulSoup import BeautifulSoup
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

def set_head_row():
    with open("jd_data.csv",'a') as f:
        f.write('%s\n'%','.join(["jd_id", "title", "info", "img_url"]))

def get_data_row(url_prefix, id):
    id = str(id)
    url = url_prefix%id
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    
    #product img url
    div = soup.find('div',{'id': 'preview'})
    img = div.find('img')
    img_url = img.get('src')

    #product info
    div = soup.find('div',{'class': 'mc',"id":"product-detail-1"})
    lis = div.findAll('li')
    title = lis[0].get('title')
    print title
    info = ';'.join([l.getText() for l in lis])

    with open("jd_data.csv",'a') as f:
        f.write('%s\n'%','.join([id, title, info, img_url]))

url_prefix = "http://item.jd.com/%s.html"
#set_head_row()
id_base = 650259
for i in xrange(-710,1000):
    try:
        id = id_base + i
        get_data_row(url_prefix, id)
        time.sleep(0.1)
    except Exception, e:
        print id, 'shit', e
    print '============>', i, id, 'done'