from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base

class SalesSubChannel(Base):
    __tablename__ = "sales_sub_channels"

    id = Column(Integer, primary_key=True, index=True)
    sales_subchannel_name = Column(String)
    sales_channel_id = Column(Integer, ForeignKey("sales_channels.id"))