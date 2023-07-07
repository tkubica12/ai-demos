# Azure OpenAI demo
Make sure Python libraries are installed and put your API key and endpoint into environmental variables.

```bash
export OPENAI_API_KEY=yourkey
export OPENAI_API_URL=https://yourendpoint

pip install openai
```

## Text summarization
In [src/summarization](./src/summarization/) folder there is file text.txt - put you input there and then run the script ```python generate.py``` which will output results into output.csv file.

## Text parsing
See example data and code in [src/parsing](./src/parsing/) folder.

## Embeddings (similarity search)
Example with movie descriptions: [notebooks/movies.ipynb](./notebooks/movies.ipynb