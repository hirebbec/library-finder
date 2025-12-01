import asyncio

from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue

from config import settings

broker = RabbitBroker(url=settings().rabbitmq_dsn)

app = FastStream(broker)


@broker.subscriber(RabbitQueue(name=settings().RABBITMQ_SEARCH_QUEUE))
async def handle(msg):
    print(msg)


if __name__ == "__main__":
    asyncio.run(app.run())
