from config import settings
from elastic import es
from message import MessageSchema


class SearchService:
    def __init__(self):
        self._es = es

    async def search(self, msg: MessageSchema):
        result = await es.search(
            index=settings().ELASTIC_PDF_INDEX,
            query={"match": {"content": msg.query}},
            highlight={"fields": {"content": {}}},
        )

        print(result)
