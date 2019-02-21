#coding:utf-8

tpc_sgs_frq_list = []
a = open('analyzed.csv','r')
c = open('analyzed_mdf.csv','w')
tpc = ''
sgs = ''
frq = 0
for i in a:
	LINE = i.rstrip().split(',')
	if LINE[0] != '':
		tpc = LINE[0]
		c.write(i)
	else:
		sgs  = LINE[2]	
		frq  = int(LINE[3])
	if frq >= 7:####### 頻度下限値 #################
		#print (tpc, sgs, frq)
		tpc_sgs_frq_list.append(tpc+','+sgs+','+str(frq))
		c.write(i)
a.close()
c.close()

#for i in tpc_sgs_frq_list:
#	print (i)


b = open('LDA_suggest_merged.csv','r')
d = open('LDA_suggest_merged_mdf.csv','w')
for i in b:
	LINE = i.rstrip().split(',')
	ID   = LINE[0]
	URL  = LINE[1]
	sgs  = LINE[2]
	tpc  = LINE[3]
	prb  = LINE[4]
	
	for n in tpc_sgs_frq_list:
		line = n.rstrip().split(',')
		TPC  = line[0]
		SGS  = line[1]
		FRQ  = line[2]
	
		#print (tpc,TPC)
		#print (sgs,SGS)	
		if tpc == TPC and sgs == SGS:
			print(i.rstrip())
			d.write(i)
b.close()
d.close()
