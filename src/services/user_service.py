from sqlalchemy.sql.functions import user

from core import Response
from repositories.user_repo import UserRepository
from db.models import User


class UserService:

    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, t_id)->Response[int]:
        """Return t_id of user"""
        if not self.get_user(t_id).success:
            user = User(t_id=t_id)
            self.repo.create(user)
            return Response.ok(t_id)
        else:
            return Response.ok(t_id)

    def get_user(self, t_id: int):
        return self.repo.get_by_t_id(t_id=t_id)

    def list_users(self):
        return self.repo.get_all()

    def delete_user(self, t_id: int)->str:
        self.repo.delete_by_t_id(t_id=t_id)
        return f"User {t_id} deleted successfully"