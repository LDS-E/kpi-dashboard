from pydantic import BaseModel

class SKUBase(BaseModel):
    product_id: int
    presentation: str

class SKUCreate(SKUBase):
    pass

class SKUResponse(SKUBase):
    id: int

    class Config:
        orm_mode = True