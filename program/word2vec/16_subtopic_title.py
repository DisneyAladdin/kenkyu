#coding:utf-8
a = open('test.html','r')
b = open('test1.html','w')
c = open('subtopic3.csv','r')
d = open('id-suggest.csv','r')
#query = input('input query\n--->')

dict_id_suggest = {}
for i in d:
	LINE = i.rstrip().split(',',1)
	ID       = LINE[0]
	#suggests = LINE[1].split(',')
	#dict_id_suggest[ID] = suggests
	str_suggests = LINE[1]
	#for sg in suggests:
		#str_suggests = str_suggests+'\n'+sg
	dict_id_suggest[ID] = str_suggests
	#print (LINE[1])
#for i in dict_id_suggest:
#	print(i,dict_id_suggest[i])





#query = input('input query\n--->')
dict_subtopic_title = {}
for i in c:
	LINE = i.rstrip().split(',')
	ID   = LINE[0]
	URL  = LINE[1]
	suggest = LINE[2]
	topic   = LINE[3]
	prob    = LINE[4]
	sub     = LINE[5]
	if sub != '100':
		subtopic = topic+'_'+sub
		suggests = dict_id_suggest[ID]
		suggest  = suggest +','+ suggests
		dict_subtopic_title.setdefault(subtopic,set()).add(suggest)
		

#for i in dict_subtopic_title:
#	print(i,dict_subtopic_title[i])
dict_id_title = {}
for i in dict_subtopic_title:
	suggest = ''
	num=0
	for n in dict_subtopic_title[i]:
		if num==0:
			suggest = n
		else:
			suggest = suggest + ',' + n
		num+=1
	set_suggest = set(suggest.split(','))
	suggest_cmp = ''
	num2=0
	for p in set_suggest:
		if num2==0:
			suggest_cmp = p
		else:
			suggest_cmp = suggest_cmp + ',' + p
		num2+=1
	print(i, suggest_cmp)
	dict_id_title[i] = suggest_cmp
#for i in dict_subtopic_title:
#	print(i,dict_subtopic_title[i])




#<div class ="expand_comma" ><h2> 航空会社 座席 広さ</h2></div><!-- 2_3 -->
for i in a:
	if '<div class ="expand_comma" >' in i and '<!-- ' in i:
		print(i)
		sub = i.rstrip().split('</div><!--')[1].split('-->')[0].replace(' ','')
		title = dict_id_title[sub].replace(',','<br>')
		b.write('<div class ="expand_comma" ><h2>'+ title +'</h2></div>\n')
	else:
		b.write(i)
		



a.close()
b.close()
c.close()
d.close()
