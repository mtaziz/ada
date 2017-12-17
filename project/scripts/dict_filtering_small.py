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
    return dicts.astype(str).str.lower().str.replace(r'[^\w\s]', ' ')

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
DICT_PATH = "../data/dictionaries/dict_1.csv"
dictionaries = pd.read_csv(DICT_PATH)

print('loaded dict')
#define languages for dict
en_dict = dictionaries['english'].dropna()
fr_dict = dictionaries['french'].dropna()
de_dict = dictionaries['german'].dropna()

#clean dict
en_dict = dict_cleaning(en_dict)
fr_dict = dict_cleaning(fr_dict)
de_dict = dict_cleaning(de_dict)
print('cleaned dict')
#Tokenizing
tknzr = TweetTokenizer()

en_dict = en_dict.map(lambda x: tknzr.tokenize(x))
fr_dict = fr_dict.map(lambda x: tknzr.tokenize(x))
de_dict = de_dict.map(lambda x: tknzr.tokenize(x))
print('tokenized dict')
#Removing stop words
# fr_dict = dict_remove_stops(fr_dict, 'french')
# en_dict = dict_remove_stops(en_dict, 'english')
# de_dict = dict_remove_stops(de_dict, 'german')

print('removed stops in dict')
#Stemming the words
en_dict = dict_stem_words(en_dict, 'english')
fr_dict =  dict_stem_words(fr_dict, 'french')
de_dict =  dict_stem_words(de_dict, 'german')
print('stemmed words in dict')

english= df[df.lang == 'en']['tokenized'].map(lambda x: match_dict(x, en_dict))
df['keywords'] = english
print('found and added keywords: english')
df[df.lang == 'en'].to_pickle('../data/spinn3r_tweets/keyword_tweets/small_english_keyworded_tweets.pkl')
print('writing english keyword dataframe to pickel 🥒 🥒 😋')


df['keywords']= df[df.lang == 'de']['tokenized'].map(lambda x: match_dict(x, de_dict))
print('found and added keywords: german')
df[df.lang == 'de'].to_pickle('../data/spinn3r_tweets/keyword_tweets/small_german_keyworded_tweets.pkl')
print('writing german keyword dataframe to pickel 🥒 🥒 😋')


df['keywords']= df[df.lang == 'fr']['tokenized'].map(lambda x: match_dict(x, fr_dict))
print('found and added keywords: french')
df[df.lang == 'fr'].to_pickle('../data/spinn3r_tweets/keyword_tweets/small_french_keyworded_tweets.pkl')
print('writing french keyword dataframe to pickel 🥒 🥒 😋')
