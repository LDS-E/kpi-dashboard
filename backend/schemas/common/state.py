from pydantic import BaseModel
from typing import Optional

class StateBase(BaseModel):
    name: str
    country_id: int

class StateCreate(StateBase):
    pass

class StateResponse(StateBase):
    id: int

    class Config:
        from_attributes = True
