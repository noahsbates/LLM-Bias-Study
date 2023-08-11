## Used to remove names and therefore sentiment analysis bias from the system when rating poems and descriptions
import regex as re
import pandas as pd
from utils.basicData.presidentData import president_dict
from utils.dataRequest.generator import loadPoems
import tqdm
#from utils.dataRequest.generator import savePoems


#Get all first and last president names to remove from poems.
presidentNamesComplete = president_dict['name']
presidentNamesSplit = []
for i in presidentNamesComplete:
    firstLast = i.split(' ')
    for eachName in firstLast:
        presidentNamesSplit.append(eachName)

def findRemovePresident(inputPoem):
    nameReplaced = inputPoem
    for i in presidentNamesSplit:
        nameReplaced = nameReplaced.replace(i, "NAME")
    
    presidentReplaced = nameReplaced.replace("NAME NAME NAME NAME", "the president")
    presidentReplaced = presidentReplaced.replace("NAME NAME NAME", "the president")
    presidentReplaced = presidentReplaced.replace("NAME NAME", "the president")
    presidentReplaced = presidentReplaced.replace("NAME", "the president")
    return presidentReplaced

#print(findRemovePresident("Hello I am Joe Biden. I am also Donald Trump. I am the one who is Harry S. Truman"))

def replaceEntireSet(inpath,outpath):
    print('HERE')
    for president_name in tqdm.tqdm(president_dict['name'],desc=f'Removing president names. {inpath} -> {outpath}'):
        presidentDF = loadPoems(inpath,president_name)
        outputDF = presidentDF.copy()
        outputDF['output'] = outputDF['output'].apply(findRemovePresident)

        outputDF.to_csv(f"{outpath}/{president_name}.csv")