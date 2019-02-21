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
from urllib.parse import urlparse #URL --> Domain
from time import sleep

dict_web_id  = {}
dict_url     = {} 
dict_topic   = {}
dict_suggest = {}
dict_sub     = {}
dict_bin     = {}
domains      =set()
urls         =set()

###################サブトピックリストの読み込み###################
a = open('sub_list.csv', 'r')
set_subtopic_keys = set()
for line in a:
	LINE = line.rstrip().split(',')
	web_id = LINE[0]
	url    = LINE[1]
	topic  = LINE[2]
	sub_id = LINE[3]
        
	Domain = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(url))
	domains.add(Domain)
	dict_web_id.setdefault(Domain, set()).add(web_id)
	dict_sub.setdefault(Domain, set()).add(sub_id)
	dict_topic.setdefault(Domain, set()).add(topic)
	set_topic=dict_topic[Domain]
	set_sub=dict_sub[Domain]
	set_subtopic_keys=dict_sub.keys() #dict_subのkeyの集合
a.close()



#################ビンリストの読み込み###########################
A = open('bin_list.csv','r')
set_bin_keys = set()
for line in A:
	LINE = line.rstrip().split(',')
	web_id = LINE[0]
	url    = LINE[1]
	topic  = LINE[2]
	bin_id = LINE[3]
	Domain = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(url))
	domains.add(Domain)
	dict_web_id.setdefault(Domain, set()).add(web_id)
	dict_topic.setdefault(Domain, set()).add(topic)
	dict_bin.setdefault(Domain, set()).add(bin_id)
	set_topic         = dict_topic[Domain]
	set_bin           = dict_bin[Domain]
	set_bin_keys = dict_bin.keys()
A.close()






###################ノウハウサイトの読み込み######################
b = open('know-how.csv','r')
count = 0
set_know_how = set()
dict_title = {}
dict_predict={}
dict_confidence={}
dict_truth={}
for line in b:
	count = count + 1
	print(line)
	LINE = line.rstrip().split(',')
	Domain = LINE[2]
	Domain = Domain + '/'
	Title  = LINE[3]
	predict= LINE[4]
	confidence=LINE[5]
	truth=LINE[1]
	set_know_how.add(Domain)
	dict_title[Domain] = Title
	dict_predict[Domain]=predict
	dict_confidence[Domain]=confidence
	dict_truth[Domain]=truth
b.close()







####################ドメインごとにHTMLを作成#####################
p = open('result.csv','w')
p.write('domain_id\ttitle\tpredict\tconfidence\tsum_page\tsum_topic\ttopics\ttruth\n')
def make_domain_dict():
	set_sugge = set()
	domain_dict ={}
	domain_id = 0
	for domain in domains:
		if domain in set_know_how:
			domain_id = domain_id + 1
			print (OKGREEN + 'domain_id=' + str(domain_id) + ENDC)
			set_topic     = dict_topic[domain]
			set_web_id    = dict_web_id[domain]
			if domain in set_subtopic_keys:
				set_subtopic  = dict_sub[domain] #domainにsubtopicがある場合
			else:
				set_subtopic  = 'N' #domainにsubtopicがない場合
			if domain in set_bin_keys:
				set_bin = dict_bin[domain]
			else:
				set_bin = 'N'

			count_topic   = len(set_topic)
			count_subtopic= len(set_subtopic)
			count_bin     = len(set_bin)
			count_page    = len(set_web_id)
			domain_dict["DOMAIN_ID"]   = domain_id
			domain_dict["DOMAIN"]      = domain
			domain_dict["WEB_ID"]      = set_web_id
			#domain_dict["URL"]         = set_url
			domain_dict["TOPIC"]       = set_topic
			domain_dict["SUBTOPIC"]    = set_subtopic
			domain_dict["BIN"]         = set_bin
			domain_dict["CT"]          = count_topic
			domain_dict["TITLE"]       = dict_title[domain]	
			print (          '[domain]--->'         + domain)
			print (OKGREEN + '[domain_id]--->'      + str(domain_id)     + ENDC)
			print (          '[web_id]-->'          + str(set_web_id))
			print (OKGREEN + '[count page]--->'     + str(count_page)    + ENDC)
			print ('[TOPIC]->'          + str(list(set_topic)))
			print (OKGREEN + '[count topic]--->'    + str(count_topic)   + ENDC)
			print ('[SUBTOPIC]->'       + str(list(set_subtopic)))
			print (OKGREEN + '[count subtopic]->'   + str(count_subtopic) + ENDC)
			print ('')
			print ('')
			strings = (str(domain_id)+'\t'\
				+str(dict_title[domain])+'\t'\
				+str(dict_predict[domain])+'\t'\
				+str(dict_confidence[domain])+'\t'\
				+str(count_page)+'\t'\
				+str(count_topic)+'\t'\
				+str(list(set_topic))+'\t'\
				+str(dict_truth[domain])+'\t'\
				+str(domain)+'\n')
			p.write(strings) 
			sleep(1)
			make_html(domain_dict, domain_id)
	




def make_html(domain_dict, domain_id):
	topic_ids   = domain_dict["TOPIC"]
	web_ids     = domain_dict["WEB_ID"]
	sub_ids     = domain_dict["SUBTOPIC"]
	bin_ids     = domain_dict["BIN"]
	title       = domain_dict["TITLE"]
	h = open('test1.html','r')
	i = open('domain_'+str(domain_id)+'.html','w')
	#exec("i=open('domain_%d.html','w')"%(domain_id))
	flag = 3
	for row in h:
		#sleep(0.05)
		# トピックに関する部分
		if 'class="suggest_list_small_class" value="'  in row:
			#value
			V1 = row.split('class="suggest_list_small_class" value="')
			V2 = V1[1]
			V2 = V2.split('"')
			value = V2[0]
			#TOPIC
			#L1 = row.split('(topic:')
			#L2 = L1[1]
			#L2 = L2.split(')')
			#TOPIC_NUM = L2[0]
			TOPIC_NUM  = value
			#TITLE
			R1 = row.split('">')
			R2 = R1[1]
			R2 = R2.split('<')
			title = R2[0]
			if TOPIC_NUM in topic_ids:
				string = '<div id="suggest_list_small_class_'+str(value)+'" class="suggest_list_small_class" value="'+str(value)+'" style="background-color: orange;"><font color="black">'+str(title)+'</font></div>\n'
				i.write(string)
			else:
				i.write(row)	



		# subtopicとbinのウェブページに関する部分
		elif '<!--web_id_sub:' in row:
			flag = 0
			#web_id_sub
			L1 = row.split('<!--web_id_sub:')
			L2 = L1[1]
			L2 = L2.split('-->')
			WEB_ID_SUB = L2[0]
			if WEB_ID_SUB in web_ids:
				i.write(row)
				flag = 1
		elif flag == 0 and '<!-- for search_result -->' in row:
			flag = 1
		#subtopicのタイトルの部分
		elif 'class="subtopic_list"' in row:
			L1 = row.split('subtopic_list_')
			L2 = L1[1]
			L2 = L2.split('"')
			sub_id = L2[0]
			if sub_id in sub_ids:
				flag = 4
			i.write(row)
		elif 'class ="expand_comma"' in row and flag == 4:
			L1 = row.split('class ="expand_comma"')
			front = L1[0]
			back  = L1[1]
			string = str(front) + ' class ="expand_comma" style="background-color: orange;"' + str(back)
			i.write(string)
			flag = 1
		elif 'class="summary_list"' in row:
			flag = 0
		elif flag == 0 and '<!-- for summary_list -->' in row:
			flag = 1

		#bin部分
		elif 'class="bin_list"' in row:
			L1 = row.split('bin_list_')
			L2 = L1[1]
			L2 = L2.split('"')
			bin_id = L2[0]
			if bin_id in bin_ids:
				flag = 4
			i.write(row)
			
		#サイト名
		elif 'id="suggest_list_title"' in row:
			string = '<div id="suggest_list_title"><font size="4">'+str(title)+'</font></div>'
			i.write(string)

		# 対象URLだけ出力
		elif flag == 1:
			i.write(row)
		# 対象URL以外は出力なし
		elif flag == 0:
			#print 'No sentence'
			command = 'Nothing'
		# それ以外の部分はそのまま出力
		else:
			i.write(row)



		


	h.close()
	i.close()	
	sleep(0.1)
make_domain_dict()
#suggest_id()
p.close()


print (len(set_know_how))
print (RED + 'Prgram ended' + ENDC)
