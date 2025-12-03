import functools

from redis.asyncio import Redis

from config import settings


@functools.lru_cache
def get_redis() -> Redis:
    return Redis.from_url(settings().redis_dsn)
