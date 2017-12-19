# Mental Health in Switzerland
 Our notebook can be found at [project.ipynb](project.ipynb)
 Our report can be found at [report.pdf](report.pdf)


## Contributions
- Léonore : project formulation, methodology, data cleaning, NLP pipeline update, matching algorithm, plotting graphs,  writing report.
- Othman : data cleaning, NLP pipeline, labeling tweets, dictionary update, writing report, notebook organisation.
- Saskia : beautify graphs, proofread report and notebook.

## Abstract
Social media provide a unique look into people’s feelings and thoughts. Twitter, due to its relative anonymity, can provide a honest look at how people deal with taboo topics such mental illness. As such, aggregated data from Twitter has previously been used to identify depression in users, among other mental illnesses, but also to measure – on a smaller scale – the public’s opinion on this subject [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4217192/].

Our project aims to perform a large scale analysis of the expression of mental distress in  tweets posted in Switzerland. To achieve this goal, we iteratively build a set of search terms using manual inspection and topic modeling. This dictionary aims to identify mental illnesses and signs of mental distress in tweets.

Our dataset is refined using this dictionary, allowing us to analyze the resulting set of tweets.

## Research questions

- What percentage of tweets / how many accounts show mental indicators?
- Can we see a difference between the genders?
- Can we find seasonal patterns? Winter VS Summer?
- Can we see linguistic patterns? Regional patterns?
- To what extent is Twitter representative of the country’s health census?

## Dataset

### Dataset we are using
- Spinn3r Swiss tweets dataset
- twitter-swisscom dataset

### Methology
0. Data exploration, check if we can find any issues with Twitter data and make sure to handle them.
1. Use simple NLP methods to perform analysis on data set.
2. Determine a dictionary of keywords linked to mental health and emotion identifiers.
3. Filter tweets using the dictionary and construct a dataset we can work with on. 
4. Apply our methods to the $2^{nd}$ dataset (twitter-swisscom) to gain more insights.
5. Answer our research question using our filtered data.

## Internal milestone up until poster presentation (Jan. 29-30, 2018)

1. Work on the poster and presentation (19-29 January)

## Internal milestones up until project milestone 3 (Dec. 19, 2017) ✓

### 1. Finish NLP pipeline & label tweets & report basics (to be done before dec. 3th) ✓
1. Serialize the NLP pipeline using Spark (and run it on the cluster)
2. Label tweets so we can start performing the ML methods
3. Start writing the paper (Intoduction and Methology)

### 2. Analyze datset to respond to questions (to be done before dec. 10th) ✓
1. Build a classifier using labeled tweets
2. Use the LDA on the classifier to determine related words
3. Determine the most frequent words (or topics) in our dataset
4. Answer the question
- Look at the seasonal distribution (winter/summer)
- Look at the difference between categories (male/female, negative/neutral sentiment, languages)
- Look at the regional distribution (if possible given our data)
- Compare our results to the Swiss Mental Health Statistics

### 3. Finish report and analysis (until deadline dec. 19th) ✓
1. Finish the report
2. Clean the notebook

## Internal milestones up until project milestone 2 (Nov. 28, 2017) ✓
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
