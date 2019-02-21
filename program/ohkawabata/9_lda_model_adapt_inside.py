#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
BOLD    = '\033[1m'
UNDERLINE = '\033[4m'


import gensim
from gensim import corpora, models, similarities


def make_corpus(dictionary,list3):
	print("コーパスの作成を開始します。")
	corpus = [dictionary.doc2bow(text) for text in list3]
	#corpora.MmCorpus.serialize('cop.mm', corpus)
	#corpus = gensim.corpora.TextCorpus('cop.mm')
	return corpus


ID = input('Please input page_ID that you want to try\n--->')
dictionary = gensim.corpora.Dictionary.load_from_text('dict_ittan.txt')
a = open('dict_ittan.txt','r')
b = open('mecabed.csv','r')
new_text = []
for i in b:
	page_id = i.rstrip().split(',')[0]
	if page_id == ID:
		content = i.rstrip().split(',')[3].split(' ')
		new_text.append(content)
		print (content)
#corpus = gensim.corpora.MmCorpus('cop.mm')
#model = gensim.models.ldamodel.LdaModel.load(model_dir_path.joinpath(file_name.replace('.txt', '_lda.pkl')).__str__()
#new_text = [['就活','川畑修人',''],['ガンダム','GD']]
corpus = make_corpus(dictionary,new_text)
lda = gensim.models.ldamodel.LdaModel.load("lda.model")
for topics_per_document in lda[corpus]:
	print(topics_per_document)
a.close()
b.close()


c = open('result_of_lda.csv','r')
for i in c:
	page_id = i.rstrip().split(',')[0]
	if page_id == ID:
		topic = i.rstrip().split(',')[3]
		prob  = i.rstrip().split(',')[4]
		print ('Trueth-->'+GREEN+topic,prob+ENDC)
c.close()
