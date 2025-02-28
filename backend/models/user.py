from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum

from ..database import Base

class JobTitle(Enum):
    HEAD = "Head"
    MANAGER = "Manager"
    SALES_REP = "Sales Rep"
    ANALYST = "Analyst"

class DepartmentName(Enum):
    MARKETING = "Marketing"
    SALES = "Sales"
    REVENUE = "Revenue"
    FINANCE = "Finance"
    PRODUCT = "Product"
    ENGINEERING = "Engineering"
    HR = "Human Resources"
    OPERATIONS = "Operations"
    DATA = "Data"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    job_title = Column(String)  
    department_name = Column(String)  
    company = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)