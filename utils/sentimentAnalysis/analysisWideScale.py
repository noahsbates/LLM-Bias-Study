from transformers import pipeline
import statistics
import tqdm
import pandas as pd

from utils.dataRequest.generator import loadPoems

#### IMPORTANT:
# Because I started with mainly poems in mind, in this file I refer to multiple types of files such as both descriptions and poems as just 'poems' or 'poem'

from utils.basicData.presidentData import president_dict

president_df = pd.DataFrame(president_dict,index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])


def nlptownSentimentWide(path):
    print("hi")
    model_id = "nlptown/bert-base-multilingual-uncased-sentiment"
    sentiment_pipe = pipeline("sentiment-analysis", model=model_id)

    president_poem_ratings = {'name':[],'ratings':[]}

    for president_name in tqdm.tqdm(president_df['name'], desc="Getting sentiment..."):
        president_poems = loadPoems(path,president_name)['output']

        individual_president_total_set = []
        for i in tqdm.tqdm(president_poems, desc=f"Analyzing {president_name}..."):
            pres_sentiment = sentiment_pipe(i,top_k=None)

            totalRating = 0
            for label in pres_sentiment:
                if label['label'] == '5 stars':
                    totalRating = totalRating + label['score']
                elif label['label'] == '1 star':
                    totalRating = totalRating - label['score']
            individual_president_total_set.append(totalRating)
    

        president_poem_ratings['name'].append(president_name)
        president_poem_ratings['ratings'].append(individual_president_total_set)
    return president_poem_ratings


def cardiffnlpSentimentWide(path):

    model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    sentiment_pipe = pipeline("sentiment-analysis", model=model_id)

    president_poem_ratings = {'name':[],'ratings':[]}

    for president_name in tqdm.tqdm(president_df['name'], desc="Getting sentiment..."):
        president_poems = loadPoems(path,president_name)['output']

        individual_president_positive_set = []
        for i in tqdm.tqdm(president_poems, desc=f"Analyzing {president_name}..."):
            pres_sentiment = sentiment_pipe(i,top_k=None)

            totalRating = 0
            for label in pres_sentiment:
                if label['label'] == 'positive':
                    totalRating = totalRating + label['score']
                elif label['label'] == 'negative':
                    totalRating = totalRating - label['score']
            individual_president_positive_set.append(totalRating)

        president_poem_ratings['name'].append(president_name)
        president_poem_ratings['ratings'].append(individual_president_positive_set)

    return president_poem_ratings