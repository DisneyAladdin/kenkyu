#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
BOLD    = '\033[1m'
UNDERLINE = '\033[4m'


####### ID---Suggests[] ####################
dict_id_suggests = {}
e = open('id-suggest.csv','r')
for i in e:
	LINE     = i.rstrip().split(',',1)
	ID       = LINE[0]
	suggests = LINE[1].split(',')
	dict_id_suggests[ID] = suggests
	print (dict_id_suggests[ID])
e.close()





###### LDA の結果を読み込み ##############
a = open('result_of_lda.csv','r')
dict_ID      = {}
dict_Suggest = {}
dict_Topic   = {}
dict_Prob    = {}
num = 0
for i in a:
	if num >= 1:
		LINE = i.rstrip().split(',')
		Id   = LINE[0]
		URL  = LINE[1]
		#Suggest = LINE[2]
		suggests = dict_id_suggests[Id]
		Topic = LINE[3]
		Prob  = LINE[4]
		Prob = float(Prob)
		#print(URL)
		#print(Suggest)
		dict_ID.setdefault(URL,[]).append(Id)
		for suggest in suggests:
			dict_Suggest.setdefault(URL,[]).append(suggest)
		dict_Topic.setdefault(URL,[]).append(Topic)
		dict_Prob.setdefault(URL,[]).append(Prob)
	num += 1
a.close()






# サジェスト頻度の読み込み
dict_Freq = {}
b = open('analyzed.csv','r')
#num = 0
for i in b:
	LINE = i.rstrip().split(',')
	if LINE[0].isdecimal() == False: # トピックタイトルの行はスキップ
		Suggest = LINE[2]
		Freq    = LINE[3]
		Freq = int(Freq)
		#print(Suggest,Freq)
		dict_Freq[Suggest] = Freq
	#num += 1
#print(dict_Freq)
b.close()









# URL--Freqのディクショナリの作成
dict_URL_Freq = {}
for i in dict_Suggest:
	Freq_list    = []
	Suggest_list = dict_Suggest[i]#####[suggest1, suggest2,...,suggestN]
	for n in Suggest_list:
		dict_URL_Freq.setdefault(i,[]).append(dict_Freq[n])#i=URL, n=suggest, dict_Freq[n]=Frequency
	



#print (dict_ID)


# サジェスト頻度最大のサジェストを代表サジェストにする
dict_ID_suggests = {}
c = open('LDA_suggest_merged.csv','w')
f = open('sorted.csv','r')
num = 0
#for n in dict_URL_Freq:#n=URL
for row in f:	
	num += 1
	if num > 1:# 最初の行（インデックス）をスキップ
		LINE = row.rstrip().split(',')
		ID   = LINE[0]
		URL  = LINE[1]
		sugg = LINE[2]
		topic= LINE[3]
		prob = LINE[4]
		index = [i for i, x in enumerate(dict_URL_Freq[URL]) if x == max(dict_URL_Freq[URL])]
		index = int(index[0]) # 二つ以上ある場合はindex番号が小さいものを優先
		suggest = dict_Suggest[URL][index]
		#ID      = dict_ID[n][index]
		#topic   = dict_Topic[n][index]
		#prob    = dict_Prob[n][index]
		print(GREEN+ID+ENDC)
		print(BLUE+URL+ENDC)
		print(dict_Suggest[URL])
		print(dict_URL_Freq[URL])
		print(suggest)
		print('------------------')
		c.write(str(ID)+','+URL+','+suggest+','+topic+','+prob+'\n')
		##### ID,[suggest1,suggest2,suggest3....] ########
		dict_ID_suggests[ID] = dict_Suggest[URL]
c.close()
f.close()


