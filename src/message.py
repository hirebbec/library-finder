from pydantic import BaseModel


class MessageSchema(BaseModel):
    uuid: str
    query: str
