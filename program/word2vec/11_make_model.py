#coding:utf-8
from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus('./wiki_and_webpage_appended.txt')

model = word2vec.Word2Vec(sentences, size=20, min_count=2, window=20)
#model = word2vec.Word2Vec(sentences, size=200, min_count=20, window=15)
model.save("./text.model")
