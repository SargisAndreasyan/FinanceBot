from repositories.category_repo import CategoryRepository
class CategoryService:

    def __init__(self):
        self.repo = CategoryRepository()

    def create_category(self, user_id, name) -> str:
        name = name.strip().lower()

        if self.repo.get_by_name(user_id, name):
            return f"{name} category already exists"

        self.repo.create(user_id=user_id, name=name)
        return f"{name} category created successfully"


    def delete_category(self, name: str)->str:
        self.repo.delete(name=name)
        return f"{name} category deleted successfully"