from pydantic import BaseModel

class CityBase(BaseModel):
    name: str
    state_id: int

class CityCreate(CityBase):
    pass

class CityResponse(CityBase):
    id: int

    class Config:
        from_attributes = True
