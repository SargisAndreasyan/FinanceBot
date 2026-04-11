from repositories.user_repo import UserRepository

class UserService:

    def __init__(self):
        self.repo = UserRepository()

    def create_user(self):
        return self.repo.create()

    def get_user(self, template_id: int):
        return self.repo.get_by_id(template_id)

    def list_users(self):
        return self.repo.get_all()

    def delete_user(self, template_id: int):
        return self.repo.delete(template_id)