#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
import urllib.request, urllib.error
from urllib.request import Request, urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
from time import sleep
from extractcontent3 import ExtractContent
import requests
import chardet #Confirm the codec
import re#正規表現
import random
from urllib.parse import urlparse


##### ExtractContent （本文のみ抽出）########
def extractor(html):
    extractor = ExtractContent()
    # オプション値を指定する
    opt = {"threshold":50}
    #extractor.set_default(opt)
    #html = open("index.html").read() # 解析対象HTML
    extractor.analyse(html)
    text, title = extractor.as_text()
    html, title = extractor.as_html()
    title = extractor.extract_title(html) 
    #print(text)
    return text




# 今はつかってない
def soup(html):
    if '<title>' in html:
    	title   = html.split('<title>',2)[1].split('</title>',2)[0].replace(',',' ')
    else:
        title   = 'NULL'
    if '<meta name="description"  content="' in html:
        snippet = html.split('<meta name="description"  content="',2)[1].split('" />',2)[0].replace(',',' ')
    else:
        snippet = 'NULL'
    if '<meta name="keywords"  content="' in html:
        keywords= html.split('<meta name="keywords"  content="',2)[1].split('" />',2)[0].replace(',',' ')
    else:
        keywords= 'NULL'
    #r = re.search( '(%s.*%s)' % ('<title>','</title>'), flags=re.DOTALL)
    #m = r.search(bs_obj)
    #ret = m.group(0)
    #snippet = re.search(r'%s(.*)?%s'%('<meta name="description"','"'), html)
    #soup = BeautifulSoup(html, "html.parser")
    #title = soup.find_all("title")
    #snippet = soup.find_all('meta', attrs={'name': 'description', 'content': True})[0]
    #suggest = soup.find_all("keywords")
    #print(title)
    print(GREEN+title+ENDC)
    print(CYAN+snippet+ENDC)
    print(PURPLE+keywords+ENDC)
    #print(suggest)
    #soup_h1 = soup.find_all("h1")
    #soup_h2 = soup.find_all("h2")
    #soup_h3 = soup.find_all("h3")
    #soup_h4 = soup.find_all("h4")
    #soup_h5 = soup.find_all("h5")
    #soup_h6 = soup.find_all("h6")
    #soup_a = soup.find_all("a")
    #soup_p = soup.find_all("p")
    #soup=soup_title+soup_h1+soup_h2+soup_h3+soup_h4+soup_h5+soup_h6+soup_a+soup_p

    #maped_list = map(str, soup)
    #soup1 = ' '.join(maped_list)
    #soup2 = BeautifulSoup(soup1, "html.parser")
    #text = soup2.get_text()
    return title, snippet, keywords






def request(url,try_cnt):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    html = r.text
    title,snippet,keywords = 'title','snippet','keywords'
    text = extractor(html) #Extract Content
    text = text.replace(',',' ').replace('\n',' ').replace('\t','').replace('\r','')
    print (text+'...')
    return text, title, snippet, keywords






# main function
#a = open('domains.csv','r')
url_list = []
with open('all_url_list.txt','r') as f:
    url_list = f.read().split("\n")

random.shuffle(url_list)

b = open('webpage.csv','w')
b.write('id,url,keywords,title,snippet,contents\n')
# just in case
#c = open('id-content.csv','w')
#c.write('page_id,content\n')

cnt = 0
#for i in a:
bef_domain = ''
for i in url_list:
    if cnt >= 0:
        web_id = 'N'+str(cnt)
        url    = i.rstrip()
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(url))
        if domain == bef_domain:
            sleep(1)
        try_cnt= 0
        print (GREEN+str(web_id)+ENDC)
        print (BLUE+url+ENDC)
        if '.pdf' in url:
            print('Because of PDF file, skipped\n')
        else:
            try:
                text, title, snippet, keywords = request(url,try_cnt)
                print ('')
                b.write(web_id+','+url+','+keywords+','+title+','+snippet+','+text+'\n')
            except:
                print(RED,'server error occured',ENDC)
        bef_domain = domain
    cnt += 1
a.close()
b.close()
