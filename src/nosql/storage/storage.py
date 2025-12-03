import json
from typing import Sequence

from faststream import Depends
from redis.asyncio import Redis

from nosql.storage.client import get_redis
from schemas.search_result import SearchResultSchema


class CacheStorage:
    def __init__(self, redis: Redis = Depends(get_redis)):
        self._redis = redis

    async def create_search_result(
        self, uuid: str, results: Sequence[SearchResultSchema]
    ) -> None:
        await self._redis.set(
            name=uuid, value=json.dumps([r.model_dump() for r in results]), ex=10 * 60
        )
