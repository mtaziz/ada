# Mental Health in Switzerland

## Abstract
Social media, such as Twitter, provide a unique look into people’s feelings and thoughts. As such, aggregated data from social media has previously been successfully used to identify depression and other mental illnesses in users. However, most studies on this subject tend to focus only on clinical depression, which is a very specific condition that is not indicative of the general mental health of the population.

Switzerland has one of the best mental health infrastructures, indicating that mental health probably is a problem within the population (on average, 10% of the Swiss population will have at least a depression in their life). Nevertheless, society still stigmatizes these issues, which is why we turn to social media to get a better picture of mental health in the country by focusing on more general indicators of mental health disorders.

To achieve this goal, we use simple natural language processing methods to get more insights into the affected population.

## Research questions

### Mental Health : where we stand {IMPROVED}
- What indicators of mental health issues can we find in tweets? (We already define our own dictionnary. However, we suppose that using other methods, we can find more related word, giving the needed insights.)
- What percentage of tweets / how many accounts show such indicators?
- Can we see a difference between the genders ?
- Can we find seasonal patterns? Winter VS Summer? (Seasonal Affective Disorder for the year 2016)
- Can we see linguistic patterns? (This would allow us to have an insight on the Röstigraben issue)
- To what extent is Twitter representative of the country’s health census?

### Mental Health: what we think about it {REMOVED}

We looked at the given datasets but found that there was not enough available information covering our subject. Moreover, as you mentioned in the 1st milestone feedback, the 1st research question is already a lot of work. For both reasons, we decided to drop this question.

## Dataset

### Dataset we are using
- Spinn3r swiss tweets dataset

### Methology
0. Data exploration, check if we can actualy find any issues with twitter data and make sure to handle them. (For example depression can be used in an economic way).
1. Use simple natural language processing methods (LSI, pLSI, LDA and VSM using lemmatization, stemming and n-grams) to preform analysis on data set.
2. Determine a dictionary of keywords linked to mental health and emotion identifiers (and possibly (if time allows) use Machine Learning algorithms to broaden it along our work).
3. Filter tweets by the dictionary and construct a dataset we can work with on. Such as, number of tweets containing dictonary entry by region, season, language.
4. Find trends allowing us to broaden our research or tweak our model to iterate on those steps.
5. Use the news data set by using keywords from the dictionary (previously built).

## A list of internal milestones up until project milestone 3

### 1. Handle the raw data & general data analysis (to be done before nov. 12th)
0. Check how we get data on our computer and how we can handle the large volume of data.
1. Learn how the dataset is encoded, how specific the geomarkers are, and if sentiment stamps are useful to our question.
2. Look at the overall distribution of the tweets' languages, and check for issues with non-standardization of Swiss German.
    -> also look at regional distribution.
3. Look at how frequent the use of emojis is, what methods to use to handle them.
4. Look into handling time dimension of data, look at distribution of tweets over time.
5. See to what extent Swiss News outlets talk about mental health.
6. Find potential issues with data, are there any NaN values, how can we deal with bots and spam etc.
(*Read papers that might give us interesting insights)

### 2. See how we can transform the data (to be done before nov. 18th)
1. Look more closely into what NLP techniques work best on our data and begin to form our dictionary.
2. Filter the tweets down to a dataset that interests us, check if size of dataset is reasonable.
3. Check how we can look at the tweets in a temporal manner, what statistical tools we should use to be able to draw conclusions.
4. Look into ways we can visualize our data.

### 3. Work on notebook and future plans (until deadline nov. 28th)

1. Work on properly commented notebook that can be read by people outside the team.
2. Have a nice visualisations and first results in notebook.

## A list of internal milestones up until project milestone 2
<_We will discuss all these questions in the Notebooks. We only keep this on the README so that you that can see the problems we tackled._>

### 1. Handle the raw data & general data analysis (to be done before nov. 12th)
0. Check how we get data on our computer and how we can handle the large volume of data.
1. Learn how the dataset is encoded, how specific the geomarkers are, and if sentiment stamps are useful to our question.
2. Look at the overall distribution of the tweets' languages, and check for issues with non-standardization of Swiss German.
    -> also look at regional distribution.
3. Look at how frequent the use of emojis is, what methods to use to handle them.
4. Look into handling time dimension of data, look at distribution of tweets over time.
5. See to what extent Swiss News outlets talk about mental health.
6. Find potential issues with data, are there any NaN values, how can we deal with bots and spam etc.
(*Read papers that might give us interesting insights)

### 2. See how we can transform the data (to be done before nov. 18th)
1. Look more closely into what NLP techniques work best on our data and begin to form our dictionary.
2. Filter the tweets down to a dataset that interests us, check if size of dataset is reasonable.
3. Check how we can look at the tweets in a temporal manner, what statistical tools we should use to be able to draw conclusions.
4. Look into ways we can visualize our data.

### 3. Work on notebook and future plans (until deadline nov. 28th)

1. Work on properly commented notebook that can be read by people outside the team.
2. Have a nice visualisations and first results in notebook.

# Questions for TAs
1. What is a good scope of the projet, e.g. is our project too ambitious or not ambitious enough?
-> The mental health stigma part might be too much and we weren't sure if we should include it or not/or instead center our project around it.
-> What are the 'expecations'?
2. Regarding the second step of our methodology, can we use external libraries or help to define the dictionary?
3. How should we best get data from the 200 years news source, how can we deal with the issue that it only covers francophone media? Can we use other new sources to have more recent data (same time as tweets)?


