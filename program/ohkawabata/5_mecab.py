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
            slice = pos.split(",")
            if len(word) > 1:
                if slice[0] == "名詞":
                    output_words.append(word)
                    output_text = output_text + ' ' + word
                elif slice[0] in [ "形容詞" , "動詞", "副詞"]:
                    if slice[5] == "基本形":
                        output_words.append(slice[-3])#活用していない原型を取得
                        output_text = output_text + ' ' + slice[-3]
    return output_words,output_text





# main_function
a = open('filtered.csv','r')
b = open('mecabed.csv','w')
b.write('page_id,url,suggest,mecabed_content\n')
cnt=0
for i in a:
    if cnt>=1:
        LINE = i.rstrip().split(',')
        page_id = LINE[0]
        url     = LINE[1]
        suggest = LINE[2]
        content = LINE[3]
        print ('[page_id]-->'+GREEN+page_id+ENDC)
        try:
            op_words,output_text = Mplg(content)
            #print(op_words)
            print(output_text[:50]+'....\n')
            b.write(page_id+','+url+','+suggest+','+output_text+'\n')
        except:
            print('The Content is None')
    cnt+=1
a.close()
b.close()
