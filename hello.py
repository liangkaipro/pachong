# -* coding:utf-8 *-
import urllib2,urllib
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


x=0

def crawl(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib2.Request(url,headers=headers)
    page = urllib2.urlopen(req,timeout=20)#设置超时
    contents = page.read()#获取源码
    soup = BeautifulSoup(contents,'html.parser')
    my_girl = soup.find_all('img')
    for girl in my_girl:
        link = girl.get('src')
        print link

        global  x
        urllib.urlretrieve(link,'doc\%s.jpg' % x)
        x+=1
        print("正在下载第%s张" % x)
for page in range(1,5):
    page+=1
    url = 'http://www.dbmeinv.com/?pager_offset-%s' % page
    crawl(url)










