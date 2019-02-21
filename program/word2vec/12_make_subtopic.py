#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
BOLD    = '\033[1m'
UNDERLINE = '\033[4m'


from gensim.models.word2vec import Word2Vec
#model_path = 'word2vec.gensim.model'
model_path = 'text.model'
model = Word2Vec.load(model_path)
#query = input('please input query.')
from time import sleep

def make_suggest_vector(Suggest):
	try:
		vec = model[Suggest]
		return vec
	except:
		return 'no vector'
#For Vector has
dict_vector = {}
dict_suggest= {}
dict_ID     = {}
dict_topic  = {}
dict_prob   = {}
#For No Vector has
NoVec_ID      = {}
NoVec_suggest = {}
NoVec_topic   = {}
NoVec_prob    = {}

num = 0
a = open('LDA_suggest_merged.csv','r')
for i in a:
	num += 1
	LINE = i.rstrip().split(',')
	ID      = LINE[0]
	URL     = LINE[1]
	suggest = LINE[2]
	Topic   = LINE[3]
	Prob    = LINE[4]	
	len_sugg= len(suggest.split(' '))
	len_sugg_j = len(suggest.split(' '))
	if len_sugg >= 2:#  サジェストをスペースで区切った第一サジェストのみを使用
		Suggest = suggest.split(' ')[1]
	elif len_sugg_j>=2:
		Suggest = suggest.split(' ')[1]
	vector  =  make_suggest_vector(Suggest)
	if vector != 'no vector':
		dict_vector[URL] = vector
		dict_suggest[URL]= suggest
		dict_ID[URL]     = ID
		dict_topic[URL]  = Topic
		dict_prob[URL]   = Prob
	else:
		NoVec_ID[URL]      = ID
		NoVec_suggest[URL] = suggest
		NoVec_topic[URL]   = Topic
		NoVec_prob[URL]    = Prob
a.close()


#分散表現のないサジェストにおけるトピックで回す
NoVec_sub = {}
for suggest in NoVec_suggest.values():
	print ('NoVec_suggest=',suggest)
	#valueがsuggestのkeys(URLのリスト)をリスト型で返す
	URLs = list(filter(lambda x: NoVec_suggest[x] == suggest,NoVec_suggest.keys()))
	#上のURLリストに対応したtopic番号
	topics = [NoVec_topic[x] for x in list(filter(lambda x : x in URLs,NoVec_topic.keys()))]
	print(topics)
	#Subtopicを作れるtopic番号
	sub_topics = list(set([x for x in topics if topics.count(x) >= 3]))
	print(sub_topics)
	for tp in sub_topics:
		URL_per_topic = list(filter(lambda x: NoVec_topic[x] == tp,NoVec_topic.keys()))
		for URL in URL_per_topic:
			if NoVec_suggest[URL] == suggest:
				#トピック番号_サジェストのkey作成
				key = tp+'_'+suggest
				#トピックがtpでかつサジェストがsuggestのURLを保存
				NoVec_sub.setdefault(key,set()).add(URL)
				#print(CYAN,key,ENDC)
				#print(NoVec_sub[key])
	#print(NoVec_sub)
	#suggestでSubtopicになれるURLのリスト
	#sub_URLs =  [y for y in list(filter(lambda x: NoVec_topic[x] in sub_topics ,NoVec_topic.keys())) if NoVec_suggest[y] == suggest]
	#print(sub_URLs)
	#for topic in sub_topics:
	#	if NoVec_topic 
	#sleep(2)


#dict_subtopic[m] = sub_num # m: WebID, sub_num: subtopic num
#NoVec_topic_sb
c = open('NoVec_but_subtopic.csv','w')
NoVec_ID_list = NoVec_ID.values()
NoVec_but_sub_ID = []
for key in NoVec_sub:
	LINE = key.rstrip().split('_',2)
	topic   = LINE[0]
	suggest = LINE[1]
	#prob    = NoVec_prob
	URLs    = NoVec_sub[key]
	for URL in URLs:
		print(URL)
		print(NoVec_ID.keys())
		ID = NoVec_ID[URL]
		prob = NoVec_prob[URL]
		NoVec_but_sub_ID.append(ID)
		c.write(ID+','+URL+','+suggest+','+topic+','+prob+'\n')
c.close()

d = open('NoVec_and_bin.csv','w')
for ID in NoVec_ID_list:
	if ID not in NoVec_but_sub_ID:
		URL = [k for k, v in NoVec_ID.items() if v == ID][0]
		topic = NoVec_topic[URL]
		suggest = NoVec_suggest[URL]
		prob    = NoVec_prob[URL]
		d.write(ID+','+URL+','+suggest+','+topic+','+prob+'\n')
d.close()









num2 = 0
for URL in dict_vector:
	num2 += 1
	print('--------------------------------------------------')
	print(dict_ID[URL])
	print(BOLD+GREEN+URL+ENDC)
	print(CYAN+dict_suggest[URL]+ENDC)
	print(dict_topic[URL])
	print(dict_prob[URL])
	print(dict_vector[URL])
print(num)#num of row
print(num2)#num of row (suggest vector has)






################ make CosSim from the vector ######################
import numpy as np
def cos_sim(v1, v2):
	return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
dict_topic_URL_vector = {}
num_of_URL = 0
for URL in dict_topic:
	# トピック番号をkeyとして，リスト型に{URL:Vector}の辞書型を格納
	dict_topic_URL_vector.setdefault(dict_topic[URL],[]).append({URL:dict_vector[URL]})


dict_subtopic = {}
######## Proceed per topic ##################
for i in dict_topic_URL_vector:
	num_of_URL += len(dict_topic_URL_vector[i])
	dict_CosSim = {}
	tmp_list    = []
	Flag = 0
	print('--------------------------------------------------------')
	print('Topic=',GREEN,BOLD,i,ENDC)
	######### Proceed per URL ###########
	for n in dict_topic_URL_vector[i]:
		key_x = list(n.keys())[0]
		value_x = list(n.values())[0]
		for m in dict_topic_URL_vector[i]:
			key_y = list(m.keys())[0]
			value_y = list(m.values())[0]
			x = np.array(value_x)
			y = np.array(value_y)
			#print(cos_sim(x, y))
			#if key_x != key_y:
			# 現在のトピック番号に存在するURLのリストをkeyとして，各URLに対するその他のURLのCos類似度を辞書型に格納
			dict_CosSim.setdefault(key_x,[]).append({key_y:cos_sim(x, y)})

	######## Proceed per URL ##########
	lim = 0.7 #cos類似度の下限値をここで定めてる
	sub_list = []
	for URL in dict_CosSim:
		per_url_list = []
		per_url_list = dict_CosSim[URL] #各URLに対する他のURLのCos類似度{URL:CosSim}のリスト
		keys = []
		values = []
		for i in per_url_list:# i={url:CosSim}
			for key in i: # key=url
				value = i[key]# value=CosSim
				if value >= lim: #urlのCosSimがlimより大きければkeys[]にurlのIDを追加，values[]にCosSimを追加
					keys.append(dict_ID[key])
					values.append(value)
		#indexes = [i for i, x in enumerate(values) if x >= 0.7]
		#print(indexes)
		print(GREEN,BOLD,dict_ID[URL],ENDC,keys)
		#print(keys)
		print(BLUE,'CosSim--->',values,ENDC)
		tmp_list.append(keys)# tmp_list[]にkeys[]を追加（二次元配列）

		

	###### merge  the List of webID which is upper than 'lim' on CosSim ##########
	#print (tmp_list)
	sub_list = []
	cnt = 0
	for sub in tmp_list:# sub[]:CosSim >= 0.7 のIDリスト
		Flag=0
		if cnt==0:
			sub_list.append(sub)
			cnt=1
		else:
			for n in sub_list:# sub_list[sub[]], n = sub[]
				for ID in set(n):
					indexes = [i for i, x in enumerate(sub) if x == ID]
					if len(indexes)>=1 and Flag==0:
						Flag=1
						for p in sub:
							set(n).add(p)
		if Flag==0:
			sub_list.append(set(sub))
	del sub_list[0]
	subtopic = []
	subtopic_num = []
	sub_num = 1
	for n in sub_list:
		if len(n)>=3:# You need to change this number depend on definition of 'subtopic'
			subtopic.append(list(n))
			subtopic_num.append(sub_num)
			for m in list(n):
				dict_subtopic[m] = sub_num # m: WebID, sub_num: subtopic num
			sub_num += 1
	print('----------------------------------------------------------')
	print(BLUE,'[SUB_LIST]\n',ENDC,sub_list)	
	print(GREEN,'[SUBTOPIC]\n',ENDC,subtopic)
	print(RED,'[SUB_NUM]\n',ENDC,subtopic_num)
print(BLUE,'Num of URL -->',str(num),ENDC)
print(GREEN,'Num of URL having subtopic -->',str(num_of_URL),ENDC)
print(RED,'Num of No Vector suggest---->',str(len(NoVec_suggest.values())))
print(GREEN,'Program has successfully done!!. Please check subtopic.csv', ENDC)
#print(dict_subtopic)







############## Write the subtopic to file #############
b = open('subtopic.csv','w')
b.write('ID,URL,suggest,topic,probability,subtopic\n')
#bin_cnt = 100
for URL in dict_ID:
	ID      = dict_ID[URL]
	suggest = dict_suggest[URL]
	topic   = dict_topic[URL]
	prob    = dict_prob[URL]
	try:# Whether the Webpage has subtopic or not
		sub= dict_subtopic[ID] #ID: WebID, dict_subtopic[ID]:subtopic_num
	except:
		sub= 100
		#bin_cnt += 1
	b.write(str(ID)+','+str(URL)+','+str(suggest)+','+str(topic)+','+str(prob)+','+str(sub)+'\n')


b.close()

