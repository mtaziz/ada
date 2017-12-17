#!/usr/bin/python
import sys
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize, TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
import pickle

#FUNCTIONS
def dict_cleaning(dicts):
    return dicts.astype(str).str.lower()

def dict_remove_stops(dictionary, language):
    lang = language[:2]
    if language == 'german':
        lang = 'de'

    lang_set = stopwords.words(language)
    return dictionary.apply(lambda expression: [word for word in expression if word not in lang_set])

def dict_stem_words(dictionary, language):
    lang = language[:2]
    if language == 'german':
        lang = 'de'

    stemmer = SnowballStemmer(language)

    return dictionary.apply(lambda expression: [stemmer.stem(word) for word in expression])


def compare(s, t):
    return Counter(s) == Counter(t)

def match_dict(tweet, dict_):
    """returns keywords that match in string
    tweet: tweet to find keywords in
    dict_: list of keywords
    """
    doc = [sublist for sublist in dict_ if compare(list(filter(lambda x: x in tweet, sublist)), sublist) ]
    return doc#at least one match

print('starting script 💖')
df = pickle.load( open( "../data/spinn3r_tweets/processed_tweets.pkl", "rb" ))
print('loaded dataframe from pickle')

#load dictionary
DICT_PATH_POS = "../data/dictionaries/dict_2.2.csv"

DICT_PATH_NEG = '../data/dictionaries/neg_dict_1.1.csv'
dictionary_pos = pd.read_csv(DICT_PATH_POS)
dictionary_neg = pd.read_csv(DICT_PATH_NEG)

print('loaded dict')
#define languages for dict
en_dict_pos = dictionary_pos['english'].dropna()
en_dict_neg = dictionary_neg['english'].dropna()

#clean dict
en_dict_pos =  dict_cleaning(en_dict_pos)
en_dict_neg =  dict_cleaning(en_dict_neg)
print('cleaned dict')
#Tokenizing
tknzr = TweetTokenizer()

en_dict_pos = en_dict_pos.map(lambda x: tknzr.tokenize(x))
en_dict_neg = en_dict_neg.map(lambda x: tknzr.tokenize(x))
print('tokenized dict')
#Removing stop words
# en_dict_pos = dict_remove_stops(en_dict_pos, 'english')
# en_dict_neg = dict_remove_stops(en_dict_neg, 'english')

print('removed stops in dict')
#Stemming the words
en_dict_pos = dict_stem_words(en_dict_pos, 'english')
en_dict_neg = dict_stem_words(en_dict_neg, 'english')
print('stemmed words in dict')

no_neg = df[df.lang == 'en']['tokenized'].map(lambda x: len(match_dict(x, en_dict_neg)) == 0)

english = df[df.lang == 'en'][no_neg]['tokenized'].map(lambda x: match_dict(x, en_dict_pos))

df['keywords'] = english

print('found and added keywords: english')
df[df.lang == 'en'].to_pickle('../data/spinn3r_tweets/keyword_tweets/final_english_keyworded_tweets.pkl')
print('writing english keyword dataframe to pickel 🥒 🥒 😋')
