from pydantic import BaseModel
from typing import Optional

class BrickCreate(BaseModel):
    code: str
    city_id: int

class BrickResponse(BaseModel):
    id: int
    code: str
    city_id: int

    class Config:
        orm_mode = True
