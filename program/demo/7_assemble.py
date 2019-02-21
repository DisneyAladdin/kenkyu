# coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'
import csv
import sys
import codecs
from urllib.parse import urlparse #URL --> Domain
from time import sleep


def main(n):
	a = open('data/topic_title.txt','r')
	#exec("b = open('data/mainpage_%d.html','r')" %(n))
	b = open('data/mainpage_'+str(n)+'.html','r')
	#exec("c = open('data/mainpage_rev_%d.html','w')" %(n))
	c = open('data/mainpage_rev_'+str(n)+'.html','w')

	dict_topic_title = {}
#num = 0

	for i in a:
		#num = num + 1
		num = int(i.split('(topic:')[1].split(')')[0])
		dict_topic_title[num] = i.rstrip().split('(topic:')[0]


	for n in b:
		if 'topic:' in n:
			topicNum = int(n.split('topic:')[1].split('-->')[0])
			print (topicNum)
			n = n.replace('Topic'+str(topicNum),dict_topic_title[topicNum])
			c.write(n)
		else:
			c.write(n)
	a.close()
	b.close()
	c.close()



for n in range(1,5):
	main(n)
