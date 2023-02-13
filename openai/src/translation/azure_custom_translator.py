import requests, uuid, json, os

if "AZURE_TRANSLATOR_KEY" not in os.environ or "AZURE_TRANSLATOR_CATEGORY" not in os.environ:
    raise Exception("Please set AZURE_TRANSLATOR_KEY and AZURE_TRANSLATOR_CATEGORY environment variable")

key = os.getenv("AZURE_TRANSLATOR_KEY")
category = os.getenv("AZURE_TRANSLATOR_CATEGORY")
endpoint = "https://api.cognitive.microsofttranslator.com"
path = '/translate'
location = "westeurope"
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['cs'],
    'category': category
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

input_file = "../../datasets/translations/music_EN.txt"
# Read text from input_file
with open(input_file, 'r') as f:
    text = f.read()

# You can pass more than one object in body.
body = [{
    'text': text
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(response[0]['translations'][0]['text'])