from repositories.user_repo import UserRepository

class UserService:

    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, t_id)->dict:
        if self.get_user(t_id) is None:
            self.repo.create(t_id=t_id)
            return {'user_id': t_id , 'answer': f'User {t_id} already exists'}

        else:
            return {'user_id': t_id , 'answer': f'User {t_id} already exists'}

    def get_user(self, t_id: int):
        return self.repo.get_by_id(t_id=t_id)

    def list_users(self):
        return self.repo.get_all()

    def delete_user(self, t_id: int)->str:
        self.repo.delete(t_id=t_id)
        return f"User {t_id} deleted successfully"