#coding:utf-8
import csv
import sys
import codecs
import math
import random
from time import sleep

a = open('data/test1.html','r')
b = open('data/topic_title.txt','w')


for i in a:
	i = i.rstrip()
	if 'class="suggest_list_small_class"' in i:
		i = i.split('">',2)[1].split('</div>',2)[0]
		#i = i[1]
		#i = i.replace('</div>','')
		print (i)
		b.write(i+'\n')

		
	#sleep(0.01)
a.close()
b.close()
