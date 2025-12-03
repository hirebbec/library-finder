import asyncio

from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue

from config import settings
from schemas.message import MessageSchema
from search import SearchService
from faststream import Depends

broker = RabbitBroker(url=settings().rabbitmq_dsn)

app = FastStream(broker)


@broker.subscriber(RabbitQueue(name=settings().RABBITMQ_SEARCH_QUEUE))
async def handle(
    msg: MessageSchema, search_service: SearchService = Depends(SearchService)
):
    await search_service.search(msg=msg)


if __name__ == "__main__":
    asyncio.run(app.run())
