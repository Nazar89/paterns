from sqlalchemy import Column, Integer, String, Text, Uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"
    id = Column(Uuid, primary_key=True, nullable=False, index=True)
    model = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    year = Column(Integer, nullable=True)
