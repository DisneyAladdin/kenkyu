#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
from time import sleep
import chardet




def guess_charset(data):  
	f = lambda d, enc: d.decode(enc) and enc  
	try: return f(data, 'utf-8')  
	except: pass  
	try: return f(data, 'shift-jis')  
	except: pass  
	try: return f(data, 'euc-jp')  
	except: pass  
	try: return f(data, 'iso2022-jp')  
	except: pass  
	return None  
  
def conv(data):  
	charset = guess_charset(data)  
	u = data.decode(charset)  
	return u.encode('utf-8')  








query=input('please input query\n---->')
a = open('webpage.csv','r',encoding = 'utf_8')
b = open('filtered.csv','w')
b.write('page_id,url,suggest,content\n')
c = open('eliminated.csv','w')
c.write('page_id,url,suggest,content\n')
#d = open('noisy_url.csv','r')
jogai_list=[]
#for i in d:
#	URL=i.rstrip().split(',')[1]
#	jogai_list.append(URL)
#d.close()
	




cnt = 0
good_cnt = 0
bad_cnt  = 0
for i in a:
	if cnt >= 1:
		LINE = i.rstrip().split(',')
		web_id = LINE[0]
		url    = LINE[1]
		suggest= LINE[2]
		content= LINE[3]
		print (GREEN+web_id+ENDC)
		print (BLUE+url+ENDC)
		#print(chardet.detect(str(content.read())))
		if '.pdf' in url or content == 'None' or url in jogai_list or (query+' ' not in suggest and ' '+query not in suggest) or len(content) < 10:
			print (RED+'Eliminate this page'+ENDC)
			c.write(web_id+','+url+','+suggest+','+content+'\n')
			bad_cnt += 1
			#sleep(1)
		else:
			b.write(web_id+','+url+','+suggest+','+content+'\n')
			good_cnt += 1
	cnt += 1
	#sleep(0.02)
print ('[cnt]-->'+str(cnt-1))
print ('[good_cnt]-->'+str(good_cnt))
print ('[bad_cnt]-->'+str(bad_cnt))
a.close()
b.close()
c.close()
