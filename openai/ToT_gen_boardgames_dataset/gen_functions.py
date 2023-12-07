from openai import AzureOpenAI
from typing import List
import json
import tiktoken

def gen_outline(client: AzureOpenAI, deployment_name):
    """
    This function generates an outline for a board game description.
    It uses the AzureOpenAI client to create a list of chapters for the description.
    The output is a JSON array where each chapter is a string in the array.

    Args:
        client (AzureOpenAI): The AzureOpenAI client.
        deployment_name (str): The name of the deployment.

    Returns:
        output (List[str]): The list of chapters.
        num_tokens (int): The number of tokens in the response message.
    """
    system_prompt = """Tvým úkolem je připravit univerzální seznam kapitol pro popis dobrodružné deskové hry. 
Výstup vrať jako JSON tak, aby každá kapitola představovala jeden řetězec v poli řetězců. Text bude vždy v češtině.
Například: ["První kapitola", "Druhá kapitola"]"""
    message_text = [{"role":"system","content":system_prompt}]
    response = client.chat.completions.create(
        model=deployment_name,
        messages = message_text,
        temperature=0.7,
        max_tokens=1000,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    response_message = response.choices[0].message.content

    try:
        output = json.loads(response_message)
        encoding = tiktoken.encoding_for_model('gpt-4')
        num_tokens = len(encoding.encode(response_message))
        return output, num_tokens
    except Exception as e:
        raise Exception("Model did not return valid JSON: " + str(e))

def gen_basics(client: AzureOpenAI, deployment_name):
    """
    This function generates a list of board game names and their descriptions.
    It uses the AzureOpenAI client to create a list of board game names and their three-sentence descriptions.
    The output is a JSON array where each element is an object with "name" and "description" keys.

    Args:
        client (AzureOpenAI): The AzureOpenAI client.
        deployment_name (str): The name of the deployment.

    Returns:
        output (List[dict]): The list of board game names and descriptions.
        num_tokens (int): The number of tokens in the response message.
    """
    system_prompt = """Tvým úkolem je připravit minimálně 30 názvů dobrodružné deskové hry a její popis ve třech větách. 
Výstup vrať jako JSON tak, aby název byl v klíči "name" a popis v klíči "description". Název a popis vždy v češtině.
Například: [{"name": "Název hry", "description": "Popis hry"}, {"name": "Název hry2", "description": "Popis hry2"}]"""

    message_text = [{"role":"system","content":system_prompt}]
    response = client.chat.completions.create(
        model=deployment_name,
        messages = message_text,
        temperature=0.7,
        max_tokens=7000,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    response_message = response.choices[0].message.content

    try:
        output = json.loads(response_message)
        encoding = tiktoken.encoding_for_model('gpt-4')
        num_tokens = len(encoding.encode(response_message))
        return output, num_tokens
    except Exception as e:
        raise Exception("Model did not return valid JSON: " + str(e))

def gen_chapter(client: AzureOpenAI, deployment_name, game_name, game_description, chapter_name):
    """
    This function generates text for a specific chapter of a game guide.
    It uses the AzureOpenAI client to generate the text based on the provided game name, game description, and chapter name.
    The output is a string representing the text of the chapter.

    Args:
        client (AzureOpenAI): The AzureOpenAI client.
        deployment_name (str): The name of the deployment.
        game_name (str): The name of the board game.
        game_description (str): The description of the board game.
        chapter_name (str): The name of the chapter.

    Returns:
        output (str): Text of the chapter.
        num_tokens (int): The number of tokens in the response message.
    """
    system_prompt = f"""Tvým úkolem je vytvořit text do kapitoly {chapter_name} návodu k dobrodružné deskové hře {game_name}. Popis této hry: {game_description}.
Drž se uvedeného názvu kapitoly, hry a jejího popisu, nevytvářej žádné další kapitoly nebo hry, jen ty zadané. Text vždy v češtině."""

    message_text = [{"role":"system","content":system_prompt}]
    response = client.chat.completions.create(
        model=deployment_name,
        messages = message_text,
        temperature=0.7,
        max_tokens=7000,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    response_message = response.choices[0].message.content

    output = response_message
    encoding = tiktoken.encoding_for_model('gpt-4')
    num_tokens = len(encoding.encode(response_message))
    return output, num_tokens