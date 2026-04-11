from db.session import SessionLocal
from db.models import User

class UserRepository:

    def create(self):
        db = SessionLocal()
        try:
            obj = User()
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj
        finally:
            db.close()

    def get_by_id(self, template_id: int):
        db = SessionLocal()
        try:
            return db.query(User).filter(User.id == template_id).first()
        finally:
            db.close()

    def get_all(self):
        db = SessionLocal()
        try:
            return db.query(User).all()
        finally:
            db.close()

    def delete(self, template_id: int):
        db = SessionLocal()
        try:
            obj = db.query(User).filter(User.id == template_id).first()
            if obj:
                db.delete(obj)
                db.commit()
            return obj
        finally:
            db.close()