from transformers import pipeline
from generator import loadDescriptions
import statistics
import tqdm
import pandas as pd
print('Finished Analysis Imports.')

model_id = "nlptown/bert-base-multilingual-uncased-sentiment"
sentiment_pipe = pipeline("sentiment-analysis", model=model_id)

president_dict = {'name' : ['Joe Biden', 'Donald Trump', 'Barack Obama', 'George W. Bush', 'Bill Clinton', 'George H. W. Bush', 'Ronald Reagan', 'Jimmy Carter', 'Gerald Ford', 'Richard Nixon', 'Lyndon B. Johnson', 'John F. Kennedy', 'Dwight D. Eisenhower', 'Harry S. Truman', 'Franklin D. Roosevelt', 'Herbert Hoover', 'Calvin Coolidge', 'Warren G. Harding', 'Woodrow Wilson', 'William Howard Taft', 'Theodore Roosevelt', 'William McKinley', 'Grover Cleveland'],
                  'party': ['D','R','D','R','D','R','R','D','R','R','D','D','R','D','D','R','R','R','D','R','R','R','D'],
                  'num'  : [46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24]
                  }
president_df = pd.DataFrame(president_dict,index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])


def sentimentLook():

    president_description_ratings = {'name':[],'ratings':[]}

    for president_name in tqdm.tqdm(president_df['name'], desc="Getting sentiment..."):
        president_descriptions = loadDescriptions(president_name)['output']

        individual_president_5star_set = []
        for i in tqdm.tqdm(president_descriptions, desc=f"Analyzing {president_name}..."):
            pres_sentiment = sentiment_pipe(i,top_k=None)

            for label in pres_sentiment:
                if label['label'] == '5 stars':
                    individual_president_5star_set.append(label['score'])
                    break

        president_description_ratings['name'].append(president_name)
        president_description_ratings['ratings'].append(individual_president_5star_set)

    return president_description_ratings


def meanSentimentLook():
    sentimentLookOut = sentimentLook()
    president_description_ratings_mean = sentimentLookOut
    president_description_ratings_len = len(sentimentLookOut['ratings'])

    for i in range(president_description_ratings_len):
        president_description_ratings_mean['ratings'][i] = statistics.mean(president_description_ratings_mean['ratings'][i])

    return president_description_ratings_mean
