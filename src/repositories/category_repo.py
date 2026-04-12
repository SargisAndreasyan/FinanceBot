from db.session import SessionLocal
from db.models import Category
from repositories.base import BaseRepository
from core import Response


class CategoryRepository(BaseRepository):
    model = Category

    def get_by_name(self, user_id: int, name: str):
        db = SessionLocal()
        try:
            category = (
                db.query(Category)
                .filter(
                    Category.user_id == user_id,
                    Category.name == name
                )
                .first()
            )

            if not category:
                return Response.fail("not_found")

            return Response.ok({
                "id": category.id,
                "name": category.name,
                "user_id": category.user_id
            })

        finally:
            db.close()