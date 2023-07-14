import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def binRange(start,stop,step):
    returnList = []
    for i in range(int(1+((stop-start)/step))):
        returnList.append(round((i+start)*step,5))
    return returnList


def hist_avgline_redblue(results):
    inc = 0.025
    bins = binRange(0, 1, inc )
    binsoffset = binRange(0+inc/2, 1+inc/2, inc )



    sns.set(style="ticks")
    sns.set_style("darkgrid")

    # Create a sample DataFrame with embedded lists
    df = results.copy()
    #reduce poems graphed for republicans so there is even data quantity
    df.loc[df['party'] == 'R', 'ratings'] = df.loc[df['party'] == 'R', 'ratings'].apply(lambda lst: lst[:77])

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



def boxplot_redblue(results):
    # Set seaborn style
    sns.set(style="ticks")
    sns.set_style("darkgrid")

    # Create a figure and axis for the box plots
    fig, ax = plt.subplots(figsize=(10, 6))

    # Initialize lists to store boxplot statistics and positions for each party
    boxplot_stats_dem = []
    boxplot_stats_rep = []
    positions_dem = []
    positions_rep = []
    ult_avg_rating_rep = []
    ult_avg_rating_dem = []

    # Iterate over each set of ratings
    for i, row in results.iterrows():
        year = row['year']
        ratings = row['ratings']
        party = row['party']

        # Calculate the average rating for the current party
        avg_rating = sum(ratings) / len(ratings)

        # Append ratings and positions to the corresponding lists based on the party
        if party == 'D':
            boxplot_stats_dem.append(ratings)
            positions_dem.append(year)
        elif party == 'R':
            boxplot_stats_rep.append(ratings)
            positions_rep.append(year)


        if party == 'D':
            ult_avg_rating_dem.append(avg_rating)

        elif party == 'R':
            ult_avg_rating_rep.append(avg_rating)


    ax.axhline(y=(sum(ult_avg_rating_dem) / len(ult_avg_rating_dem)), color='blue', linestyle='dashed', label='Average Rating (D)', alpha=0.7)
    ax.axhline(y=(sum(ult_avg_rating_rep) / len(ult_avg_rating_rep)), color='red', linestyle='dashed', label='Average Rating (R)', alpha=0.7)

    # Create the boxplots for Democratic and Republican ratings
    ax.boxplot(boxplot_stats_dem, positions=positions_dem, widths=1.8, patch_artist=True, boxprops=dict(facecolor='blue'))
    ax.boxplot(boxplot_stats_rep, positions=positions_rep, widths=1.8, patch_artist=True, boxprops=dict(facecolor='red'))

    # Set the x-axis tick positions and labels
    ax.set_xticks(results['year'])
    ax.set_xticklabels(results['year'])

    # Set the labels for the axes
    ax.set_xlabel('Year')
    ax.set_ylabel('Rating')

    # Show the legend
    ax.legend()
    ax.set_xticklabels(results['year'], rotation=60)
    # Show the plot
    plt.show()

def scatterplot_redblue(results):
    # Create a sample DataFrame with embedded lists
    df = results

    # Expand the DataFrame to have a row for each president's rating
    expanded_df = df.explode('ratings')

    # Set the color palette for the parties
    party_colors = {'D': 'blue', 'R': 'red'}
    sns.set_palette(party_colors.values())

    # Create the plot using Seaborn
    sns.scatterplot(data=expanded_df, x='year', y='ratings', hue='party', s=100)

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('President Rating')
    plt.title('President Ratings by Year')

    # Display the plot
    plt.show()

















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
