#encoding:utf-8
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
ENDC    = '\033[0m'
import urllib
import urllib.request
import json
import sys
import pandas as pd
from time import sleep
import csv

def scrape_serps(key,maxrank,df_api,api_counter,j,try_cnt):
    phrase = urllib.parse.quote(key)
    try:
        #api_counter
        url_list = []
        title_list = []
        snippet_list = []
        a = list(df_api["log"])
        cnt=1# 1位から１０位を意味する
        while(cnt<maxrank*10):
            if api_counter < 99:
                print("[page_num]-->"+str(cnt))
                API_KEY = df_api["API_KEY"][j]
                ENGINE_ID = df_api["API_ID"][j]
                print (CYAN+"[api_cnt]-->"+GREEN+str(api_counter)+ENDC)
                print ("[API_KEY]-->"+str(API_KEY))
                print ("[API_NUM]-->"+str(j))
                print ("[SUGGEST]-->"+key)
                #print ("------------")
                req_url = "https://www.googleapis.com/customsearch/v1?hl=ja&key="+API_KEY+"&cx="+ENGINE_ID+"&alt=json&q="+ phrase +"&start="+ str(cnt)
                print("[req_url]-->"+str(req_url))
                headers = {"User-Agent": 'Mozilla /5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B5110e Safari/601.1'}
                # 以下５行をコメントアウトすればリクセストなし
                req = urllib.request.Request(req_url)
                res = urllib.request.urlopen(req)
                dump = json.loads(res.read())
                #sleep(1)
                hit = dump["queries"]["request"][0]["totalResults"]
                print(hit)
                for p in range(len(dump["items"])):
                    url_list.append(dump['items'][p]['link'])
                    title_list.append(dump['items'][p]['title'])
                    snippet_list.append(dump['items'][p]['snippet'].replace('\n',''))
                print(GREEN+'[len_list]-->'+str(len(dump["items"]))+ENDC)

                if int(hit) < 11:
                    cnt = 100
                api_counter = api_counter + 1
                cnt = cnt +10
            else:
                j = j + 1
                api_counter = 0
            print('_____________________________')

        with open('data.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\n') # 行末は改行
            for i,u in enumerate(url_list):
                data = [key,url_list[i],title_list[i],snippet_list[i]]
                writer.writerow(data)

        if len(dump["items"]) >= 1:
            return url_list,title_list,snippet_list,df_api,api_counter,j
        else:
            return ['no'],['no'],['no'],df_api,api_counter,j

    # if 503 or 403error returned (when the http server do not temporary accept your request)
    except Exception as e:
        try_cnt += 1
        sleep(1)
        if try_cnt <= 3:
            scrape_serps(phrase,maxrank,df_api,api_counter,j,try_cnt)
            #scrape_serps(key_,page,df_api,api_counter,j)
        else:
            print ('server error occured')
            #url_list.append('NULL')
            #title_list.append('NULL')
            #snippet_list.append('NULL')
            print(title_list)
            print(df_api)
            print(api_counter)
            print(j)
            #return url_list,title_list,snippet_list,df_api,api_counter,j




def main():
    api_counter = 0
    j = 0
    page = input("how many page do you want?(1or2)")
    page = int(page)
    df = pd.read_csv("suggest.csv",header=None)
    df.columns=["suggest"]
    sg = list(df["suggest"])

    urls = []
    titles = []
    snippets = []

    urls_ = []
    titles_ = []
    snippets_ = []

    sgs = []
    df_api = pd.read_csv("api.csv")
    ct = 0
    #print (sg)
    for key in sg:
        ct = ct + 1
        try_cnt = 0
        print ("")
        print (GREEN+str(ct)+ENDC)
        print("====================================")
        print(key)
        try: 
            url_list,title_list,snippet_list,df_api,api_counter,j = scrape_serps(key,page,df_api,api_counter,j,try_cnt)
            urls_.extend(url_list)
            titles_.extend(title_list)
            snippets_.extend(snippet_list)
            if url_list[0]!='NULL':
                for i in range(len(url_list)):#Deffault: page*10
                    sgs.append(key)
                urls += [url_list]
        except:
            print('exceptional error occured and skipped')
    #df_api.to_csv("api.csv")
    urls = pd.DataFrame(urls)
    titles = pd.DataFrame(titles)
    snippets = pd.DataFrame(snippets)
    df = pd.concat([df,urls],axis=1)
    df.to_csv("urls.csv")
    df_ = pd.concat([pd.Series(urls_),pd.Series(sgs)],axis=1)
    # web_id は自動で付与される
    df_.columns = ["url","suggest"]
    #df_.to_csv("sg_urls.csv")

    de = pd.concat([pd.Series(urls_), pd.Series(titles_), pd.Series(snippets_)],axis=1)
    de.columns = ["url","title","snippets"]
    #de.to_csv("url-title-snippet.csv")

main()
