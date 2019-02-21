#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
from operator import itemgetter


a = open('result_of_lda.csv','r')
b = open('sorted.csv','w')
b.write('page_id,url,suggest,topic,probability\n')
dataset = []
cnt = 0
for i in a:
    if cnt>=1:
        row = i.rstrip().split(',')
        row[3] = int(row[3])
        row[4] = float(row[4])
        print (row)
        dataset.append(row)
    cnt += 1
dataset.sort(key=itemgetter(4),reverse=True)
dataset.sort(key=itemgetter(3))



for n in dataset:
    print (n[0]+'\n'+n[1]+'\n'+n[2]+'\n'+str(n[3])+'\n'+str(n[4])+'\n'+'______________________________')
    b.write(n[0]+','+n[1]+','+n[2]+','+str(n[3])+','+str(n[4])+'\n')
a.close()
b.close()
