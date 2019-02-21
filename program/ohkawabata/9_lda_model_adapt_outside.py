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

def make_corpus(dictionary,list3):
    print(GREEN+"コーパスの作成を開始します。"+ENDC)
    corpus = [dictionary.doc2bow(text) for text in list3]
    #corpora.MmCorpus.serialize('cop.mm', corpus)
    #corpus = gensim.corpora.TextCorpus('cop.mm')
    return corpus


def Mplg(text):
    output_words = []
    #MECABで名詞を取り出す
    m = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    soup = m.parse (text)
    for row in soup.split("\n"):
        word =row.split("\t")[0]
        if word == "EOS":
            break
        else:
            pos = row.split("\t")[1]
            slice = pos[0:2]
            if slice == "名詞":
                output_words.append(word)
    return output_words





# main_function
input_word = input(GREEN+'Please input some words\n--->'+ENDC)
dictionary = gensim.corpora.Dictionary.load_from_text('dict_ittan.txt')
op_words = Mplg(input_word)
new_text = []
new_text.append(op_words)
corpus = make_corpus(dictionary,new_text)
lda = gensim.models.ldamodel.LdaModel.load("lda.model")
for topics_per_document in lda[corpus]:
    print(topics_per_document)
