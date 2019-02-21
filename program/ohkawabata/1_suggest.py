import argparse
from time import sleep
from string import ascii_lowercase
from string import digits
import requests
import urllib.parse


class GoogleAutoComplete:
    def __init__(self, test_mode=False, recurse_mode=False):
        self.base_url = 'https://www.google.co.jp/complete/search?'\
                        'hl=ja&output=toolbar&ie=utf-8&oe=utf-8&'\
                        'client=firefox&q='
        self.test_mode = test_mode
        self.recurse_mode = recurse_mode

        a = open('table_hiragana.dat','r')
        tango_list = []
        for tango in a:
            #sleep(1)
            tango = tango.rstrip()
            tango_list.append(tango)

        if test_mode:
            self.chrs = ['あ', 'g', '1']
            #self.chrs = ['あ']
        else:
            #self.chrs = [chr(i) for i in range(ord('あ'), ord('ん'))] # 大川くんのオリジナル．'gojuon.txt'と同じこと
            self.chrs  = [str(i) for i in tango_list] # Perlの五十音のファイルと全く同じ
            #self.chrs.extend(ascii_lowercase) #アルファベットとかもあえてとらない
            #self.chrs.extend(digits) # 数字はあまりいいサジェストとってこれないからあえてとらない

    def get_suggest(self, query):
        buf = requests.get(self.base_url +
                           urllib.parse.quote_plus(query)).json()
        suggests = [ph for ph in buf[1]]
        print("query: [{0}]({1})".format(query, len(suggests)))
        for ph in suggests:
            print(" ", ph)
        sleep(1)
        return suggests

    def get_suggest_with_one_char(self, query):
        # キーワードそのものの場合のサジェストワード
        ret = self.get_suggest(query)

        # キーワード＋空白の場合のサジェストワード
        ret.extend(self.get_suggest(query + ' '))

        # キーワード＋空白＋1文字の場合のサジェストワード
        for ch in self.chrs:
            ret.extend(self.get_suggest(query + ' ' + ch))

        """# -rオプションがあればもう1段階
        if self.recurse_mode:
            ret = self.get_uniq(ret)  # 事前に重複を除いておく
            addonelevel = []
            for ph in ret:
                addonelevel.extend(self.get_suggest(ph + ' '))
            ret.extend(addonelevel)"""

        return self.get_uniq(ret)

    # 重複を除く
    def get_uniq(self, arr):
        uniq_ret = []
        for x in arr:
            if x not in uniq_ret:
                uniq_ret.append(x)
        return uniq_ret

if __name__ == "__main__":
    phrase = input('please input query.')

    #a = open('gojuon.txt','r')
    #tango_list = []
    #for tango in a:
    #    tango = tango.rstrip()
    #    tango_list.append(tango)
    # Google Suggest キーワード取得
    gs = GoogleAutoComplete(recurse_mode = "--recure")
    ret = gs.get_suggest_with_one_char(phrase)

    #a = open('gojuon.txt','r')
    #tango_list = []
    #for tango in a:
    #   tango = tango.rstrip()
    #    tango_list.append(tango)
    # ファイルに保存する
    fname = "suggest.csv"
    with open(fname, 'w') as fs:
        for key in ret:
            fs.write(key + "\n")
