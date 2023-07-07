## Vector search in Azure comparison
See [vector_databases/vector_databases.ipynb](vector_databases/vector_databases.ipynb) for tests of various options to store and search embeddings in Azure services:
- Terraform code to deploy Azure resources
- Tested solutions:
    - Azure Database for PostgreSQL with pgvector
    - Azure Cosmos DB for Mongo DB vCore
    - Azure Cognitive Search
    - Azure Data Explorer
    - Redis (using RedisSearch - unfortunately I cannot test Azure Cache for Redis Enterprise so used container)