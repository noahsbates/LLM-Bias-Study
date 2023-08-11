import tqdm
import pandas as pd
import os
import time

#### IMPORTANT:
# Because I started with mainly poems in mind, in this file I refer to multiple types of files such as both descriptions and poems as just 'poems' or 'poem'

class poemCompiler():
    def __init__(self, queryModel):
        self.queryModel = queryModel
        self.name = queryModel.model
    
    def compilePoems(self, message, poemcount = 10):
        output_poems = []
        for i in tqdm.tqdm(range(poemcount), desc=f"Generating set of {poemcount} with {self.name}: [{message}]"):
            out = self.queryModel.ask(message)
            output_poems.append(out)
        return pd.DataFrame(output_poems, columns=["output"])

def loadPoems(path,name):
    return pd.read_csv(f"{path}/{name}.csv")

def savePoems(path,name):
    pass
