from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import Mapped

from db import Category, User
from db.base import Base

class Expense(Base):
    __tablename__ = "expense"
    id: Mapped[int] = Column(Integer, primary_key=True)
    user_id: Mapped[User] = Column(Integer, ForeignKey("users.id"))
    category: Mapped[Category] = Column(Integer, ForeignKey("category.id"))
    date: Mapped[Date]
