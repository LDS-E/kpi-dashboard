from pydantic import BaseModel

class SalesSubChannelBase(BaseModel):
    name: str
    sales_channel_id: int

class SalesSubChannelCreate(SalesSubChannelBase):
    pass

class SalesSubChannelResponse(SalesSubChannelBase):
    id: int

    class Config:
        orm_mode = True