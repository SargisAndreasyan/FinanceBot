from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped
from db.base import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = Column(Integer, primary_key=True)
    t_id: Mapped[int]