import gensim
from gensim import corpora, models, similarities


def make_corpus(dictionary,list3):
	print("コーパスの作成を開始します。")
	corpus = [dictionary.doc2bow(text) for text in list3]
	#corpora.MmCorpus.serialize('cop.mm', corpus)
	#corpus = gensim.corpora.TextCorpus('cop.mm')
	return corpus



dictionary = gensim.corpora.Dictionary.load_from_text('dict_ittan.txt')
a = open('dict_ittan.txt','r')
a = a[2:]
for i in a:
	LINE = i.rstrip().split('\t')
	ID   = LINE[0]
	word = LINE[1]
	frq  = LIEN[2]
	print (word)

#corpus = gensim.corpora.MmCorpus('cop.mm')
#model = gensim.models.ldamodel.LdaModel.load(model_dir_path.joinpath(file_name.replace('.txt', '_lda.pkl')).__str__()
new_text = [['就活','グループ'],['就活','手帳']]
corpus = make_corpus(dictionary,new_text)
lda = gensim.models.ldamodel.LdaModel.load("lda.model")
for topics_per_document in lda[corpus]:
	print(topics_per_document)
