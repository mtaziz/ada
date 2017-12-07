import numpy as np
import pandas as pd
import pyspark as ps
import matplotlib.pyplot as plt
import csv

import unicodedata

from nltk.tokenize import word_tokenize, TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

from gensim import corpora, models

import pyLDAvis.gensim

#functions:
def remove_stops(language, cleaned, frame):
    lang = language[:2]
    if language == 'german':
        lang = 'de'
    lang_set = stopwords.words(language)
    cleaned.loc[cleaned['lang'] == lang, frame] = cleaned.loc[cleaned['lang'] == lang, frame].\
        apply(lambda tweet: [word for word in tweet if word not in lang_set])


def stem_words(language, cleaned, frame):
    lang = language[:2]
    if language == 'german':
        lang = 'de'

    stemmer = SnowballStemmer(language)

    cleaned.loc[cleaned['lang'] == lang, frame] = cleaned.loc[cleaned['lang'] == lang, frame]. \
        apply(lambda tweet: [stemmer.stem(word) for word in tweet])
#main executable

df = pd.read_json('tweets.json', lines=True)
tokenized = df['main'].map(lambda x: tknzr.tokenize(x))

tokenized.to_pickle('tokenized_strings.pkl')

df['tokenized'] = tokenized

remove_stops('english', df, 'tokenized')
stem_words('english', df, 'tokenized')