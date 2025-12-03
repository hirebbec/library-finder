from schemas.base import BaseSchema


class SearchResultSchema(BaseSchema):
    query: str
    file_id: int
    snippet: str
    score: float
