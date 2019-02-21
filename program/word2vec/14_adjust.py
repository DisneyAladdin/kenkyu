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


dict_topic_max = {}#各topicごとの，サブトピック番号の最大値
dict_topic_suggests = {}#各topicごとの，Binに分類されたサジェストのリスト
dict_topic_ids = {} #各topicごとの，Binに分類されたidのリスト

a = open('subtopic2.csv','r')
pre_topic = '0'#最初のトピックが0だから
MAX = 0
#Flag = 0
for i in a:
	LINE = i.rstrip().split(',')
	ID   = LINE[0]
	URL  = LINE[1]
	sugg = LINE[2]
	topic= LINE[3]
	prob = LINE[4]
	sub  = int(LINE[5])

	if topic != pre_topic:
		MAX = 0	
		dict_topic_max[topic] = MAX

	if sub!=100 and sub>MAX:
		MAX = sub
		dict_topic_max[topic] = MAX

	if sub==100:
		dict_topic_suggests.setdefault(topic,[]).append(sugg)
		dict_topic_ids.setdefault(topic,[]).append(ID)

	pre_topic = topic
	#print(topic,dict_topic_max[topic])	
a.close()

#print(dict_topic_suggests)



dict_id_sub = {}
for topic in dict_topic_suggests:#topicごとに
	print (GREEN,topic,ENDC)
	subtopic = dict_topic_max[topic]
	for suggest in set(dict_topic_suggests[topic]):#suggestごとに（サジェストの重なりなし）
		index = [i for i, x in enumerate(dict_topic_suggests[topic]) if x == suggest]#同じサジェストのインデックス[]を返す
		if len(index)>=3:#3つ以上でサブトピック
			subtopic += 1
			for fac in index:
				print('id',dict_topic_ids[topic][fac])
				print('suggest',dict_topic_suggests[topic][fac])
				print('sub',CYAN,subtopic,ENDC)	
				dict_id_sub[dict_topic_ids[topic][fac]] = subtopic




b = open('subtopic2.csv','r')
c = open('subtopic3.csv','w')
dataset = []
for i in b:
	LINE = i.rstrip().split(',')
	ID   = LINE[0]
	URL  = LINE[1]
	sugg = LINE[2]
	topic= int(LINE[3])
	prob = LINE[4]
	sub  = int(LINE[5])
	
	if ID in dict_id_sub.keys():
		sub = dict_id_sub[ID]
		#print (sub)	
	row = [ID,URL,sugg,topic,prob,sub]
	dataset.append(row)
	
	#c.write(ID+','+URL+','+sugg+','+topic+','+prob+','+sub+'\n')

b.close()
#c.close()

dataset.sort(key=itemgetter(5)) #サブトピックでソート
dataset.sort(key=itemgetter(3)) #トピックでソート

for row in dataset:
	row_str = ",".join(map(str,row))
	c.write(row_str+'\n')
c.close()

