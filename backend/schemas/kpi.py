from pydantic import BaseModel
from typing import Optional

class KPIBase(BaseModel):
    name: str
    value: float
    description: Optional[str] = None

class KPICreate(KPIBase):
    pass

class KPIResponse(KPIBase):
    id: int

    class Config:
        from_attributes = True