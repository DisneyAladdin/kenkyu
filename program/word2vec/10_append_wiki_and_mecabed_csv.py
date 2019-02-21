#coding:utf-8

a = open('jawiki_token.txt','r')
b = open('mecabed.csv','r')
c = open('wiki_and_webpage_appended.txt','w')

for i in a:
	c.write(i)
for i in b:
	mecabed_text = i.split(',',4)[3]
	c.write(mecabed_text)
a.close()
b.close()
c.close()

