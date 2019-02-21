a = open('adapted.csv','r')
b = open('filtered.csv','w')
c = open('eliminated.csv','w')

border = float(input('please enter the border\n--->'))

cnt=0
cnt_f=0
cnt_e=0
for i in a:
	if cnt >= 1:	
		LINE = i.rstrip().split(',')
		topic= LINE[3]
		prob = float(LINE[4])
		if prob < border:
			#print ('the Webpage is lower than border!!')
			c.write(i)
			cnt_e += 1
		else:
			b.write(i)
			cnt_f += 1
	cnt+=1


print('filtered-->',cnt_f)
print('eliminated-->',cnt_e)
