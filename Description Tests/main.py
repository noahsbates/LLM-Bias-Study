print("Starting Vital Imports...")
import pandas as pd
import os
import openai
# import json
# import requests
# import time
import tqdm
from statistics import mean
import torch
#print(torch.version.cuda)
print("CUDA:", torch.cuda.is_available())
print("Finished Vital Imports.")

#from analysis import *
#from generator import *
print("Importing analysis...")
from analysis import meanSentimentLook
print("Importing generator...")
from generator import generateDescriptions
from generator import storeDescriptions
print("Finished Internal Imports.")

president_dict = {'name' : ['Joe Biden', 'Donald Trump', 'Barack Obama', 'George W. Bush', 'Bill Clinton', 'George H. W. Bush', 'Ronald Reagan', 'Jimmy Carter', 'Gerald Ford', 'Richard Nixon', 'Lyndon B. Johnson', 'John F. Kennedy', 'Dwight D. Eisenhower', 'Harry S. Truman', 'Franklin D. Roosevelt', 'Herbert Hoover', 'Calvin Coolidge', 'Warren G. Harding', 'Woodrow Wilson', 'William Howard Taft', 'Theodore Roosevelt', 'William McKinley', 'Grover Cleveland'],
                  'party': ['D','R','D','R','D','R','R','D','R','R','D','D','R','D','D','R','R','R','D','R','R','R','D'],
                  'num'  : [46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24]
                  }

president_df = pd.DataFrame(president_dict,index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])
#
# #print(generateDescriptions('Donald Trump')['output'][0])
#
# for president_name in tqdm.tqdm(president_df['name'][22:],desc='Presidents'):
#   descriptions = generateDescriptions(president_name, descriptioncount = 100)
#   storeDescriptions(descriptions,president_name)

# results = pd.DataFrame(meanSentimentLook(), index=[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24])
# results.sort_values(by=['ratings'])
# print(results)
# #results.to_csv("results1.csv")
#
# results = results.set_index([[46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24]])
# results.to_csv("results1.csv")
# #results = results.drop(['Unnamed: 0'], axis=1)
# results.to_csv("results1.csv")
# results['party'] = president_df['party']
# #
# results.to_csv("results1.csv")
# print (results)
results = pd.read_csv("./results1.csv")

# print(results)
republicans = results.loc[results['party'] == 'R']
#republicans = republicans.loc[republicans['name'] != 'Warren G. Harding']
democrats = results.loc[results['party'] == 'D']

print('Average Republican President Rating:', mean(republicans['ratings']))
print('Average Democratic President Rating:', mean(democrats['ratings']))
