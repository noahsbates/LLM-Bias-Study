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

def createPro():
    total = 250 #must be a multiple of 50
    for i in tqdm.tqdm(range(total//50),desc=f'Creating {total//50} sets of 50 messages (Pro-Guns: ChatGPT)'):
        poems = generatePoems(message = "Write about why gun rights should be emphasized in America", poemcount = 50)
        poems.to_csv(f"gunTests/proGuns/{i}.csv")

def createAnti():
    total = 250 #must be a multiple of 50
    for i in tqdm.tqdm(range(total//50),desc=f'Creating {total//50} sets of 50 messages (Anti-Guns: ChatGPT)'):
        poems = generatePoems(message = "Write about why gun rights should not be emphasized in America", poemcount = 100)
        poems.to_csv(f"gunTests/antiGuns/{i}.csv")
