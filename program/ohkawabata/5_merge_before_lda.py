#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
BOLD    = '\033[1m'
UNDERLINE = '\033[4m'


######  読み込み ##############
a = open('mecabed.csv','r')
dict_ID      = {}
dict_Suggest = {}
dict_content = {}
num = 0
for i in a:
	if num >= 1:
		LINE = i.rstrip().split(',')
		Id   = LINE[0]
		URL  = LINE[1]
		suggest = LINE[2]
		content = LINE[3]
		dict_ID.setdefault(URL,[]).append(Id)
		dict_Suggest.setdefault(URL,[]).append(suggest)
		dict_content.setdefault(URL,[]).append(content)
	num += 1
a.close()





# サジェスト頻度最大のサジェストを代表サジェストにする
#dict_URL_suggests = {}
c = open('mecabed.csv','w')
for URL in dict_ID:	
	ID         = dict_ID[URL][0]
	suggest    = dict_Suggest[URL][0]
	content    = dict_content[URL][0]
#	dict_URL_suggests[URL] = dict_Suggest[URL]
	print(GREEN+ID+ENDC)
	print(BLUE+URL+ENDC)
	print(suggest)
	print('------------------')
	c.write(ID+','+URL+','+suggest+','+content+'\n')
	##### ID,[suggest1,suggest2,suggest3....] ########
c.close()
#f.close()





d = open('id-suggest.csv','w')
for URL in dict_Suggest:
	ID = dict_ID[URL][0]
	value = set(dict_Suggest[URL])
	#print(ID,value)
	string = ''
	for n in value:
		string += ','+n 
	print(ID,string)
	d.write(ID+string+'\n')
d.close()
	

