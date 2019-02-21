#coding:utf-8
a = open('filtered.csv','r')
b = open('subtopic0.csv','w')
for i in a:
	LINE = i.rstrip().split(',')
	ID   = LINE[0]
	URL  = LINE[1]
	keywords=LINE[2]
	topic= LINE[3]
	prob = LINE[4]
	sub  = '100'  #サブトピックなしで設定
	
	b.write(ID+','+URL+','+keywords+','+topic+','+prob+','+sub+'\n')
a.close()
b.close()

