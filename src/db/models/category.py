from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import Mapped
from db.base import Base

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = Column(Integer, primary_key=True)
    user_id: Mapped[int] = Column(Integer, ForeignKey("users.id"))
    name: Mapped[str] = Column(String, unique=True)