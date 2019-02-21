# coding:utf-8
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



def main(u,query,num_topics):
	id_list     = []
	topics_list = []
	CF_list     = []
	CP_list     = []
	CT_list     = []
	TR_list     = []
	DM_list     = []
	ID_list     = []
	#jogai_list  = [11,34]
	jogai_list  = []
#exec("i = open('domain_%d.html','w')" %(domain_id))
	#exec("a = open('data/mainpage_%d.html','w')" %(u))
	a = open('data/mainpage_'+str(u)+'.html','w')
	#exec("c = open('data/%d.csv','r')" %(u))
	c = open('data/'+str(u)+'.csv','r')
	num=0
	for k in c:
		num+=1
		print (num)
	c.close()

	#exec("b = open('data/%d.csv','r')" %(u))
	b = open('data/'+str(u)+'.csv','r')

# <style>td{width: 80px !important;}</style>\n\

	strings = '<head>\n\
	<meta charset="utf-8">\n\
	<link rel="shortcut icon" href="fig/light.png" type="image/png" sizes="96x96">\n\
	<TITLE>ノウハウちゃんねる</TITLE>\n\
	<link rel="stylesheet" type="text/css" href="css.css">\n\
	</head>\n\
	<font face="Comic Sans MS">\n\
	<p><body align="center" bgcolor="darkcyan">\n\
	<img src="know-how.png" width="450">\n\
	<div class="tsukuba">\n\
	<img src="tsukuba.png" width="250">\n\
	</div>\n\
	<div style="height:700px; width:1300px; border: 5px solid dimgray; overflow-y:scroll; position: center; margin: 0 auto;">\n\
	<table class="sampleTable" width="'+str(400+num*100)+'" align="center" cellspacing="0" border=2>\n\
	<tr>\n\
	<th width="30" bgcolor="lightgrey" rowspan=3><font face="Comic Sans MS">ID</font></th>\n\
	<th width="400" bgcolor="lightgrey" rowspan=3><font face="Comic Sans MS" color="blue" size="6">'+query+'</font>\n\
	<p><body align="left" bgcolor="darkslategray"><table align="center" cellspacing="1" border=2 bgcolor="white">\n\
	<tr>\n\
	<td align="center" bgcolor="lightgray"><font color="black" style="font-weight:bold">confidence</font></td>\n\
	<td width="50" align="center"><a href="mainpage_rev_1.html">★★★★</a></td>\n\
	<td width="50" align="center"><a href="mainpage_rev_2.html">★★★</a></td>\n\
	<td width="50" align="center"><a href="mainpage_rev_3.html">★★</a></td>\n\
	<td width="50" align="center"><a href="mainpage_rev_4.html">★</a></td>\n\
	</tr>\n\
	<!--<tr>\n\
	<td bgcolor="lightgray" align="center"><font color="black" style="font-weight:bold">サイト数</font></td>\n\
	<td align="center"><font style="font-weight:bold">10</font></td>\n\
	<td align="center"><font style="font-weight:bold">21</font></td>\n\
	<td align="center"><font style="font-weight:bold">40</font></td>\n\
	<td align="center"><font style="font-weight:bold">47</font></td>-->\n\
	</table>\n\
	</th>\n\
	<th bgcolor="lightgrey"colspan="'+str(num)+'" align="left">Domain</th>\n</tr>\n'
	a.write(strings)
	a.write('<tr>\n')

	for i in range(1,num+1):
    		strings = '<td bgcolor="white">'+str(i)+'位</td>\n'
    		a.write(strings)
	a.write('</tr>\n')
	a.write('<tr>\n')
#num=0
	for line in b:
	#num+=1
		LINE = line.rstrip().split(',',7)
		domain_id = LINE[0]
		title     = LINE[1]
		domain    = LINE[2]
		truth     = LINE[3]
		conf      = LINE[4]
		CP        = LINE[5]
		CT        = LINE[6]
		topics    = LINE[7].replace('"','').replace(']','').replace('[','').replace('\'','').replace(' ', '')
		topic     = topics.split(',')
	#topic.sort()
	#print num
	#print topics
		count     = len(topic)
	#print OKGREEN + str(topics) + ENDC
	#print count
	#print PURPLE + str(topic) + ENDC
		set_topic = set()
		for t in topic:
			set_topic.add(int(t))
	#print set_topic
		id_list.append(domain_id)
		topics_list.append(set_topic)
		CF_list.append(conf)
		CP_list.append(CP)
		CT_list.append(CT)
		TR_list.append(truth)
		DM_list.append(domain)
		ID_list.append(domain_id)
		strings = '<td class="domain" bgcolor="white"><a href="domain_'+str(domain_id)+'.html" target="_blank">'+str(title)+'</a></td>\n'
		a.write(strings)
	#make_html(id_list, topics_list)
	a.write('</tr>\n')


	#a.write('<tr>\n<th bgcolor="lightgrey" colspan=2>信頼度</th>\n')
	#for conf in CF_list:
	#	strings = '<td bgcolor="white" style="font-weight:bold" align="center">'+str(conf)+'</td>\n'
	#	a.write(strings)
	#a.write('</tr>\n')

	#a.write('<tr>\n<th bgcolor="lightgrey" colspan=2>ページ数</th>\n')
	#for CP in CP_list:
	#	strings = '<td bgcolor="white" style="font-weight:bold" align="center">'+str(CP)+'</td>\n'
	#	a.write(strings)
	#a.write('</tr>\n') 




	a.write('<tr>\n<th bgcolor="lightgrey" colspan=2>Topics</th>\n')
	for CT in CT_list:
		strings = '<td bgcolor="white" style="font-weight:bold" align="center">'+str(CT)+'</td>\n'
		a.write(strings)
	a.write('</tr>\n')
	#a.write('</tr>\n</table>\n</html>\n')


	a.write('<tr>\n<th bgcolor="lightgrey" colspan=2>Pages</th>\n')
	for CP in CP_list:
		strings = '<td bgcolor="white" style="font-weight:bold" align="center">'+str(CP)+'</td>\n'
		a.write(strings)
	a.write('</tr>\n')




	a.write('<tr>\n<th bgcolor="lightgrey" colspan=2>Judge by SVM</th>\n')
	for conf in CF_list:
		conf = round(float(conf),3)
		strings = '<td bgcolor="white" style="font-weight:bold" align="center">'+str(conf)+'</td>\n'
		a.write(strings)
	a.write('</tr>\n')



	a.write('<tr>\n<th bgcolor="lightgrey" colspan=2>Judge by hand</th>\n')
	for truth in TR_list:
		strings = '<td bgcolor="white" style="font-weight:bold" align="center">'+truth+'</td>\n'
		a.write(strings)
	a.write('</tr>\n')


	a.write('<tr>\n<th bgcolor="lightgrey" colspan=2>To the site</th>\n')
	for domain in DM_list:
		strings = '<td bgcolor="white" style="font-weight:bold" align="center"><input type="button" onclick="window.open(\''+str(domain)+'\',\'_blank\')"value="check" target="_blank" style="background-color:darkturquoise; font:11pt Comic Sans MS; width:60px; height:30px" onmouseover="this.style.background=\'gray\'"onmouseout="this.style.background=\'darkturquoise\'"></td>\n'
		#strings = '<td bgcolor="white" style="font-weight:bold" align="center"><a href="'+str(domain)+'" target="_blank">link</a></td>\n'
		a.write(strings)
	a.write('</tr>\n')

	
	a.write('<tr>\n<th bgcolor="lightgrey" colspan=2>Domain ID</th>\n')
	for domain_id in ID_list:
		strings = '<td bgcolor="white" style="font-weight:bold" align="center">'+str(domain_id)+'</td>\n'
		a.write(strings)
	a.write('</tr>\n')


	#a.write('<tr>\n<th bgcolor="lightgrey" colspan=2>ページ数</th>\n')
	#for CP in CP_list:
	#	strings = '<td bgcolor="white" style="font-weight:bold" align="center">'+str(CP)+'</td>\n'
	#	a.write(strings)
	#a.write('</tr>\n')

	#int num_of_topic = int(topics)
	####トピック数になっているので動的に変える必要がある
	for i in range(0,num_topics):
		if i not in jogai_list:
			if i % 2 == 0:
				a.write('<tr bgcolor="whitesmoke" align="center">\n<td >'+str(i)+'</td>\n<td width="300" style="font-weight:bold">Topic'+str(i)+'</td><!--topic:'+str(i)+'-->\n')
			else:
				a.write('<tr bgcolor="white" align="center">\n<td>'+str(i)+'</td>\n<td width="300" style="font-weight:bold">Topic'+str(i)+'</td><!--topic:'+str(i)+'-->\n')
			for topics in topics_list:
				if i in topics:
					strings = '<td bgcolor="orange"></td>\n'
				else:
					strings = '<td></td>\n'
		
				a.write(strings) 
			a.write('</tr>\n\n')


#a.write('<tr>\n<th bgcolor="gray" colspan=2><font color="white">ページ数</font></th>\n')
#for CP in CP_list:
#	strings = '<td>'+str(CP)+'</td>\n'
#	a.write(strings)	
#a.write('</tr>\n')

#a.write('<tr>\n<th bgcolor="gray" colspan=2><font color="white">トピック数</font></th>\n')
#for CT in CT_list:
#	strings = '<td>'+str(CT)+'</td>\n'
#	a.write(strings)
#a.write('</tr>\n</table>\n</html>\n')
	a.write('</table>\n</div><!--scroll-->\n<marquee><font color="white" face="Comic Sans MS" size="4">Presented by Shuto Kawabata in 2018.</marquee>\n</font>\n</body>\n</html>\n')





#print id_list
	a.close()
	b.close()

# 4つのHTMLを作りたいので４回回す！
query = input('please enter the query\n-->')
num_topics= int(input('How many topics do you have?\n--->'))
#int(num_topics)
for u in range(1,5):        
	main(u,query,num_topics)
