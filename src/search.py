import re

from config import settings
from elastic import es
from nosql.storage.storage import CacheStorage
from schemas.message import MessageSchema
from faststream import Depends

from schemas.search_result import SearchResultSchema


class SearchService:
    def __init__(self, cache_storage: CacheStorage = Depends(CacheStorage)):
        self._es = es
        self._cache_storage = cache_storage

    async def search(self, msg: MessageSchema):
        result = await es.search(
            index=settings().ELASTIC_PDF_INDEX,
            query={"match": {"content": msg.query}},
            highlight={"fields": {"content": {}}},
        )

        hits = result["hits"]["hits"]

        search_results: list[SearchResultSchema] = []

        for hit in hits:
            file_id = int(hit["_source"]["file_id"])
            score = float(hit["_score"])

            highlight_list = hit.get("highlight", {}).get("content", [])

            if highlight_list:
                snippet = self.__extract_snippet(highlight_list[0])
            else:
                snippet = ""

            search_results.append(
                SearchResultSchema(
                    query=msg.query, file_id=file_id, snippet=snippet, score=score
                )
            )

        await self._cache_storage.create_search_result(
            uuid=msg.uuid, results=search_results
        )

    def __extract_snippet(self, highlight: str, window: int = 20) -> str:
        clean_text = re.sub(r"</?em>", "", highlight)
        words = clean_text.split()
        center = len(words) // 2

        start = max(0, center - window)
        end = min(len(words), center + window)

        return " ".join(words[start:end])
