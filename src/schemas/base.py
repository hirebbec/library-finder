from datetime import datetime

from pydantic import BaseModel, ConfigDict

from config import settings


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            datetime: lambda dt: dt.astimezone(tz=settings().TIME_ZONE),
        },
    )
