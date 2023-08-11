import pandas as pd
import os
import openai
import tqdm
from statistics import mean

import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

from utils.sentimentAnalysis.analysis import nlptownSentiment
from utils.sentimentAnalysis.analysis import cardiffnlpSentiment

from utils.dataFilter.removeName import replaceEntireSet

from utils.basicTools import getRelDir

from utils.basicData.presidentData import president_dict

# Poem refers to any query from an LLM
class biasFinder():

    def __init__(self, test_folder_path, model_name, poemComplier, resultsCleanerFunc = None):
            self.president_df = pd.DataFrame(president_dict,index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])
            self.model_name = model_name
            self.test_path = test_folder_path
            self.poemCompiler = poemComplier
            self.resultsCleaner = resultsCleanerFunc

    ######## Generating The Poems ########

    def createPoemSet(self, outputFolder, message, setname, poemcount = 10):
        poems = self.poemCompiler.compilePoems(message, poemcount)
        poems.to_csv(f"{self.test_path}/{outputFolder}/{setname}.csv")

    ######## Different Analysis Algorithms (From HuggingFace) ########
    
    def analyze(self, analyzeFunction, folderToRead, name):
        results = pd.DataFrame(analyzeFunction(f"{self.test_path}/{folderToRead}"))
        results.to_csv(f"{self.test_path}/{name}.csv")

    ######## Data Retrieval  ########

    def getResults (self, resultsFilename):
        results = pd.read_csv(f"{self.test_path}/{resultsFilename}.csv", converters={'ratings': pd.eval})
        if self.resultsCleaner != None:
            results = self.resultsCleaner(results)
        print(f"Data from: {resultsFilename}")
        return results