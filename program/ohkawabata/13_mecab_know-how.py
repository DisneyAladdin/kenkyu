#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'

import MeCab

def Mplg(text):
    output_words = []
    output_text  = ''
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
                output_text = output_text + ' ' + word
    return output_words,output_text





# main_function
a = open('filtered_know-how.csv','r')
b = open('mecabed_know-how.csv','w')
b.write('page_id,url,mecabed_content\n')
for i in a:
    LINE = i.rstrip().split(',')
    page_id = LINE[0]
    url     = LINE[1]
    #suggest = LINE[2]
    content = LINE[2]
    print ('[page_id]-->'+GREEN+page_id+ENDC)
    op_words,output_text = Mplg(content)
    #print(op_words)
    print(output_text[:50]+'....\n')
    b.write(page_id+','+url+','+output_text+'\n')
a.close()
b.close()
