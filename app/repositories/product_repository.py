from typing import List
from sqlalchemy.orm import Session
from app.repositories.base_repository import BaseRepository
from app.models.product_entity import Product
from app.schemas import ProductCreate, ProductUpdate


class ProductRepository(BaseRepository[Product, ProductCreate, ProductUpdate]):
    def __init__(self):
        super().__init__(Product)

    def search_by_name(self, db: Session, name: str) -> List[Product]:
        return db.query(Product).filter(Product.name.ilike(f"%{name}%")).all()

    def get_low_stock(self, db: Session, threshold: int = 10) -> List[Product]:
        return db.query(Product).filter(Product.quantity < threshold).all()
