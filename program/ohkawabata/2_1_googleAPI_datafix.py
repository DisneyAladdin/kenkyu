import pandas as pd


df = pd.read_csv("data.csv",header = None)
df.columns=["suggest","url","title","snippet"]

df1 = pd.DataFrame(df["url"])
df1["suggest"] = df["suggest"]
df1.to_csv("sg_urls.csv")


df2 = pd.DataFrame(df["url"])
df2["title"] = df["title"]
df2["snippet"] = df["snippet"]
df2.to_csv("url-title-snippet.csv")
