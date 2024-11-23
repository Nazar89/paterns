from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class CarBase(BaseModel):
    model: str
    manufacturer: str
    description: Optional[str]
    year: Optional[int]

class CarCreate(CarBase):
    pass

class CarUpdate(BaseModel):
    model: Optional[str] = None
    manufacturer: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None

class CarRead(CarBase):
    id: UUID

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
