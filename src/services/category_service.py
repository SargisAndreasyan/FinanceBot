from db.models import Category
from repositories.category_repo import CategoryRepository
from services.user_service import UserService


class CategoryService:
    def __init__(self, t_id: int):
        self.repo = CategoryRepository()
        self.t_id = t_id
        self.user_service = UserService()

    def create_category(self, name) -> str:
        if not self.user_service.get_user(self.t_id).success:
            return "User not found"

        name = name.strip().lower()

        if self.repo.get_by_name(self.t_id, name).success:
            return f"{name} category already exists"

        category = Category(
            name=name,
            user_id=self.t_id
        )

        self.repo.create(category)

        return f"{name} category created successfully"

    def delete_category(self, name: str) -> str:
        db = self.repo.SessionLocal()
        try:
            category = db.query(Category).filter(
                Category.user_id == self.t_id,
                Category.name == name.strip().lower()
            ).first()

            if not category:
                return "Category not found"

            db.delete(category)
            db.commit()

            return f"{name} category deleted successfully"

        finally:
            db.close()