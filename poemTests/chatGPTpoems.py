import pandas as pd
import os
import openai
import tqdm
from statistics import mean

import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

from utils.dataRequest.generator import generatePoems

from utils.sentimentAnalysis.analysis import nlptownSentiment
from utils.sentimentAnalysis.analysis import cardiffnlpSentiment

#Notes: results2.csv was analyzed with nlptown/bert-base-multilingual-uncased-sentiment
#       results3.csv was analyzed with cardiffnlp/twitter-roberta-base-sentiment-latest

president_dict = {'name' : ['Joe Biden', 'Donald Trump', 'Barack Obama', 'George W. Bush', 'Bill Clinton', 'George H. W. Bush', 'Ronald Reagan', 'Jimmy Carter', 'Gerald Ford', 'Richard Nixon', 'Lyndon B. Johnson', 'John F. Kennedy', 'Dwight D. Eisenhower', 'Harry S. Truman', 'Franklin D. Roosevelt', 'Herbert Hoover', 'Calvin Coolidge', 'Warren G. Harding', 'Woodrow Wilson', 'William Howard Taft', 'Theodore Roosevelt', 'William McKinley', 'Grover Cleveland'],
                  'party': ['D','R','D','R','D','R','R','D','R','R','D','D','R','D','D','R','R','R','D','R','R','R','D'],
                  'num'  : [46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24],
                  'year' : [1893, 1897, 1901, 1909,1913, 1921, 1923, 1929, 1933, 1945, 1953, 1961, 1963, 1969, 1974, 1977, 1981, 1989, 1993, 2001, 2009, 2017, 2021]
                  }

president_df = pd.DataFrame(president_dict,index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])

######## Generating The Poems ########

def createPoems():
    for president_name in tqdm.tqdm(president_df['name'][1:],desc='Presidents Poems'):
      poems = generatePoems(president_name, poemcount = 100)
      poems.to_csv(f"poemTests/politicalPoems/{president_name}.csv")

######## Different Analysis Algorithms ########

def calculateResults2 ():
    results = pd.DataFrame(nlptownSentiment("poemTests/politicalPoems"), index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])
    saveResults(results,"results2")

def calculateResults3 ():
    results = pd.DataFrame(cardiffnlpSentiment("poemTests/politicalPoems"), index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])
    saveResults(results,"results3")

######## Different Analysis Algorithms ########

#Not to be used outside of this file
def saveResults (results,resultsName):
    results = results.set_index([[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24]])
    #results = results.drop(['Unnamed: 0'], axis=1)
    results['party'] = president_df['party']
    years = president_dict['year'].copy()
    years.reverse()
    results['year'] = years
    results.to_csv(f"{resultsName}.csv")

def getResults2 ():
    results = pd.read_csv("poemTests/results2.csv", converters={'ratings': pd.eval})
    results = results.drop(['Unnamed: 0'], axis=1)
    results = results.set_index([[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24]])
    print("results2:", results)
    return results

def getResults3 ():
    results = pd.read_csv("poemTests/results3.csv", converters={'ratings': pd.eval})
    results = results.drop(['Unnamed: 0'], axis=1)
    results = results.set_index([[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24]])
    print("results3:", results)
    return results

# Not updated for new results structure.
# def printAvgRatings(results):
#     print('Average Republican President Rating:', mean(results['ratings']))
#     print('Average Democratic President Rating:', mean(results['ratings']))













#
