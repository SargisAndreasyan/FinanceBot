from db.session import SessionLocal
from db.models import Template

class TemplateRepository:

    def create(self, name: str):
        db = SessionLocal()
        try:
            obj = Template(name=name)
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj
        finally:
            db.close()

    def get_by_id(self, template_id: int):
        db = SessionLocal()
        try:
            return db.query(Template).filter(Template.id == template_id).first()
        finally:
            db.close()

    def get_all(self):
        db = SessionLocal()
        try:
            return db.query(Template).all()
        finally:
            db.close()

    def delete(self, template_id: int):
        db = SessionLocal()
        try:
            obj = db.query(Template).filter(Template.id == template_id).first()
            if obj:
                db.delete(obj)
                db.commit()
            return obj
        finally:
            db.close()