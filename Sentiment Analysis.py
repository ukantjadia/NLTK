# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 01:16:41 2023

@author: Yousha
"""

import pandas as pd
df = pd.read_csv('edited_tweets.csv')
df.head()
df.drop(df.columns[0], axis=1, inplace=True)

from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm

sia = SentimentIntensityAnalyzer()

res = {}
for i, row in tqdm(df.iterrows(), total=len(df)):
    text = row['content'] 
    id = row['id'] 
    res[id] = sia.polarity_scores(text)
    
sa = pd.DataFrame(res).T
sa = sa.reset_index()
sa = sa.rename(columns={'index':'id'})
sa_df = sa.merge(df, on='id',how='right')

sa_df = sa_df[['id','date','content','username','likeCount','retweetCount','neg','neu','pos','compound']]

sa_df.to_csv('sentiment_analyzed_tweets.csv', index=None)
