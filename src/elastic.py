from elasticsearch import AsyncElasticsearch
from config import settings

es = AsyncElasticsearch(settings().elastic_dsn)
