from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from enum import Enum


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


class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8)  
    job_title: JobTitle  
    department_name: DepartmentName 
    company: Optional[str] = None  
    is_active: bool = True


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    job_title: Optional[JobTitle] = None  
    department_name: Optional[DepartmentName] = None 
    company: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True 


class UserLogin(BaseModel):
    email: EmailStr
    password: constr(min_length=8)