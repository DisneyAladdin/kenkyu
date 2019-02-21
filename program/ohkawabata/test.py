import chardet
from urllib.request import urlopen
 
r = urlopen('http://yahoo.co.jp/')
rawdata = r.read()
print(chardet.detect(rawdata)) 
