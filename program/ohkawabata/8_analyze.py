#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
BOLD    = '\033[1m'
UNDERLINE = '\033[4m'
from operator import itemgetter
from time import sleep

query = input(GREEN+'Please input the query\n-->'+ENDC)
c = open('id-suggest.csv','r')
dict_id_suggests = {}
for row in c:
	LINE = row.rstrip().split(',',1)
	ID   = LINE[0]
	Sugg = LINE[1].split(',')
	print(Sugg)
	dict_id_suggests[ID] = Sugg
c.close()







a = open('sorted.csv','r')
dataset = []
dict_suggest = {}
cnt = 0
for i in a:
    if cnt >= 1:
        row = i.rstrip().split(',')
        page_id = row[0]
        url     = row[1]
        suggest = row[2]
        topic   = row[3]
        prob    = row[4]
        for suggest in dict_id_suggests[page_id]:
            dict_suggest.setdefault(topic, []).append(suggest)
    cnt += 1
a.close()



b = open('analyzed.csv','w')
for key in dict_suggest.keys():
    print (GREEN+BOLD+key+ENDC)
    b.write(key+',')
    dict_suggest_indexes = {}
    values = dict_suggest[key]

    for suggest in values:
        indexes = [i for i, x in enumerate(values) if x == suggest]
        dict_suggest_indexes[suggest] = len(indexes)


    title = ''
    suggest_list = sorted(dict_suggest_indexes.items(), key=lambda x:x[1],reverse=True)
    if len(suggest_list) >= 3:
        title = suggest_list[0][0]+'・'+suggest_list[1][0]+'・'+suggest_list[2][0]
    elif len(suggest_list) == 2:
        title = suggest_list[0][0]+'・'+suggest_list[1][0]
    else:
        title = suggest_list[0][0]
    title = title.replace(query+' ','')
    #print (suggest_list)
    print (CYAN+BOLD+title+ENDC)
    b.write(title+',,\n')





    for k, v in sorted(dict_suggest_indexes.items(), key=lambda x:x[1],reverse=True):
        print (k, v)
        b.write(',,'+k+','+str(v)+'\n')

    print (PURPLE+'num_of_suggest-->'+str(len(dict_suggest_indexes))+ENDC)
    print ('_______________________________')
    
    
b.close()
