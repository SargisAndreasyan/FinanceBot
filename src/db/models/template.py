from sqlalchemy import Column, Integer, String
from db.base import Base

class Template(Base):
    __tablename__ = "temp"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)