from pydantic import BaseModel

class SalesChannelBase(BaseModel):
    name: str

class SalesChannelCreate(SalesChannelBase):
    pass

class SalesChannelResponse(SalesChannelBase):
    id: int

    class Config:
        orm_mode = True