from sqlalchemy.orm import Session
from backend.models.sellout.mdtr.mdtr import MDTR
from backend.schemas.sellout.mdtr import MdtrAuditCreate

def create_mdtr_audit(db: Session, mdtr_data: MdtrAuditCreate):
    
    db_mdtr_audit = MDTR(
        audit_month=mdtr_data.audit_month,
        country=mdtr_data.country,
        state=mdtr_data.state,
        city=mdtr_data.city,
        brick_code=mdtr_data.brick_code,
        sales_channel=mdtr_data.sales_channel,
        sales_subchannel=mdtr_data.sales_subchannel,
        company_name=mdtr_data.company_name,
        pdv_code=mdtr_data.pdv_code,
        product_name=mdtr_data.product_name,
        sku=mdtr_data.sku,
        units_sold=mdtr_data.units_sold
    )
    
    db.add(db_mdtr_audit)  
    db.commit() 
    db.refresh(db_mdtr_audit) 
    return db_mdtr_audit
