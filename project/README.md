# Mental Health in Switzerland
 Our notebook can be found at [project.ipynb](project.ipynb)


## Contributions
- Léonore : Project formulation, methodology, matching algorithm, plotting graphs, data cleaning, writing report, NLP pipeline update
- Othman : NLP pipeline, data cleaning, labeling tweets, dictionary update, writing report, notebook organisation
- Saskia : Beautify graphs, proofread report and notebook

(yes we were basically two people working on this projet )

## Abstract
Social media, such as Twitter, provide a unique look into people’s feelings and thoughts. As such, aggregated data from social media has previously been successfully used to identify depression and other mental illnesses in users. However, most studies on this subject tend to focus only on clinical depression, which is a very specific condition that is not indicative of the general mental health of the population.

Switzerland has one of the best mental health infrastructures, indicating that mental health probably is a problem within the population (on average, 10% of the Swiss population will have at least a depression in their life). Nevertheless, society still stigmatizes these issues, which is why we turn to social media to get a better picture of mental health in the country by focusing on more general indicators of mental health disorders.

To achieve this goal, we use simple natural language processing methods to get more insights into the affected population.

## Research questions

### Mental Health : where we stand
- What indicators of mental health issues can we find in tweets? (We already define our own dictionnary. However, we suppose that using other methods, we can find more related word, giving the needed insights.)
- What percentage of tweets / how many accounts show such indicators?
- Can we see a difference between the genders ?
- Can we find seasonal patterns? Winter VS Summer? (Seasonal Affective Disorder for the year 2016)
- Can we see linguistic patterns? (This would allow us to have an insight on the Röstigraben issue)
- To what extent is Twitter representative of the country’s health census?

## Dataset

### Dataset we are using
- Spinn3r swiss tweets dataset

### Methology
0. Data exploration, check if we can actualy find any issues with twitter data and make sure to handle them. (For example depression can be used in an economic way).
1. Use simple natural language processing methods (LDA using stemming and n-grams) to preform analysis on data set.
2. Determine a dictionary of keywords linked to mental health and emotion identifiers (and possibly, if time allows, use Machine Learning algorithms to broaden it along our work).
3. Filter tweets by the dictionary and construct a dataset we can work with on. Such as, number of tweets containing dictonary entry by region, season, language.
4. Find trends allowing us to broaden our research or tweak our model to iterate on those steps.
5. Use the news data set by using keywords from the dictionary (previously built).

## A list of internal milestones up until project milestone 3

### 1. Finish NLP pipeline & label tweets & report basics (to be done before dec. 3th)
1. Serialize the NLP pipeline using Spark (and run it on the cluster)
2. Label tweets so we can start performing the ML methods
3. Start writing the paper (Intoduction and Methology)

### 2. Analyze datset to respond to questions (to be done before dec. 10th)
1. Build a classifier using labeled tweets
2. Use the LDA on the classifier to determine related words
3. Determine the most frequent words (or topics) in our dataset
4. Answer the question
- Look at the seasonal distribution (winter/summer)
- Look at the difference between categories (male/female, negative/neutral sentiment, languages)
- Look at the regional distribution (if possible given our data)
- Compare our results to the Swiss Mental Health Statistics

### 3. Finish report and analysis (until deadline dec. 19th)
1. Finish the report
2. Clean the notebook

## Internal milestone up until poster presentation (Jan. 29-30, 2018)

1. Work on the poster and presentation (19-29 January)

## A list of internal milestones up until project milestone 2 ✓
<_We will discuss all these questions in the Notebooks. We only keep this on the README so that you that can see the problems we tackled._>

### 1. Handle the raw data & general data analysis (to be done before nov. 12th)
0. Check how we get data on our computer and how we can handle the large volume of data. ✓
1. Learn how the dataset is encoded, how specific the geomarkers are, and if sentiment stamps are useful to our question. ✓
2. Look at the overall distribution of the tweets' languages, and check for issues with non-standardization of Swiss German. ✓
3. Look at how frequent the use of emojis is, what methods to use to handle them. _(removed from research question)_
4. Look into handling time dimension of data, look at distribution of tweets over time. ✓
5. See to what extent Swiss News outlets talk about mental health. _(removed from research question)_
6. Find potential issues with data, are there any NaN values, how can we deal with bots and spam etc. ✓
(*Read papers that might give us interesting insights)

### 2. See how we can transform the data (to be done before nov. 18th)
1. Look more closely into what NLP techniques work best on our data and begin to form our dictionary. ✓
2. Filter the tweets down to a dataset that interests us, check if size of dataset is reasonable. ✓
3. Check how we can look at the tweets in a temporal manner, what statistical tools we should use to be able to draw conclusions. _(not a big issue as we only have tweets over a period of 10 months)_
4. Look into ways we can visualize our data. ✓ _(barcharts and co., folium)_

### 3. Work on notebook and future plans (until deadline nov. 28th)

1. Work on properly commented notebook that can be read by people outside the team. ✓
2. Have a nice visualisations and first results in notebook. _(not really needed at this point, dataset was provided late)_

# Questions for TAs
