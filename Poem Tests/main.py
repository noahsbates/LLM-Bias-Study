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



def binRange(start,stop,step):
    returnList = []
    for i in range(int(1+((stop-start)/step))):
        returnList.append(round((i+start)*step,5))
    return returnList


inc = 0.025
bins = binRange(0, 1, inc )
binsoffset = binRange(0+inc/2, 1+inc/2, inc )


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")
sns.set_style("darkgrid")

# Create a sample DataFrame with embedded lists
df = results
for i in range(24,47):
    if df['party'][i] == 'R':
        df['ratings'][i] = df['ratings'][i][:78]

# Expand the DataFrame to have a row for each president's rating
expanded_df = df.explode('ratings')

# Set the color palette for the parties
party_colors = {'D': 'blue', 'R': 'red'}
sns.set_palette(party_colors.values())

# Create separate DataFrames for each party
party_d = expanded_df[expanded_df['party'] == 'D']
party_r = expanded_df[expanded_df['party'] == 'R']
print(party_r['name'].value_counts())
print('Length D:', len(party_d))
print('Length R:', len(party_r))

# Plot the histograms
sns.histplot(data=party_d, x='ratings', bins = bins, color='blue', alpha=0.5, label='Democrats')
sns.histplot(data=party_r, x='ratings', bins = bins, color='red', alpha=0.5, label='Republicans')


# Calculate average ratings for Republicans and Democrats
avg_rating_d = party_d['ratings'].astype(float).mean()
avg_rating_r = party_r['ratings'].astype(float).mean()

# Add vertical lines for the average ratings
plt.axvline(x=avg_rating_d, color='blue', linestyle='--', label='Avg. Democrats')
plt.axvline(x=avg_rating_r, color='red', linestyle='--', label='Avg. Republicans')


# Set labels and title
plt.xlabel('President Rating')
plt.ylabel('Count')
plt.title('President Ratings by Party')

# Display the plot with a legend
plt.legend()

# Show the plot
plt.show()




# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # Create a sample DataFrame with embedded lists
# df = results
#
# # Expand the DataFrame to have a row for each president's rating
# expanded_df = df.explode('ratings')
#
# # Set the color palette for the parties
# party_colors = {'D': 'blue', 'R': 'red'}
# sns.set_palette(party_colors.values())
#
# # Create the plot using Seaborn
# sns.scatterplot(data=expanded_df, x='year', y='ratings', hue='party', s=100)
#
# # Set labels and title
# plt.xlabel('Year')
# plt.ylabel('President Rating')
# plt.title('President Ratings by Year')
#
# # Display the plot
# plt.show()





# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # Set seaborn style
# sns.set(style="whitegrid")
#
# # Create a figure and axis for the box plots
# fig, ax = plt.subplots(figsize=(10, 6))
#
# # Initialize lists to store boxplot statistics and positions for each party
# boxplot_stats_dem = []
# boxplot_stats_rep = []
# positions_dem = []
# positions_rep = []
# ult_avg_rating_rep = []
# ult_avg_rating_dem = []
#
# # Iterate over each set of ratings
# for i, row in results.iterrows():
#     year = row['year']
#     ratings = row['ratings']
#     party = row['party']
#
#     # Calculate the average rating for the current party
#     avg_rating = sum(ratings) / len(ratings)
#
#     # Append ratings and positions to the corresponding lists based on the party
#     if party == 'D':
#         boxplot_stats_dem.append(ratings)
#         positions_dem.append(year)
#     elif party == 'R':
#         boxplot_stats_rep.append(ratings)
#         positions_rep.append(year)
#
#
#     if party == 'D':
#         ult_avg_rating_dem.append(avg_rating)
#
#     elif party == 'R':
#         ult_avg_rating_rep.append(avg_rating)
#
#
# ax.axhline(y=(sum(ult_avg_rating_dem) / len(ult_avg_rating_dem)), color='blue', linestyle='dashed', label='Average Rating (D)', alpha=0.7)
# ax.axhline(y=(sum(ult_avg_rating_rep) / len(ult_avg_rating_rep)), color='red', linestyle='dashed', label='Average Rating (R)', alpha=0.7)
#
# # Create the boxplots for Democratic and Republican ratings
# ax.boxplot(boxplot_stats_dem, positions=positions_dem, widths=0.4, patch_artist=True, boxprops=dict(facecolor='blue'))
# ax.boxplot(boxplot_stats_rep, positions=positions_rep, widths=0.4, patch_artist=True, boxprops=dict(facecolor='red'))
#
# # Set the x-axis tick positions and labels
# ax.set_xticks(results['year'])
# ax.set_xticklabels(results['year'])
#
# # Set the labels for the axes
# ax.set_xlabel('Year')
# ax.set_ylabel('Rating')
#
# # Show the legend
# ax.legend()
#
# plt.xticks([1893, 1905, 1917, 1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025])
# # Show the plot
# plt.show()











# def binRange(start,stop,step):
#     returnList = []
#     for i in range(int(1+((stop-start)/step))):
#         returnList.append(round((i+start)*step,5))
#     return returnList
#
#
# inc = 0.1
# bins = binRange(0, 1, inc )
# binsoffset = binRange(0+inc/2, 1+inc/2, inc )
# print('Bins:',bins)

# fig, axs = plt.subplots(2,figsize=(6, 6))
#
# def makeaxs(i,data,name='unnamed'):
#     if i == 0: color = "lightcoral"
#     else: color = "skyblue"
#
#     axs[i].hist(data,
#     #range = [0,6],
#     bins=bins,
#     edgecolor='black',
#     ec="k",
#     align='mid',
#     #legend=name,
#     #cumulative = True
#     color = color
#     )
#
#     axs[i].locator_params(axis='y', integer=True)
#     axs[i].set_ylim(0, 8)
#
# makeaxs(0,repRatings,"Republican President Ratings By ChatGPT")
# makeaxs(1,demRatings,"Democratic President Ratings By ChatGPT")

# X =
# Y1 = repRatings
# Y2 = demRatings
#
# fig, ax = plt.subplots()
# ax.plot(X,Y1,'o')
# ax.plot(X,Y2,'x')
# plt.show()

#plt.tight_layout()
#plt.axis('equal')
# plt.show()













#
