#coding:utf-8
from time import sleep
a = open('NoVec_and_bin.csv','r')
set_suggest = set()
for i in a:
	LINE = i.rstrip().split(',')
	suggest = LINE[2]
	set_suggest.add(suggest)
	#print(suggest)
	#sleep(0.1)
print(len(set_suggest))
a.close()	
