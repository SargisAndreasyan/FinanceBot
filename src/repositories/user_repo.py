from db.session import SessionLocal
from db.models import User

class UserRepository:

    def create(self,t_id):
        db = SessionLocal()
        try:
            obj = User(t_id=t_id)
            db.add(obj)
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj
        finally:
            db.close()

    def get_by_id(self, t_id: int):
        db = SessionLocal()
        try:
            return db.query(User).filter(User.t_id == t_id).first()
        finally:
            db.close()

    def get_all(self):
        db = SessionLocal()
        try:
            return db.query(User).all()
        finally:
            db.close()

    def delete(self, t_id: int):
        db = SessionLocal()
        try:
            obj = db.query(User).filter(User.id == t_id).first()
            if obj:
                db.delete(obj)
                db.commit()
            return obj
        finally:
            db.close()