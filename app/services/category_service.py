from sqlalchemy.orm import Session
from app.repositories.category_repository import CategoryRepository
from app.schemas import CategoryCreate, CategoryUpdate, CategoryDTO
from app.exceptions.base_exception import (
    ResourceAlreadyExistsException,
    ResourceNotFoundException,
)


class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()

    def create_category(self, db: Session, category_in: CategoryCreate) -> CategoryDTO:
        existing = self.repository.get_by_name(db, category_in.name)
        if existing:
            raise ResourceAlreadyExistsException("Category", "name", category_in.name)
        return self.repository.create(db, category_in)

    def get_category(self, db: Session, category_id: int) -> CategoryDTO:
        category = self.repository.get(db, category_id)
        if not category:
            raise ResourceNotFoundException("Category", str(category_id))
        return category

    def get_all_categories(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.get_all(db, skip, limit)
