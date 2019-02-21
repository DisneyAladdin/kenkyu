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
import timeout_decorator

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





def soup(html):
    soup = BeautifulSoup(html, "html.parser")
    soup_title = soup.find_all("title")
    soup_h1 = soup.find_all("h1")
    soup_h2 = soup.find_all("h2")
    soup_h3 = soup.find_all("h3")
    soup_h4 = soup.find_all("h4")
    soup_h5 = soup.find_all("h5")
    soup_h6 = soup.find_all("h6")
    soup_a = soup.find_all("a")
    soup_p = soup.find_all("p")
    soup=soup_title+soup_h1+soup_h2+soup_h3+soup_h4+soup_h5+soup_h6+soup_a+soup_p

    maped_list = map(str, soup)
    soup1 = ' '.join(maped_list)
    soup2 = BeautifulSoup(soup1, "html.parser")
    text = soup2.get_text()
    return str(text)






def request(url,try_cnt):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        text = extractor(html)
        text = text.replace(',',' ').replace('\n',' ').replace('\t','').replace('\r','')
        print (text[:50]+'...')
        return text

    except Exception as e:
        sleep(0.1)
        try_cnt += 1
        if try_cnt <= 1:
            request(url,try_cnt)
        else:
            print ('server error occured')






# main function
a = open('sg_urls.csv','r')
b = open('webpage.csv','w')
b.write('page_id,url,suggest,contents\n')
# just in case
#c = open('id-content.csv','w')
#c.write('page_id,content\n')



cnt = 0
for i in a:
    #print (GREEN + str(cnt) + ENDC)
    if cnt > 0:
        LINE = i.rstrip().split(',')
        web_id = LINE[0]
        url    = LINE[1]
        suggest= LINE[2]
        try_cnt= 0
        print (GREEN+str(web_id)+ENDC)
        print (BLUE+url+ENDC)
        print (CYAN+suggest+ENDC)
        #timeout_decorator.timeout(5)
        #req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        #html = urllib.request.urlopen(req)
        #text = soup(html)
        #text = text.replace(',',' ').replace('\n',' ').replace('\t','').replace('\r','')
        if '.pdf' in url:
            print('Because of PDF file, skipped\n')
        else:
            #@timeout_decorator.timeout(30)
            timeout_decorator.timeout(5)
            try:
                text = request(url,try_cnt)
                #print (text[:50]+'...')
                #print(chardet.detect(text))
                print ('')
                b.write(str(web_id)+','+url+','+suggest+','+str(text)+'\n')
                #c.write(str(web_id)+','+str(text)+'\n')
            except:
                print ('time error')
        sleep(0.5)
    cnt += 1
a.close()
b.close()
#c.close()




#url = "https://to-kei.net"
#req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#html = urllib.request.urlopen(req)
#text = soup(html)
#text = text.replace(',',' ')
#print(text)
