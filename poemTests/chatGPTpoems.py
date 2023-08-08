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

from utils.basicData.presidentData import president_dict

president_df = pd.DataFrame(president_dict,index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])

######## Generating The Poems ########

def createPoems():
    for president_name in tqdm.tqdm(president_df['name'][1:],desc='Presidents Poems'):
      poems = generatePoems(name = president_name, message = "Write a 8 line poem about ", poemcount = 100)
      poems.to_csv(f"poemTests/politicalPoems/{president_name}.csv")

######## Different Analysis Algorithms (From HuggingFace) ########

def calculateResults2 ():
    results = pd.DataFrame(nlptownSentiment("poemTests/politicalPoems"), index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])
    saveResults(results,"results2")

def calculateResults3 ():
    results = pd.DataFrame(cardiffnlpSentiment("poemTests/politicalPoems"), index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])
    saveResults(results,"results3")

######## Data Processing ########

#Not to be used outside of this file
def saveResults (results,resultsName):
    results = results.set_index([[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24]])
    #results = results.drop(['Unnamed: 0'], axis=1)
    results['party'] = president_df['party']
    years = president_dict['year'].copy()
    years.reverse()
    results['year'] = years
    results.to_csv(f"{resultsName}.csv")

######## Data Retrieval  ########

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













#
