# coding: utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'
import gensim
from gensim import corpora, models, similarities
from time import sleep

def find_max(topics_per_document):
    list_A = []
    list_B = []
    for q in topics_per_document:
        #topic = q[1]
        #probability = q[2]
        list_A.append(q[0])
        list_B.append(q[1])
    max_prob  = max(list_B)
    max_index = list_B.index(max_prob)
    max_topic = list_A[max_index]
    print(GREEN+str(max_topic)+','+str(max_prob)+ENDC)
    print('___________________________')
    return max_topic,max_prob


def make_dictionary(list3):
    print(GREEN+"辞書の作成を開始します。"+ENDC)
    dictionary = corpora.Dictionary(list3)
    #dictionary.filter_extremes(no_below=1, no_above=1) # 「頻度が１回のものは無視」というのを解除
    dictionary.save_as_text('dict_ittan.txt')
    dictionary = gensim.corpora.Dictionary.load_from_text('dict_ittan.txt')
    return dictionary

def make_corpus(dictionary,list3):
    print(GREEN+"コーパスの作成を開始します。"+ENDC)
    corpus = [dictionary.doc2bow(text) for text in list3]
    corpora.MmCorpus.serialize('cop.mm', corpus)
    corpus = gensim.corpora.TextCorpus('cop.mm')
    return corpus

def maketopic_lda(dictionary,topic_N,id_list,url_list,suggest_list):
    corpus2 = corpora.MmCorpus('cop.mm')
    # num of topic
    #topic_N = 2
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus2, num_topics=topic_N, id2word=dictionary)
    lda.save("lda.model")
    for i in range(topic_N):
        print('TOPIC:', i, '__', lda.print_topic(i))
    index = 0
    for topics_per_document in lda[corpus2]:
        print(topics_per_document)
        page_id = id_list[index]
        url     = url_list[index]
        suggest = suggest_list[index]
        #print (GREEN+str(page_id)+ENDC)
        #print (url)
        #print (CYAN+str(suggest)+ENDC)
        #print(topics_per_document)
        #print (GREEN+str(page_id)+ENDC)
        max_topic,max_prob = find_max(topics_per_document)
        b.write(page_id+','+url+','+suggest+','+str(max_topic)+','+str(max_prob)+'\n')
        index += 1
        #for q in topics_per_document:
            #for p in q:
                #print (GREEN+str(p)+ENDC)
            #q = q.replace('(','').replace(')','')
            #print(GREEN+str(q)+ENDC)



#listA = [["就活","メール","お礼"],["メール","ありがとう","ノック"]]
#dictionary = make_dictionary(listA)
#make_corpus(dictionary,listA)
#maketopic_lda(dictionary)


N = int(input(GREEN+'How many topics do you want?\n-->'+ENDC))
a = open('mecabed.csv','r')
b = open('result_of_lda.csv','w')
b.write('page_id,url,suggest,topic,probability\n')
id_list = []
url_list = []
suggest_list = []
listB = []
cnt = 0
for i in a:
    if cnt >=1:
        LINE = i.rstrip().split(',')
        page_id = LINE[0]
        url     = LINE[1]
        suggest = LINE[2]
        content = LINE[3]
        CNT     = content.split(' ')
        listB.append(CNT)
        id_list.append(page_id)
        url_list.append(url)
        suggest_list.append(suggest)
    cnt += 1
#print (listB)
dictionary = make_dictionary(listB)
make_corpus(dictionary,listB)
maketopic_lda(dictionary,N,id_list,url_list,suggest_list)
#sleep(0.02)
a.close()
b.close()    
