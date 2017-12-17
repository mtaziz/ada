import numpy as np
import pandas as pd

from nltk.tokenize import word_tokenize, TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

#FUNCTIONS:
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

    cleaned.loc[cleaned['lang'] == lang, frame] = cleaned.loc[cleaned['lang'] == lang, frame].\
        apply(lambda tweet: [stemmer.stem(word) for word in tweet])

#read from json
df = pd.read_json('../data/spinn3r_tweets/tweets.json', lines=True)

#changing time
df['published'] = pd.to_datetime(df['published'])
#removing @ and punctuation => we add a space so that j'ai becomes j ai,
#for better tokenizing
df['cleaned'] = df['main'].str.replace("@\S+", '')
df['cleaned'] = df['cleaned'].str.replace('_', '') #not removed by following regex
df['cleaned'] = df['cleaned'].str.replace(r'[^\w\s]', ' ')

print('cleaned!')
#tokenize
tknzr = TweetTokenizer()
tokenized = df['cleaned'].map(lambda x: tknzr.tokenize(x))
print('tokenized!')
df['tokenized'] = tokenized
#stopword removal
# remove_stops('english', df, 'tokenized')
# remove_stops('french', df, 'tokenized')
# remove_stops('german', df, 'tokenized')
# print('stopwords are gone!')
#stem words
stem_words('english', df, 'tokenized')
stem_words('french', df, 'tokenized')
stem_words('german', df, 'tokenized')
print('stemmed words!')
df.to_pickle('../data/spinn3r_tweets/processed_tweets.pkl')
print('done! 💅 😍')
