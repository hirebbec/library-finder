from schemas.base import BaseSchema


class MessageSchema(BaseSchema):
    uuid: str
    query: str
