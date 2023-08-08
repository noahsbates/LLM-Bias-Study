import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np

from sentimentSystemTests.huggingfaceReq import nlptownSentiment
from sentimentSystemTests.huggingfaceReq import cardiffnlpSentiment

from utils.basicData.presidentData import president_dict

#measure inherant bias in sentiment systems rating LLM outputs
def presidentSentimentSystemTest(testPhrases):
    nlptownSentimentOut = nlptownSentiment(testPhrases)
    cardiffnlpSentimentOut = cardiffnlpSentiment(testPhrases)

    return [nlptownSentimentOut,cardiffnlpSentimentOut]

#Jeez these variable names are getting out of control
def graphPresidentSentimentSystemTest(testPhrases):
    output = presidentSentimentSystemTest(testPhrases)

    for i in output:
        df = pd.DataFrame(i)
        df['party'] = president_dict['party']

        sns.set(style="ticks")
        sns.set_style("darkgrid")

        expanded_df = df.explode('ratings')

        # Convert 'ratings' column to numeric
        expanded_df['ratings'] = pd.to_numeric(expanded_df['ratings'])

        avg_ratings = expanded_df.groupby('party')['ratings'].mean()

        party_colors = {'D': 'lightblue', 'R': 'lightcoral'}
        sns.set_palette(party_colors.values())

        print(expanded_df)
        ax = sns.scatterplot(data=expanded_df, x='name', y='ratings', hue='party', s=100)

        for party, avg_rating in avg_ratings.items():
            print(party, avg_rating)
            ax.axhline(y=avg_rating, color=party_colors[party], linestyle='--', label=f'Avg. {party} Rating')

        plt.ylabel('President Rating')
        plt.title('Title Here')
        plt.legend()

        plt.show()
