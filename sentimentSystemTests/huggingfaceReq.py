from transformers import pipeline
import tqdm
import pandas as pd

from utils.dataRequest.generator import loadPoems

#### IMPORTANT:
# Because I started with mainly poems in mind, in this file I refer to multiple types of data such as both descriptions and poems as just 'poems' or 'poem'

from utils.basicData.presidentData import president_dict

# testPhrases replace NAME with the president name

def nlptownSentiment(testPhrases):

    model_id = "nlptown/bert-base-multilingual-uncased-sentiment"
    sentiment_pipe = pipeline("sentiment-analysis", model=model_id)

    president_poem_ratings = {'name':[],'ratings':[]}

    for president_name in tqdm.tqdm(president_dict['name'], desc="Getting sentiment..."):

        #Create test phrases for each president
        president_poems = []
        for i in testPhrases:
            president_poems.append(i.replace("NAME", president_name))

        individual_president_5star_set = []
        for i in tqdm.tqdm(president_poems, desc=f"Analyzing {president_name}..."):
            pres_sentiment = sentiment_pipe(i,top_k=None)

            for label in pres_sentiment:
                if label['label'] == '5 stars':
                    individual_president_5star_set.append(label['score'])
                    break

        president_poem_ratings['name'].append(president_name)
        president_poem_ratings['ratings'].append(individual_president_5star_set)

    return president_poem_ratings


def cardiffnlpSentiment(testPhrases):

    model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    sentiment_pipe = pipeline("sentiment-analysis", model=model_id)

    president_poem_ratings = {'name':[],'ratings':[]}

    for president_name in tqdm.tqdm(president_dict['name'], desc="Getting sentiment..."):

        #Create test phrases for each president
        president_poems = []
        for i in testPhrases:
            president_poems.append(i.replace("NAME", president_name))

        individual_president_positive_set = []
        for i in tqdm.tqdm(president_poems, desc=f"Analyzing {president_name}..."):
            pres_sentiment = sentiment_pipe(i,top_k=None)

            for label in pres_sentiment:
                if label['label'] == 'positive':
                    individual_president_positive_set.append(label['score'])
                    break

        president_poem_ratings['name'].append(president_name)
        president_poem_ratings['ratings'].append(individual_president_positive_set)

    return president_poem_ratings
