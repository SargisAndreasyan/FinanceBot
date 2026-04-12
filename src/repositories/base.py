from db.session import SessionLocal
from core.response import Response


class BaseRepository:
    model = None

    def create(self, obj) -> Response:
        db = SessionLocal()
        try:
            db.add(obj)
            db.commit()
            db.refresh(obj)

            return Response.ok(self._to_dict(obj))

        except Exception as e:
            db.rollback()
            return Response.fail(str(e))

        finally:
            db.close()

    def get_by_id(self, id_) -> Response:
        db = SessionLocal()
        try:
            obj = db.query(self.model).filter(
                self.model.id == id_
            ).first()

            if not obj:
                return Response.fail("not_found")

            return Response.ok(self._to_dict(obj))

        except Exception as e:
            return Response.fail(str(e))

        finally:
            db.close()

    def get_all(self) -> Response:
        db = SessionLocal()
        try:
            objects = db.query(self.model).all()

            return Response.ok([
                self._to_dict(obj) for obj in objects
            ])

        except Exception as e:
            return Response.fail(str(e))

        finally:
            db.close()

    def delete(self, id_) -> Response:
        db = SessionLocal()
        try:
            obj = db.query(self.model).filter(
                self.model.id == id_
            ).first()

            if not obj:
                return Response.fail("not_found")

            data = self._to_dict(obj)

            db.delete(obj)
            db.commit()

            return Response.ok(data)

        except Exception as e:
            db.rollback()
            return Response.fail(str(e))

        finally:
            db.close()

    def _to_dict(self, obj):
        return {
            c.name: getattr(obj, c.name)
            for c in obj.__table__.columns
        }