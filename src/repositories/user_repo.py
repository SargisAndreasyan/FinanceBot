from db.session import SessionLocal
from core.response import Response
from db.models import User
from repositories.base import BaseRepository


class UserRepository(BaseRepository):
    model = User

    def create_user(self, t_id: int) -> Response:
        db = SessionLocal()
        try:
            user = User(t_id=t_id)
            db.add(user)
            db.commit()
            db.refresh(user)
            return Response.ok(self._to_dict(user))

        except Exception as e:
            db.rollback()
            return Response.fail(str(e))

        finally:
            db.close()

    def get_by_t_id(self, t_id: int) -> Response:
        db = SessionLocal()
        try:
            user = db.query(User).filter(
                User.t_id == t_id
            ).first()

            if not user:
                return Response.fail("not_found")

            return Response.ok(self._to_dict(user))

        except Exception as e:
            return Response.fail(str(e))

        finally:
            db.close()