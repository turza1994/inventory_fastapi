from typing import List
from sqlalchemy.orm import Session
from app.repositories.product_repository import ProductRepository
from app.services.category_service import CategoryService
from app.schemas.product_dto import ProductCreate, ProductUpdate, ProductDTO
from app.exceptions.base_exception import ResourceNotFoundException


class ProductService:
    def __init__(self):
        self.repository = ProductRepository()
        self.category_service = CategoryService()

    def create_product(self, db: Session, product_in: ProductCreate) -> ProductDTO:
        # Check if category exists
        self.category_service.get_category(db, product_in.category_id)
        return self.repository.create(db, product_in)

    def get_product(self, db: Session, product_id: int) -> ProductDTO:
        product = self.repository.get(db, product_id)
        if not product:
            raise ResourceNotFoundException("Product", str(product_id))
        return product

    def get_all_products(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.get_all(db, skip, limit)

    def update_product(
        self, db: Session, product_id: int, product_in: ProductUpdate
    ) -> ProductDTO:
        product = self.get_product(db, product_id)
        if product_in.category_id:
            self.category_service.get_category(db, product_in.category_id)
        return self.repository.update(db, product, product_in)

    def delete_product(self, db: Session, product_id: int):
        product = self.get_product(db, product_id)

        # if product.category:
        #      _ = product.category.name

        product_dto = ProductDTO.model_validate(product)
        self.repository.delete(db, product_id)
        return product_dto

    def search_products(self, db: Session, name: str):
        return self.repository.search_by_name(db, name)

    def get_low_stock_products(self, db: Session):
        return self.repository.get_low_stock(db)
