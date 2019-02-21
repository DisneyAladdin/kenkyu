#coding:utf-8

a = open('webpage.csv','r')
b = open('webpage2.csv','w')
c = open('url-title-snippet0.csv','w')
d = open('id-suggest0.csv','w')


for i in a:
	LINE = i.rstrip().split(',')
	ID       = LINE[0]
	URL      = LINE[1]
	keywords = LINE[2]
	title    = LINE[3]
	snippet  = LINE[4]
	content  = LINE[5]
	
	b.write(ID+','+URL+','+keywords+','+content+'\n')
	c.write(ID+','+URL+','+title+','+snippet+'\n')
	d.write(ID+','+keywords+'\n')
a.close()
b.close()
c.close()
d.close() 
