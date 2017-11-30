df = sqlContext.read.json('/datasets/swiss-tweet/')

#remove nesting
df = df.select('_source.*')

#columns we care about
columns = ['main', 'published', 'source_spam_probability', 'source_location', 'tags', 'lang', 'sentiment',
                   'author_gender', 'source_followers', 'source_following']

#get only relevant columns
df = df[columns]

df = df.filter(df.lang.isin('en', 'de', 'fr'))  #gets tweets with right language
df = df.filter(df.sentiment != 'POSITIVE') #remove positive sentient tweets
df = df.filter(df.source_spam_probability < 0.5) #remove spam
df = df.withColumn('main', lower(df.main)) #get lower case

df = df.withColumn('main', regexp_replace(col('main'), 'pic.twitter\S+', ' '))#remove picture urls
df = df.withColumn('main', regexp_replace(col('main'), '@\S+', ' '))#remove mentions

#remove websites and retweets
df = df.filter(~(df.main.contains('http')))\
    .filter(~(df.main.contains('.com')))\
    .filter(~(df.main.contains('.ch')))\
    .filter(~(df.main.contains('www')))\
    .filter(~(df.main.contains('RT')))


df.write.json('/user/benchekr/reduced_tweets') #write dataframe to folder in json format
