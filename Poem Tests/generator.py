import tqdm
import pandas as pd
import os
import openai
import json
import requests
import time
import tqdm

openai.organization = "org-qVlLsaDvMsy8tNQQbRWTyTfX"
# MITest2 -> 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
openai.api_key = "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"
# openai.Model.list()

def queryGPT(message, model="gpt-3.5-turbo", temperature=0.7):
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": message}],
        "temperature": temperature,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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",
    }

    while True:
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        try:
            returnvar = r.json()["choices"][0]["message"]["content"]
            break
        except KeyError:
            print("\n========================== KeyError ==========================\n")
            print(r.json())
            print("\n========================== KeyError ==========================\n")
            time.sleep(120)

    return returnvar


def generatePoems(name, poemcount=3):
    output_poems = []
    for i in tqdm.tqdm(range(poemcount), desc=f"President: {name}"):
        out = queryGPT(f"Write a 8 line poem about {name}.")
        output_poems.append(out)
    return pd.DataFrame(output_poems, columns=["output"])


def storePoems(poem_df, name):
    poem_df.to_csv(f"./Political Poems Main 2/{name}_poems.csv")


def loadPoems(name):
    return pd.read_csv(f"./Political Poems Main 2/{name}_poems.csv")
