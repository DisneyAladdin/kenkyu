#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
BOLD    = '\033[1m'
UNDERLINE = '\033[4m'

query = input(GREEN+'Please input the query\n-->'+ENDC)

a = open('analyzed.csv','r') #for topic title
b = open('subtopic4.csv','r')
c = open('test.html','w')
#d = open('webpage.csv','r')
e = open('id-suggest2.csv','r')#for showing the suggests
f = open('sub_list.csv','w')
g = open('bin_list.csv','w')
h = open('url-title-snippet2.csv','r')




c.write(
'<!DOCTYPE html>\n\
<head>\n\
    <meta charset="utf-8">\n\
    <title>ノウハウちゃんねる</title>\n\
    <script type="text/javascript" src="../../src/jquery-1.7.1.min.js"></script>\n\
    <link rel="stylesheet" type="text/css" href="myDefaultSearch_tei_0903.css">\n\
    <script src="main_search_tei.js"></script>\n\
</head>\n\
<body bgcolor="cadetblue">\n\
    <div id="title">\n\
      <div id="title_contents">\n\
        <div id="contents_suggest"></div>\n\
        <div id="contents_add">に関する話題</div>\n\
    </div>\n\
</div>\n'
)
c.write(
'<div id="main">\n\
   <div id="suggest_list">\n\
     <div id="suggest_list_title">トピックに分類された<br>サジェスト<br></div>\n\
     <div id="suggest_list_large_class_0" class="suggest_list_large_class" value="0">・'+query+'</div>\n\
     <div style="height:378px; width:250px; overflow-y:scroll;">\n\
     <div id="suggest_list_large_class_area_0" class="suggest_list_large_class_area">\n'
)

########## Topic and Suggest ########
for i in a:
	LINE = i.rstrip().split(',')
	topic   = LINE[0]
	title   = LINE[1]+'(topic:'+topic+')'
	suggest = LINE[2].replace(query+' ','').replace(' '+query,'')
	freq    = LINE[3]	
	if len(topic) != 0:
		if topic != '0':
			c.write('      </div>\n')
		c.write('        <div id="suggest_list_small_class_'+topic+'" class="suggest_list_small_class" value="'+topic+'">'+title+'</div>\n')
		c.write('        <div id="suggest_list_small_class_area_'+topic+'" class="suggest_list_small_class_area">\n')
	else:
		c.write('        <div class="suggest_list_words" value="'+suggest+'" suggest_id="0"><span><font size="3">'+suggest+'(頻度:'+str(freq)+')'+'</font></span></div>\n')
c.write(
'      </div>\n\
    </div>\n\
    </div>\n\
</div>\n'
)
a.close()


######### ID and Content ##########
dict_content = {}
#num = 0
#for i in d:
#	LINE             = i.rstrip().split(',',4)
#	ID               = LINE[0]
#	URL              = LINE[1]
#	content          = LINE[3]
#	dict_content[ID]= content
######## ID and title, ID and snippet ##########
dict_title = {}
dict_snippet = {}
for i in h:
	LINE = i.rstrip().split(',',4)
	ID   = LINE[0]
	URL  = LINE[1]
	title = LINE[2]
	snippet = LINE[3]
	dict_title[ID] = title
	dict_snippet[ID] = snippet

######### ID and Suggests ########
dict_suggests = {}
for i in e:
	LINE     = i.rstrip().split(',',1)
	ID       = LINE[0]
	Suggests = LINE[1].split(',')
	dict_suggests[ID] = Suggests
	print(Suggests)
#d.close()
e.close()










############# Subtopic and Bin #############


change_topic = 1
change_sub   = 0
change_bin   = 0
change_sub_to_bin = 0

subtopic_list = 'off'
bin_list      = 'off'

bin_id = 0


#subtopic_counter = 0
permition_to_close_subtopic_list = 0
bef_topic = '0'
bef_sub   = '0'

tmp_snippet = 'MSN-06S SINANJU is developed for Full Frontal based on prototype mobile suits robbed from ANAHEIM ELECTRONICS, AE. Height:22.6m, Weight:25.2t. The overwhelming fighting power and the appearance of crimson reminds the viewer of the former "red comet".'

for i in b:
	LINE = i.rstrip().split(',')
	ID      = LINE[0]
	URL     = LINE[1]
	suggest = LINE[2]
	suggests = dict_suggests[ID]
	topic   = int(LINE[3])
	prob    = LINE[4]
	sub     = int(LINE[5])
	title   = dict_title[ID]
	snippet = dict_snippet[ID]
	#URL_text = dict_content[ID][:20]
	#content  = dict_content[ID][:60]
	# トピックが変わったかどうか（変化あれば１，なければ０）
	if topic != bef_topic:
		change_topic = 1
	else:
		change_topic = 0

	# subが変わったかどうか（変化があれば１，なければ０）
	if sub != bef_sub:
		change_sub = 1
	else:
		change_sub = 0
	
	# トピックが変わったら bin_id を初期化
	if change_topic == 1:
		bin_id = 0

	# subtopicからbinに切り替わる時
	if sub != bef_sub and sub == 100:
		change_sub_to_bin = 1


	# subtopic_list を閉じる
	if change_sub == 1 and subtopic_list == 'on':
		c.write('</div><!-- for subtopic_list -->\n')
		subtopic_list = 'off'
		#subtopic_counter = 0



	# subtopic の中身
	if subtopic_list == 'on' and sub==bef_sub:
		#c.write('<div class ="expand_comma" ><h2> '+suggest+'</h2></div>\n')
		c.write('<div class="search_result" style= "display:none;"><!--web_id_sub:'+ID+'-->\n')
		c.write('<div class="contents_link"><a href='+URL+' target="_blank"><b>'+title+'</b></a></div>\n')
		c.write('<div class="contents_abst">'+snippet+'</div>\n')
		c.write('<div class="contents_suggest">\n')
		for sg in suggests:
			c.write('<div class="contents_suggest_tag">'+sg+'</div>\n')
		c.write('</div> <!-- for contents_suggest -->\n')
		c.write('</div> <!-- for search_result -->\n')
		f.write(ID+','+URL+','+str(topic)+','+str(topic)+'_'+str(sub)+'\n')
		#subtopic_counter += 1



	# bin の中身
	#if bin_list == 'on' and sub==100:
	#	c.write('<div class="search_result" style= "display:none;">\n')
	#	c.write('<div class="contents_link"><a href='+URL+' target="_blank"><b>'+URL_text+'</b></a></div>\n')
	#	c.write('<div class="contents_abst">'+tmp_snippet+'</div>\n')
	#	c.write('<div class="contents_suggest">\n')
	#	for sg in suggests:
	#		c.write('<div class="contents_suggest_tag">'+sg+'</div>\n')
	#	c.write('</div> <!-- for contents_suggest -->\n')
	#	c.write('</div> <!-- for search_result -->\n')



	# subtopic_area を閉める
	if change_sub_to_bin == 1:
		c.write('</div> <!-- for subtopic_area -->\n')
		#c.write('</div>\n')

	# bin_list を閉める
	if bin_list == 'on':
		c.write('</div><!-- for bin_list -->\n')
		bin_list = 'off'

	# bin_area を閉める
	if change_topic == 1 and topic != 0:
		c.write('</div><!-- for bin_area -->\n')
		#c.write('</div>\n')


	# トピックが変わったとき
	if change_topic == 1:
		if topic != 0:
			c.write('</div><!-- for classify_area -->\n<!------------------------------------------>\n')
		c.write(
'<div id ="classify_area_'+str(topic)+'" class="classify_area"  style="display:none;">\n\
<div class ="button_frame">\n\
<div id = "button_subtopic_'+str(topic)+'" class = "button_subtopic" style = "display:none;">\n\
<span style="font-weight:bold">Subtopics</span></div>\n\
<div id = "button_bin_'+str(topic)+'" class = "button_bin" style = "display:none;">\n\
<span style="font-weight:bold">Others</span></div>\n\
</div>  <!-- for button_frame -->\n\n'
)


	# subtopic_area の定義
	if sub!=100 and change_topic==1:
		#c.write('<div style="height:400px; width:700px; overflow-x:scroll;">\n')
		c.write('<div id ="subtopic_area_'+str(topic)+'" class="subtopic_area" style="display:none;">\n')

	
	# bin_area の定義
	if sub==100 and change_sub_to_bin ==1:
		#c.write('<div style="height:400px; width:700px; overflow-x:scroll;">\n')
		c.write('<div id ="bin_area_'+str(topic)+'" class="bin_area"  style="display:none;">\n')
	############# subtopic のないトピックの bin_areaの定義 ###############
	if sub == 100 and change_sub_to_bin ==0 and change_topic == 1:
		#c.write('<div style="height:400px; width:700px; overflow-x:scroll;">\n')
		c.write('<div id ="bin_area_'+str(topic)+'" class="bin_area"  style="display:none;">\n')


	# subtopic_list の定義
	if sub != 100 and change_sub == 1:
		c.write('<div id="subtopic_list_'+str(topic)+'_'+str(sub)+'" class="subtopic_list" >\n')
		c.write('<div class ="expand_comma" ><h2> '+suggest+'</h2></div>\n')
		c.write('<div class="search_result" style= "display:none;"><!--web_id_sub:'+ID+'-->\n')
		c.write('<div class="contents_link"><a href='+URL+' target="_blank"><b>'+title+'</b></a></div>\n')
		c.write('<div class="contents_abst">'+snippet+'</div>\n')
		c.write('<div class="contents_suggest">\n')
		for sg in suggests:
			c.write('<div class="contents_suggest_tag">'+sg+'</div>\n')
		c.write('</div> <!-- for contents_suggest -->\n')
		c.write('</div> <!-- for search_result -->\n')
		f.write(ID+','+URL+','+str(topic)+','+str(topic)+'_'+str(sub)+'\n')
		#subtopic_counter += 1
		subtopic_list = 'on'



	# bin_list の定義
	if sub == 100:
		bin_id += 1
		c.write('<div id="bin_list_'+str(topic)+'_'+str(bin_id)+'" class="bin_list" >\n')
		c.write('<div class ="expand_comma" ><h2> '+suggest+'</h2></div>\n')
		c.write('<div class="search_result" style= "display:none;"><!--web_id_sub:'+ID+'-->\n')
		c.write('<div class="contents_link"><a href='+URL+' target="_blank"><b>'+title+'</b></a></div>\n')
		c.write('<div class="contents_abst">'+snippet+'</div>\n')
		c.write('<div class="contents_suggest">\n')
		for sg in suggests:
			c.write('<div class="contents_suggest_tag">'+sg+'</div>\n')
		c.write('</div> <!-- for contents_suggest -->\n')
		c.write('</div> <!-- for search_result -->\n')
		g.write(ID+','+URL+','+str(topic)+','+str(topic)+'_'+str(bin_id)+'\n')
		bin_list = 'on'
	############# subtopic のないトピックの bin_list の定義 ###############
	#if sub == 100 and change_sub == 0 and change_topic == 1:
	#	c.write('<div id="bin_list_'+str(topic)+'_'+str(sub)+'" class="bin_list" >\n')
	#	c.write('<div class ="expand_comma" ><h2> '+suggest+'</h2></div>\n')
	#	c.write('<div class="search_result" style= "display:none;">\n')
	#	c.write('<div class="contents_link"><a href='+URL+' target="_blank"><b>'+URL_text+'</b></a></div>\n')
		
	#	c.write('</div> <!-- for search_result -->\n')
	#	bin_list = 'on'

	# 初期化
	if change_topic == 1:
		change_topic = 0
	if change_sub_to_bin == 1:
		change_sub_to_bin = 0
	change_sub = 0


	# 一つ前の値として保存
	bef_topic = topic
	bef_sub   = sub


	#print (suggests)
# 一番最後のトピックの<bin_area>, <classify_area>, <body>, <html>を閉める
c.write('</div><!-- for bin_area -->\n</div><!-- for classify_area -->\n</body>\n</html>')
b.close()
c.close()
f.close()
g.close()
h.close()
