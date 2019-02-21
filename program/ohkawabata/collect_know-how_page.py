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


def request(url,try_cnt):
	try:
		req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		html = urllib.request.urlopen(req)
		text = soup(html)
		text = text.replace(',',' ').replace('\n',' ').replace('\t','').replace('\r','')
		print (text[:50]+'...')
		return text

	except Exception as e:
		sleep(0.5)
		try_cnt += 1
		if try_cnt <= 2:
			request(url,try_cnt)
		else:
			print ('server error occured')






a = open('domain.csv','r')
for url in a:
	if cnt > 0:
		try_cnt = 0
		text = request(url,try_cnt)
	cnt += 1
