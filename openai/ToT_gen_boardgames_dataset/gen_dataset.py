import os
from openai import AzureOpenAI
import time
import unidecode
from typing import List
import json
import unidecode

from gen_functions import gen_outline, gen_basics, gen_chapter

# Set OpenAI API credentials
client = AzureOpenAI(
  api_key = os.environ['AZURE_OPENAI_API_KEY'],
  azure_endpoint = os.environ['OPENAI_URL'],
  api_version = "2023-09-01-preview",
)
deployment_name = os.getenv("DEPLOYMENT_NAME")

# Sleep time between requests - workaround for API rate limits
sleep_time = 5

# Count total tokens
total_tokens = 0

# Base folder for outputs
base_folder = "games"
os.makedirs(base_folder, exist_ok=True)

# Generate boardgames guide outline
print("Generating boardgames guide outline")
outline, num_tokens = gen_outline(client=client, deployment_name=deployment_name)
total_tokens += num_tokens
print(f"Outline generated with {num_tokens} tokens")

# Generate boardgames names and base descriptions
print("Generating boardgames names and descriptions")
games, num_tokens = gen_basics(client=client, deployment_name=deployment_name)
total_tokens += num_tokens
print(f"Names and descriptions generated with {num_tokens} tokens")

# Generate boardgames chapters
for game in games:
    print(f"Total tokens so far: {total_tokens}")
    print("--------------------------------------")
    print(f"Generating chapters for {game['name']}")
    for chapter in outline:
        print(f"...Generating chapter {chapter}")
        text, num_tokens = gen_chapter(client=client, deployment_name=deployment_name, game_name=game['name'], game_description=game['description'], chapter_name=chapter)
        total_tokens += num_tokens
        print(f"......Chapter generated with {num_tokens} tokens")
        file_name = f"{base_folder}/{unidecode.unidecode(game['name']).replace(' ', '_')}_{unidecode.unidecode(chapter).replace(' ', '_')}.txt"
        with open(file_name, "w", encoding='utf-8') as f:
          f.write(f"Nazev hry: {game['name']}\nKapitola: {chapter}\n\n{text}")
        time.sleep(sleep_time)

print("--------------------------------------")
print(f"Total tokens: {total_tokens}")