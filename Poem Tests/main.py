import pandas as pd
import os
import openai
# import json
# import requests
# import time
import tqdm
from statistics import mean

import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
rng = np.random.default_rng(19680801)
print("Finished Out Imports.")

#from analysis import *
#from generator import *
#from analysis import sentimentLook
from graphing import hist_avgline_redblue
from graphing import boxplot_redblue
from graphing import scatterplot_redblue
print("Finished In Imports.")

president_dict = {'name' : ['Joe Biden', 'Donald Trump', 'Barack Obama', 'George W. Bush', 'Bill Clinton', 'George H. W. Bush', 'Ronald Reagan', 'Jimmy Carter', 'Gerald Ford', 'Richard Nixon', 'Lyndon B. Johnson', 'John F. Kennedy', 'Dwight D. Eisenhower', 'Harry S. Truman', 'Franklin D. Roosevelt', 'Herbert Hoover', 'Calvin Coolidge', 'Warren G. Harding', 'Woodrow Wilson', 'William Howard Taft', 'Theodore Roosevelt', 'William McKinley', 'Grover Cleveland'],
                  'party': ['D','R','D','R','D','R','R','D','R','R','D','D','R','D','D','R','R','R','D','R','R','R','D'],
                  'num'  : [46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24],
                  'year' : [
    1893,  # Grover Cleveland
    1897,  # William McKinley
    1901,  # Theodore Roosevelt
    1909,  # William Howard Taft
    1913,  # Woodrow Wilson
    1921,  # Warren G. Harding
    1923,  # Calvin Coolidge
    1929,  # Herbert Hoover
    1933,  # Franklin D. Roosevelt
    1945,  # Harry S. Truman
    1953,  # Dwight D. Eisenhower
    1961,  # John F. Kennedy
    1963,  # Lyndon B. Johnson
    1969,  # Richard Nixon
    1974,  # Gerald Ford
    1977,  # Jimmy Carter
    1981,  # Ronald Reagan
    1989,  # George H. W. Bush
    1993,  # Bill Clinton
    2001,  # George W. Bush
    2009,  # Barack Obama
    2017,  # Donald Trump
    2021
]
                  }

president_df = pd.DataFrame(president_dict,index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])

# for president_name in tqdm.tqdm(president_df['name'][1:],desc='Presidents'):
#   poems = generatePoems(president_name, poemcount = 100)
#   storePoems(poems,president_name)


# results = pd.DataFrame(sentimentLook(), index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])
# results.to_csv("results2.csv")
# print(results)


# results = pd.read_csv("./results2.csv")
# results = results.set_index([[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24]])
# results = results.drop(['Unnamed: 0'], axis=1)
# results['party'] = president_df['party']
# years = president_dict['year'].copy()
# years.reverse()
# results['year'] = years
# results.to_csv("results2.csv")
# raise ValueError('end')



results = pd.read_csv("./results2.csv", converters={'ratings': pd.eval})

results = results.drop(['Unnamed: 0'], axis=1)
results = results.set_index([[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24]])
print(results)


# print(results)
republicans = results.loc[results['party'] == 'R']
#republicans = republicans.loc[republicans['name'] != 'Warren G. Harding']
democrats = results.loc[results['party'] == 'D']

# repRatings = republicans['ratings']
# demRatings = democrats['ratings']
# print('Average Republican President Rating:', mean(republicans['ratings']))
# print('Average Democratic President Rating:', mean(democrats['ratings']))


#hist_avgline_redblue(results)
boxplot_redblue(results)
#scatterplot_redblue(results)












#
