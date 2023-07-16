import tqdm
import pandas as pd
import os
import time

from utils.dataRequest.queryModel import queryGPT

#### IMPORTANT:
# Because I started with mainly poems in mind, in this file I refer to multiple types of files such as both descriptions and poems as just 'poems' or 'poem'

def generatePoems(name = '', message = "Write a 8 line poem about ",poemcount=3):
    output_poems = []
    for i in tqdm.tqdm(range(poemcount), desc=f"Generating set of {poemcount}: [{name}]"):
        out = queryGPT(f"{message}{name}.")
        output_poems.append(out)
    return pd.DataFrame(output_poems, columns=["output"])

def loadPoems(path,name):
    return pd.read_csv(f"{path}/{name}.csv")
