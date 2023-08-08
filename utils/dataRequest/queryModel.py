import openai
import json
import requests
import time
import tqdm

from utils.dataRequest.config import API_KEY

openai.organization = "org-qVlLsaDvMsy8tNQQbRWTyTfX"
openai.api_key = API_KEY
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
        "Authorization": f"Bearer {API_KEY}",
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
