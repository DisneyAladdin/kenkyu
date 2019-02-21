#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
from time import sleep

a = open('webpage_know-how.csv','r')
b = open('filtered_know-how.csv','w')
b.write('page_id,url,content\n')
c = open('eliminated.csv','w')
c.write('page_id,url,content\n')
cnt = 0
good_cnt = 0
bad_cnt  = 0
for i in a:
	if cnt >= 1:
		LINE = i.rstrip().split(',')
		web_id = LINE[0]
		url    = LINE[1]
		#suggest= LINE[2]
		content= LINE[2]
		print (GREEN+web_id+ENDC)
		print (BLUE+url+ENDC)
		if '.pdf' in url or content == 'None':
			print (RED+'Eliminate this page'+ENDC)
			c.write(web_id+','+url+','+content+'\n')
			bad_cnt += 1
			#sleep(1)
		else:
			b.write(web_id+','+url+','+content+'\n')
			good_cnt += 1
	cnt += 1
	sleep(0.02)
print ('[cnt]-->'+str(cnt-1))
print ('[good_cnt]-->'+str(good_cnt))
print ('[bad_cnt]-->'+str(bad_cnt))
a.close()
b.close()
c.close()
