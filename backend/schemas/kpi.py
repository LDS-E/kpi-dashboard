from pydantic import BaseModel, constr, condecimal, Field
from typing import Optional, Union
from enum import Enum
from datetime import datetime

class DataType(str, Enum):
    NUMBER = "number"
    TEXT = "text"
    DATE = "date"


class KPICreate(BaseModel):
    name: constr(min_length=3)
    data_type: DataType
    data: Union[condecimal(decimal_places=2), str, datetime]  
    unit: Optional[str] = None
    source: Optional[str] = None
    category: Optional[str] = None
    description: Optional[constr(max_length=255)] = None

class KPIResponse(BaseModel):
    id: int
    name: str
    data_type: DataType
    data: Union[float, str, datetime]
    unit: Optional[str] = None
    source: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    timestamp: datetime

    class Config:
        from_attributes = True