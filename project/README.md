# Title

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?

Social media, such as Twitter, provide a unique look into people’s feelings and thoughts. As such, aggregated data from social media has previously been successfully used to identify depression and other mental illnesses in users.
However, most studies on this subject tend to focus only on clinical depression, which is a very specific condition that is not indicative of the general mental health of the population.
Switzerland has one of the best mental health infrastructures, indicating that mental health is a problem within the population. But society still stigmatizes these issues, which is why we turn to social media to get a better picture of mental health in the country by focusing on more general indicators of mental health disorders.
We use simple natural language processing methods to get more insights into the affected population and how they are perceived by the Swiss society.


# Research questions
A list of research questions you would like to address during the project.


## Mental Health : where we stand
- What indicators of mental health issues can we find in Tweets?
- What percentage of tweets / how many accounts show such indicators?
- Can we find seasonal patterns? Winter vs summer? (Seasonal Affective Disorder)
- Can we see regional patterns? Countryside vs city? Can we find increased levels of mental illness indicators around high stress areas such as EPFL?
- To what extent is Twitter representative of the country’s health census?

## Mental Health: what we think about it

- Can we identify stigmatization of mental health based on tweets?
- If so, to what extent is it present?
- How has this image changed over time?

# Dataset
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

## Datasets
- Swiss tweets dataset
- 200 years news (however, ends in 1998)
- News on the Web (how much does it represent Swiss views on mental illness?)

## Methology

1. Use simple natural language processing methods (LSI, pLSI, LDA and VSM using lemmatization, stemming and n-grams) to retrieve a dataset easy to work with
2. Determine a dictionary of keywords linked to mental health and emotion identifiers (and use Machine Learning algorithms to broaden it along our work)
3. Use the emojis in order to define the best elements
4. Find trends allowing us to broaden our research or tweak our model to iterate on these steps



# A list of internal milestones up until project milestone 2
Add here a sketch of your planning for the next project milestone.

1. See how dataset is coded, how specific the geomarkers are, and if sentiment stamps are useful to our question
2. Look at the languages of the tweets (overall distribution, issues with Swiss German), find way to filter tweets that interest us
3. See to what extent swiss news outlets talk about mental health


# Questions for TAa
Add here some questions you have for us, in general or project-specific.

1. What is a good scope of the projet, e.g. is our project too ambitious or not ambitious enough?
2. Regarding the second step of our methodology can we use external libraries or help to define the dictionary?



