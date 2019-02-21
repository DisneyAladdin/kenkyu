#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
BOLD    = '\033[1m'
UNDERLINE = '\033[4m'
import MeCab
import gensim
from gensim import corpora, models, similarities 

def find_max(topics_per_document):
    list_A = []
    list_B = []
    for q in topics_per_document:
        list_A.append(q[0])
        list_B.append(q[1])
    max_prob  = max(list_B)
    max_index = list_B.index(max_prob)
    max_topic = list_A[max_index]
    print(str(max_topic)+','+str(max_prob))
    print('___________________________')
    return max_topic,max_prob






def make_corpus(dictionary,list3):
    print(GREEN+"コーパスの作成を開始します。"+ENDC)
    corpus = [dictionary.doc2bow(text) for text in list3]
    #corpora.MmCorpus.serialize('cop.mm', corpus)
    #corpus = gensim.corpora.TextCorpus('cop.mm')
    return corpus


#def Mplg(text):
#    output_words = []
#    #MECABで名詞を取り出す
#    m = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
#    soup = m.parse (text)
#    for row in soup.split("\n"):
#        word =row.split("\t")[0]
#        if word == "EOS":
 #           break
#        else:
#            pos = row.split("\t")[1]
#            slice = pos[0:2]
#            if slice == "名詞":
#                output_words.append(word)
#    return output_words





# main_function
#input_word = input(GREEN+'Please input some words\n--->'+ENDC)


a = open('mecabed.csv','r')
dictionary = gensim.corpora.Dictionary.load_from_text('dict_ittan.txt')
new_text = []
id_list = []
url_list = []
keywords_list=[]
cnt = 0
for i in a:
    if cnt  >= 1:
        LINE = i.rstrip().split(',')
        page_id = LINE[0]
        url     = LINE[1]
        keywords= LINE[2]
        content = LINE[3].split(' ')
        new_text.append(content)
        id_list.append(page_id)
        url_list.append(url)
        keywords_list.append(keywords)
    cnt += 1
a.close()

corpus = make_corpus(dictionary,new_text)
lda = gensim.models.ldamodel.LdaModel.load("lda.model")


b = open('adapted.csv','w')
b.write('page_id,url,keywords,topic,probability\n')
index = 0
for topics_per_document in lda[corpus]:
    print(topics_per_document)
    max_topic,max_prob = find_max(topics_per_document)
    page_id = id_list[index]
    url     = url_list[index]
    keywords= keywords_list[index]
    #print('page_id=',page_id)
    #print('url=',url)
    b.write(page_id+','+url+','+keywords+','+str(max_topic)+','+str(max_prob)+'\n')
    index += 1#ここでインデックス番号を右にずらす
b.close()
