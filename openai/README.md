# Azure OpenAI demo
Make sure Python libraries are installed and put your API key and endpoint into environmental variables.

```bash
export OPENAI_API_KEY=yourkey
export OPENAI_API_URL=https://yourendpoint

pip install openai
```

## Vector search in Azure comparison
See [vector_databases/vector_databases.ipynb](vector_databases/vector_databases.ipynb) for tests of various options to store and search embeddings in Azure services:
- Terraform code to deploy Azure resources
- Tested solutions:
    - Azure Database for PostgreSQL with pgvector
    - Azure Cosmos DB for Mongo DB vCore
    - Azure Cognitive Search
    - Azure Data Explorer
    - Redis (using RedisSearch - unfortunatelly I cannot test Azure Cache for Redis Enterprise so used container)

## Text summarization
In src/summarization folder there is file text.txt - put you input there and then run the script ```python generate.py``` which will output results into output.csv file.