
from pydantic import BaseModel

class MdtrAuditBase(BaseModel):
    audit_month: str  
    country: str  
    state: str  
    city: str  
    brick_code: str  
    sales_channel: str  
    sales_subchannel: str  
    company_name: str  
    pdv_code: str  
    product_name: str  
    sku: str  
    units_sold: int  

    class Config:
        orm_mode = True  

class MdtrAuditCreate(MdtrAuditBase):
    pass 

class MdtrAudit(MdtrAuditBase):
    id: int  

    class Config:
        orm_mode = True
