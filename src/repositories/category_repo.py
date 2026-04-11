from db.session import SessionLocal
from db.models import Category

class CategoryRepository:

    def create(self,user_id, name):
        db = SessionLocal()
        try:
            obj = Category(user_id = user_id, name = name)
            db.add(obj)
            db.commit()
            db.add(obj)
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj
        finally:
            db.close()

    def get_all(self):
        db = SessionLocal()
        try:
            return db.query(Category).all()
        finally:
            db.close()

    def get_by_name(self, user_id: int, name: str):
        db = SessionLocal()
        try:
            return (
                db.query(Category)
                .filter(Category.user_id == user_id, Category.name == name)
                .first()
            )
        finally:
            db.close()

    def delete(self, name: str):
        db = SessionLocal()
        try:
            obj = db.query(Category).filter(Category.name == name).first()
            if obj:
                db.delete(obj)
                db.commit()
            return obj
        finally:
            db.close()