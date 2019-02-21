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
from time import sleep              #To sleep
import requests                     #request HTML from URL
from operator import itemgetter     #sort by factor



dict_url        = {}
dict_predict    = {}
dict_true       = {}
dict_confidence = {}
ID_list         = []

a = open('data/svm_input.csv','r')
b = open('data/svm_output.csv','r')


for i in a:
	#print i.rstrip()
	url = i.rstrip().split(',')[0]
	ID  = i.rstrip().split(',')[1]
	dict_url[ID] = url
	ID_list.append(ID)



for i in b:
	#print i.rstrip()
	ID         = i.rstrip().split(',')[0]
	true       = i.rstrip().split(',')[1]
	predict    = i.rstrip().split(',')[2]
	confidence = i.rstrip().split(',')[3]
	
	dict_predict[ID]    = predict
	dict_true[ID]       = true
	dict_confidence[ID] = confidence

a.close()
b.close()




c = open('data/domain.csv','w')
for i in ID_list:
	if i != 'id':
		print ''
		print i                 # id
		print dict_url[i]       # url
		print dict_true[i]      # true
		print dict_predict[i]   # predict
		print dict_confidence[i]# confidence
		string = str(i)+','\
			+str(dict_url[i])+','\
			+str(dict_true[i])+','\
			+str(dict_predict[i])+','\
			+str(dict_confidence[i])+'\n'
		c.write(string)
		print OKGREEN +str(string.rstrip()) + ENDC
c.close()



