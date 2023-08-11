from utils.dataRequest.queryModel import modelRequester
from utils.dataRequest.config import API_KEYS 

queryGPT_4_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEYS['chatGPT_4']}",
    }
def queryGPT_4_payload_packager(message):
    payload = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7,
    }
    return payload
def queryGPT_4_json_finder(inp):
    return inp["choices"][0]["message"]["content"]
queryGPT_4 = modelRequester("gpt-4", "https://api.openai.com/v1/chat/completions",queryGPT_4_headers,queryGPT_4_payload_packager,queryGPT_4_json_finder)