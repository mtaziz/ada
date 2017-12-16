import csv
import numpy as np
import pandas as pd
import pyspark as ps
from langdetect import detect

schema = pd.read_table('../data/twitter-swisscom/schema.txt', header=None, delim_whitespace=True, index_col=0,
                       names=['name', 'type', 'specification', '??', 'format'] )

twitter_df = pd.read_table('../data/twitter-swisscom/twex.tsv',
              sep='\t', engine='c', encoding='utf-8', quoting=csv.QUOTE_NONE,
              header=None, names=schema.name, na_values=['\\N', ' NaN'])


def detect_lang(word):
    try: x = detect(word)
    except: x = 'undef'
    return x

del twitter_df['placeId']
del twitter_df['source']
del twitter_df['sourceName']
del twitter_df['id']

twitter_df['text'] = twitter_df['text'].dropna()

twitter_df['text'] = twitter_df['text'].astype(str)

twitter_df['text'] = twitter_df['text'].str.lower()

url_mask = twitter_df['text'].str.contains("www\S+") | \
twitter_df['text'].str.contains("http\S+") | \
twitter_df['text'].str.contains(".ch") | \
twitter_df['text'].str.contains(".com")\
| twitter_df['text'].str.contains("rt")

twitter_df['text'] = twitter_df['text'].str.replace("pic.twitter\S+", '')
twitter_df.drop(twitter_df[url_mask].index, inplace=True)

twitter_df.text = twitter_df.text.str.replace('\((.+?)\)', '', case=False)#remove content in ()
twitter_df.text = twitter_df.text.str.replace('([^\s\w]|_)+','', case=False)#remove non alphanumeric (needed for language dec)
twitter_df = twitter_df[twitter_df.text.map(lambda x: len(x)) > 5 ] #remove small words
twitter_df = twitter_df[twitter_df.text != 'nan']

twitter_df.reset_index(drop=True, inplace=True)
twitter_df['text'] = twitter_df['text'].astype(str)

twitter_df = twitter_df[twitter_df['text'].map(detect_lang).map(lambda x: x in ['en', 'fr', 'de'])]

twitter_df.to_json('processed_d1.json')
