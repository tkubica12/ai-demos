import os
import openai
import csv
import json
import pandas as pd

openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_API_URL")
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Exit if the environment variables are not set
if "OPENAI_API_URL" not in os.environ or "OPENAI_API_KEY" not in os.environ:
    raise Exception("Please set OPENAI_API_KEY and OPENAI_API_URL environment variable")

# Input folder
input_folder = "../../datasets/press_releases_ministry_cz"

# Read content of all files in the input folder into Pandas DataFrame
df = pd.DataFrame()
for file in os.listdir(input_folder):
    with open(os.path.join(input_folder, file), 'r') as f:
        content = f.read()
        df = df.append({"file": file, "content": content}, ignore_index=True)

# Define lambda function calling OpenAI API and returning parsed information
def openai_parse(text, file):
    print(f"Processing {file}")
    prompt = text + "\n\nVytáhni následující informace ve formátu JSON:\n\nHlavní předmět textu as topic, osoby as persons, instituce as institutions, abstract o délce 100 znaků.\n\n"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=500,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    
    # Try parse response as JSON
    try:
        data = json.loads(response.choices[0].text)
    except:
        print("Not valid JSON")
    return data['topic'], data['persons'], data['institutions'], data['abstract']

# Use OpenAI to parse content
df['topic'], df['persons'], df['institutions'], df['abstract'] = zip(*df.apply(lambda x: openai_parse(x["content"], x["file"]), axis=1))

# Write output files
print("Writing output files")
df.to_json("output_full.json", orient="records")
df.drop(['content'], axis = 1, inplace = False).to_json("output.json", orient="records")
df.to_csv("output.csv", index=True)