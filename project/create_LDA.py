#!/usr/bin/python
import sys
from gensim import corpora, models
import numpy as np
import pandas as pd

import pyLDAvis.gensim
import pickle

#read from line
lang = sys.argv[1]
topics = int(sys.argv[2])

#read from pickle
df = pickle.load( open( "processed_tweets.pkl", "rb" ))
print('loaded from pickle')
language_df = df[df.lang == lang].tokenized
#get einglish words
dictionary = corpora.Dictionary(language_df)
#remove overly common and too rare
dictionary.filter_extremes(no_below=3, no_above=.5)
print('created dictionary')
texts = language_df.tolist()
corpus = [dictionary.doc2bow(text) for text in texts]
print('created corpus')
ldamodel = models.LdaMulticore(corpus, id2word=dictionary, num_topics=topics, workers=3) #takes like 5minutes on leo's pc
print('built model')
ldamodel.save('general_lda_'+lang+'.model')
print('saving model 💾')
