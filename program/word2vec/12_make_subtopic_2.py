#coding:utf-8

a = open('subtopic.csv','r')
b = open('NoVec_but_subtopic.csv','r')
c = open('NoVec_and_bin.csv','r')

dict_topic_sub = {}#key=topic, value=set_of_subtopic
num=0
for i in a:
	num+=1
	if num>1:
		LINE = i.rstrip().split(',')
		topic = LINE[3]
		sub   = LINE[5]
		if sub != '100':
			dict_topic_sub.setdefault(topic,set()).add(int(sub))






dict_topic_maxsub = {}#key=topic, value=max_num_of_subtopic
for topic in dict_topic_sub:
	if len(dict_topic_sub[topic]) >= 1:
		maxsub_in_topic = max(list(dict_topic_sub[topic]))
		#print(maxsub_in_topic)
		dict_topic_maxsub[topic] = maxsub_in_topic
	else:
		dict_topic_maxsub[topic] = 0
		



d = open('NoVec_subtopic.csv','w')
pre_suggest = ''
for i in b:
	LINE = i.rstrip().split(',')
	ID      = LINE[0]
	URL     = LINE[1]
	suggest = LINE[2]
	topic   = LINE[3]
	prob    = LINE[4]
	try:
		maxsub  = dict_topic_maxsub[topic]
	except:
		maxsub  = 0
	#print (maxsub)
	sub     = 0
	if suggest != pre_suggest:
		sub = maxsub + 1
		dict_topic_maxsub[topic] = sub #topicのmax_num_of_subtopicを更新
	else:
		sub = maxsub
		
	d.write(ID+','+URL+','+suggest+','+topic+','+prob+','+str(sub)+'\n')
	pre_suggest = suggest
d.close()




e = open('NoVec_bin.csv','w')
for i in c:
	LINE = i.rstrip().split(',')
	ID      = LINE[0]
	URL     = LINE[1]
	suggest = LINE[2]
	topic   = LINE[3]
	prob    = LINE[4]
	sub     = 100
	e.write(ID+','+URL+','+suggest+','+topic+','+prob+','+str(sub)+'\n')
e.close()







a.close()
b.close()
c.close()
