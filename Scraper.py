# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 22:40:54 2023

@author: Yousha
"""

import pandas as pd
from tqdm import tqdm    # To display loading bar
import snscrape.modules.twitter as sntwitter

scraper = sntwitter.TwitterSearchScraper("#chatgpt")

tweets = []
n_tweets = 100_000

for i, tweet in tqdm(enumerate(scraper.get_items()), total=n_tweets):
    data = [
            tweet.date,
            tweet.id,
            tweet.rawContent,
            tweet.user.username,
            tweet.likeCount,
            tweet.retweetCount
            ]
    tweets.append(data)
    if i == n_tweets:
        break

tweets_df = pd.DataFrame(tweets, columns=["date","id","content","username","likeCount","retweetCount"])
tweets_df.head()

tweets_df.date = pd.to_datetime(tweets_df.date)
tweets_df.dtypes

# Output
tweets_df.to_csv('tweets_data.csv',index=None)
