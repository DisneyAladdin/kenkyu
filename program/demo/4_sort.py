#coding:utf-8
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
import math
import random
from urllib.parse import urlparse       #URL --> Domain
from time import sleep              #To sleep
import requests                     #request HTML from URL
from operator import itemgetter     #sort by factor
import matplotlib.pyplot as plt     #Graph 
import numpy as np                  #Graph






a = open('data/result.csv','r')
LIST = []
conf = []
num = 0
for i in a:
	if num != 0:
		LINE = i.rstrip().split('\t')
		#domain_id = LINE[0]
		#title     = LINE[1]
		#predict   = LINE[2]
		#confidence= LINE[3]
		#sum_page  = LINE[4]
		#sum_topic = LINE[5]
		#topics    = LINE[6]
		#truth     = LINE[7]
		#LINE[1] = LINE[1].encode('utf-8')	
		LINE[3] = float(LINE[3])
		LINE[4] = int(LINE[4])
		LINE[5] = int(LINE[5])
		LINE[7] = int(LINE[7])
		LIST.append(LINE)
		conf.append(LINE[3])
	num += 1
#print LIST	
LIST.sort(key=itemgetter(3),reverse=True)
max_conf = max(conf)
min_conf = min(conf)/max_conf
a.close()
#print 'max_conf=' + str(max_conf)

# 正規化
for row in LIST:
	row[3] = row[3]/max_conf
print (LIST)



#cnt = 0
num_2 = 0
# ここで下限値を指定，，0.5, 0, 最小値と0の間, 最小値
lim_list = [0.5,0,min_conf/2,min_conf]
for n in lim_list:
	cnt = 0
	list_2 = []
	num_2 += 1
	for i in LIST:
		#i[3] = i[3]/max_conf
		if i[3] >= n:# while 'confidence' is more than n
			#i[3] = i[3]/max_conf
			list_2.append(i)	
			cnt += 1
			#domain_id = i[0]
			#title     = i[1]
			#confidence= float(i[3])
			#sum_page  = int(i[4])
			#sum_topic = int(i[5])
			#print cnt
			#print title
			#print confidence/max_conf # 正規化
			#print sum_page
			#print sum_topic
			#print ''
	list_2.sort(key=itemgetter(4),reverse=True)# ページ数でソート
	list_2.sort(key=itemgetter(5),reverse=True)# トピック数でソート
	#print num_2
	exec("b = open('data/%d.csv','w')" %(num_2))
	for line in list_2:
		string = str(line[0])+','+str(line[1])+','+str(line[8])+','+str(line[7])+','+str(line[3])+','+str(line[4])+','+str(line[5])+','+str(line[6])
		b.write(string+'\n')
	b.close()
	for i in list_2:
		print (i[1])
		print (i[8])
		print (i[7])
		print (i[3])
		print (i[5])
		print (i[4])
		print ('')
	print ('\n\n')
print ('max_conf='+str(max_conf))
print ('min_conf='+str(min_conf))
#print list_2


#print LIST
