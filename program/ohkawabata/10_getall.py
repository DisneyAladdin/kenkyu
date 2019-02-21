# coding:utf-8
import os
import re
import time
from urllib import request
from urllib.parse import urljoin
from urllib.request import urlparse, urlretrieve

from bs4 import BeautifulSoup

# 処理済み判断変数
proc_files = {}

# HTML内のリンクを抽出


def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']")  # CSS
    links += soup.select("a[href]")  # リンク
    result = []
    # href を取り出し，リンクを絶対パスに変換
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result


# ファイルをダウンロードし保存する関数
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$", savepath):  # ディレクトリならindex.html
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    # すでにダウンロード済み？
    if os.path.exists(savepath):
        return savepath
    # ダウンロード先のディレクトリを作成
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        os.makedirs(savedir)
    # ファイルをダウンロード
    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print("ダウンロード失敗")
        return None

# HTMLを解析してダウンロードする関数


def analize_html(url, root_url):
    savepath = download_file(url)
    if savepath is None:
        return
    if savepath in proc_files:
        return  # 解析済みなら処理しない
    proc_files[savepath] = True
    print("analize_html=", url)
    # リンクを抽出
    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)
    for link_url in links:
        # リンクがルート以外のパスを指定していたら無視
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url):
                continue
        # HTMLか？
        if re.search(r".(html|htm)$", link_url):
            # 再帰的にHTMLファイルを解析
            analize_html(link_url, root_url)
            continue
        # それ以外のファイル
        download_file(link_url)


if __name__ == "__main__":
    # URLを丸ごとダウンロード
    url = "https://to-kei.net/"
    analize_html(url, url)
