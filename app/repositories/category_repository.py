from sqlalchemy.orm import Session
from app.repositories.base_repository import BaseRepository
from app.models.category_entity import Category
from app.schemas import CategoryCreate, CategoryUpdate


class CategoryRepository(BaseRepository[Category, CategoryCreate, CategoryUpdate]):
    def __init__(self):
        super().__init__(Category)

    def get_by_name(self, db: Session, name: str):
        return db.query(Category).filter(Category.name == name).first()
