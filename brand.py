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
get_head_row()
id_base = 1810581
for i in xrange(10000):
    try:
        id = id_base + i
        get_data_row(url_prefix%id)
    except Exception, e:
        print id, 'shit'
    print '============>',i, 'done'
			


div0 = soup.find("div", { "class" : "layout_w1200_g22 laymt"})
div1 = div0.find("div", { "class" : "grid_18"})
div2 = div1.findAll("div", { "class" : "des"})
div3 = div2[1].findAll("div", { "class" : "descon"})
div4 = div3.find("div", { "class" : "desitem"})


for tag in soup.find_all('dl', class_='des_info clearfix'):
        m_order = int(tag.find('td', class_='m_order').get_text())
        m_name = tag.a.get_text()
        m_year = tag.span.get_text()
        m_rating_score = float(tag.em.get_text())
        m_rating_num = int(tag.find(headers="m_rating_num").get_text())
        print("%s %s %s %s %s" % (m_order, m_name, m_year, m_rating_scor