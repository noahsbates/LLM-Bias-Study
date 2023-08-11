from utils.dataRequest.queryModel import modelRequester
from utils.dataRequest.config import API_KEYS 

queryGPT_3_5_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEYS['chatGPT_3_5']}",
    }
def queryGPT_3_5_payload_packager(message):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7,
    }
    return payload
def queryGPT_3_5_json_finder(inp):
    return inp["choices"][0]["message"]["content"]
queryGPT_3_5 = modelRequester("gpt-3.5-turbo", "https://api.openai.com/v1/chat/completions",queryGPT_3_5_headers,queryGPT_3_5_payload_packager,queryGPT_3_5_json_finder)