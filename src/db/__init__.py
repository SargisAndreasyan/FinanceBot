from db.session import engine
from db.base import Base

from db.models import User

def init_db():
    Base.metadata.create_all(bind=engine)