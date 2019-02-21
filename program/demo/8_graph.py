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
from urlparse import urlparse #URL --> Domain
from time import sleep
from operator import itemgetter     #sort by factor
import numpy as np
import matplotlib.pyplot as plt
# ラベルを日本語対応にするのに必要
font = {'family': 'AppleGothic'}
plt.rc('font', **font)




#################### TOPIC #######################
a = open('data/4.csv','r')
# id, title, domain, truth, confidence, page, topic, topics
c = open('graph/graph_topic.csv','w')
c.write('Ranking,Num_of_seikai,Rate_of_Seikai\n')
seikai_list = []
num_list = []
rate_list = []
count_list = []
num = 0
for i in a:
	num = num+1
	truth = int(i.rstrip().split(',',7)[3])
	if truth == 1:
		seikai_list.append(truth)
	num_of_seikai = len(seikai_list)
	rate = float(num_of_seikai)/float(num)
	print 'num=',num
	print 'seikai=',num_of_seikai
	print 'rate=',rate
	print ''
	c.write(str(num)+','+str(num_of_seikai)+','+str(rate)+'\n')
	num_list.append(num)
	rate_list.append(rate)
	count_list.append(num_of_seikai)

a.close()
c.close()
#print num_list
num_list_per_5 = []
rate_list_per_5= []
for num in num_list:
	if num % 5 == 0:
		num_list_per_5.append(num)
		rate_list_per_5.append(rate_list[num-1])
		





################## Confidence ###################
b = open('data/4.csv','r')
d = open('graph/graph_conf.csv','w')
d.write('Ranking,Num_of_seikai,Rate_of_Seikai\n')
num2 = 0
file_list = []
for i in b:
	num2 = num2+1
	I = i.rstrip().split(',',7)
	I[3] = int(I[3])
	I[4] = float(I[4])
	I[5] = int(I[5])
	file_list.append(I)
b.close()
file_list.sort(key=itemgetter(4),reverse=True)
count_seikai=0
num3=0
rate_list2 = []
count_list2= []
for row in file_list:
	num3+=1
	truth = row[3]
	if truth == 1:
		count_seikai+=1
	rate = float(count_seikai)/float(num3)
	rate_list2.append(rate)
	count_list2.append(count_seikai)
	#print 'num=',num3
	#print 'seikai=',count_seikai
	#print 'rate=',rate
	#print ''
	d.write(str(num3)+','+str(count_seikai)+','+str(rate)+'\n')
d.close()

#num_list_per_5 = []
rate_list_per_5_conf= []
for num in num_list:
	if num % 5 == 0:
		#num_list_per_5.append(num)
		rate_list_per_5_conf.append(rate_list2[num-1])





################## PAGE #####################
e = open('graph/graph_page.csv','w')
e.write('Ranking,Num_of_seikai,Rate_of_seikai\n')
file_list.sort(key=itemgetter(5),reverse=True)
#print file_list
count_seikai=0
num3 = 0
rate_list3 = []
count_list3= []
for i in file_list:
	num3+=1
	truth = i[3]
	if truth == 1:
		count_seikai+=1
	rate = float(count_seikai)/float(num3)
	rate_list3.append(rate)
	count_list3.append(count_seikai)
	#print 'num=',num3
	#print 'seikai=',count_seikai
	#print 'rate=',rate
	#print ''
	e.write(str(num3)+','+str(count_seikai)+','+str(rate)+'\n')
e.close()
rate_list_per_5_page= []
for num in num_list:
 	if num % 5 == 0:
	#num_list_per_5.append(num)
		rate_list_per_5_page.append(rate_list3[num-1])











X = np.array(num_list)
Y = np.array(count_list)
Y2= np.array(count_list2)
Y3= np.array(count_list3)
#Y = np.array(rate_list)
#X = np.array(num_list_per_5)
#Y = np.array(rate_list_per_5)
#Y2= np.array(rate_list_per_5_conf)
#Y3= np.array(rate_list_per_5_page)
#plt.title(u'ランキングの種類とノウハウサイトの相関',fontsize=12)
#plt.xlabel(u'出力順位',fontsize=20)
#plt.ylabel(u'正解数',fontsize=20)
#plt.plot(X,Y,label = u"トピック数でランキング",marker='.',linewidth = 4.0,ms=10)
#plt.plot(X,Y2,label=u'信頼度でランキング',marker='.',linewidth = 2.0,ms=10)
#plt.plot(X,Y3,label=u'ページ数でランキング',marker='.',linewidth = 1.0,ms=10)
#plt.plot(X,Y,marker='.',linewidth = 6.0,ms=20)
#plt.plot(X,Y2,marker='.',linewidth = 4.0,ms=15)
#plt.plot(X,Y3,marker='.',linewidth = 2.0,ms=10)
plt.plot(X,Y,marker='.')
plt.plot(X,Y2,marker='.')
plt.plot(X,Y3,marker='.')

#plt.ylim(0.0, 1.0)
#plt.xlim(0,90)
plt.ylim(0,60)
plt.legend(loc='lower right')
#plt.legend() # 凡例を表示
plt.tick_params(labelsize=20)
plt.grid()
plt.savefig('Soukan.png',format = 'png', dpi=400)
#plt.plot(X,Y2,"r",label='confidence',marker='.')
plt.show()

