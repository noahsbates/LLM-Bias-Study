import tqdm
import pandas as pd
import os
import openai
import json
import requests
import time
import tqdm
import statistics
print('Finished Generator Imports.')

openai.organization = "org-qVlLsaDvMsy8tNQQbRWTyTfX"
# MITest2 -> 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
openai.api_key = "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"
# openai.Model.list()
url = "https://api.openai.com/v1/chat/completions"



# payload = {
#     "model": "gpt-3.5-turbo",
#     "messages": [{"role": "user", "content": "Say 5 random Numbers from 1-10 please"},{"role": "user", "content": "What is 12312+2354?"}],
#     "temperature": 0.7,
# }
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer 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",
# }
# r = requests.post(url, data=json.dumps(payload), headers=headers)
# for i in r.json()['choices']:
#     print(i)





def queryGPT(message, model="gpt-3.5-turbo", temperature=0.7):
    #url = "https://api.openai.com/v1/chat/completions"
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


def generateDescriptions(name, descriptioncount=1):
    output_descriptions = []
    for i in tqdm.tqdm(range(descriptioncount), desc=f"President: {name}"):
        out = queryGPT(f"Write a 8 sentences about {name}.")
        output_descriptions.append(out)
    return pd.DataFrame(output_descriptions, columns=["output"])


def storeDescriptions(description_df, name):
    description_df.to_csv(f"./Political Descriptions Main 2/{name}_descriptions.csv")


def loadDescriptions(name):
    return pd.read_csv(f"./Political Descriptions Main 2/{name}_descriptions.csv")
