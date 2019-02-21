#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
from operator import itemgetter


a = open('subtopic5.csv','r')
b = open('subtopic2.csv','w')
#b.write('id,url,suggest,topic,probability,subtopic\n')
dataset = []
cnt = 0
for i in a:
    if cnt>=1:
        row = i.rstrip().split(',')
        row[3] = int(row[3])
        row[4] = float(row[4])
        row[5] = int(row[5])
        print (row)
        dataset.append(row)
    cnt += 1
#dataset.sort(key=itemgetter(5),reverse=True)
dataset.sort(key=itemgetter(5))#subtopic
dataset.sort(key=itemgetter(3))#topic



for n in dataset:
    print (n[0]+'\n'+n[1]+'\n'+n[2]+'\n'+str(n[3])+'\n'+str(n[4])+'\n'+'______________________________')
    b.write(n[0]+','+n[1]+','+n[2]+','+str(n[3])+','+str(n[4])+','+str(n[5])+'\n')
a.close()
b.close()
