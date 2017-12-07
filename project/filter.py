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
def dict_cleaning(lang):
    lang_dict = eval(lang + '_dict')
    lang_dict = lang_dict.astype(str).str.lower()

def dict_remove_stops(language):
    lang = language[:2]
    if language == 'german':
        lang = 'de'

    lang_dict = eval(lang + '_dict')
    lang_set = stopwords.words(language)
    lang_dict = lang_dict.apply(lambda expression: [word for word in expression if word not in lang_set])

def dict_stem_words(language):
    lang = language[:2]
    if language == 'german':
        lang = 'de'

    lang_dict = eval(lang + '_dict')
    stemmer = SnowballStemmer(language)

    lang_dict = lang_dict.apply(lambda expression: [stemmer.stem(word) for word in expression])

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
df = pickle.load( open( "processed_tweets.pkl", "rb" ))
print('loaded dataframe from pickle')

#load dictionary
DICT_PATH = "dictionary.csv"
dictionaries = pd.read_csv(DICT_PATH)

print('loaded dict')
#define languages for dict
en_dict = dictionaries['english'].dropna()
fr_dict = dictionaries['french'].dropna()
de_dict = pd.concat([dictionaries['german'].dropna(), dictionaries['swiss_german'].dropna()])

#clean dict
dict_cleaning('en')
dict_cleaning('fr')
dict_cleaning('de')
print('cleaned dict')
#Tokenizing
tknzr = TweetTokenizer()

en_dict = en_dict.map(lambda x: tknzr.tokenize(x))
fr_dict = fr_dict.map(lambda x: tknzr.tokenize(x))
de_dict = de_dict.map(lambda x: tknzr.tokenize(x))
print('tokenized dict')
#Removing stop words
dict_remove_stops('english')
dict_remove_stops('french')
dict_remove_stops('german')

print('removed stops in dict')
#Stemming the words
dict_stem_words('english')
dict_stem_words('french')
dict_stem_words('german')
print('stemmed words in dict')

df['keywords']= df[df.lang == 'en']['tokenized'].map(lambda x: match_dict(x, en_dict))
print('found and added keywords: english')
df['keywords']= df[df.lang == 'de']['tokenized'].map(lambda x: match_dict(x, de_dict))
print('found and added keywords: german')
df['keywords']= df[df.lang == 'fr']['tokenized'].map(lambda x: match_dict(x, fr_dict))
print('found and added keywords: french')

del df['tags'], df['cleaned']

df.to_pickle('keyworded_tweets.pkl')
print('writing keyword dataframe to pickel 🥒 🥒 😋')
