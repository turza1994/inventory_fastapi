from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas import ProductCreate, ProductUpdate, ProductDTO
from app.services.product_service import ProductService

router = APIRouter()


def get_service():
    return ProductService()


@router.post("/products", response_model=ProductDTO)
def create_product(
    product_in: ProductCreate,
    db: Session = Depends(get_db),
    service: ProductService = Depends(get_service),
):
    return service.create_product(db, product_in)


@router.get("/products/{product_id}", response_model=ProductDTO)
def read_product(
    product_id: int,
    db: Session = Depends(get_db),
    service: ProductService = Depends(get_service),
):
    return service.get_product(db, product_id)


@router.put("/products/{product_id}", response_model=ProductDTO)
def update_product(
    product_id: int,
    product_in: ProductUpdate,
    db: Session = Depends(get_db),
    service: ProductService = Depends(get_service),
):
    return service.update_product(db, product_id, product_in)


@router.delete("/products/{product_id}", response_model=ProductDTO)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    service: ProductService = Depends(get_service),
):
    return service.delete_product(db, product_id)


@router.get("/products", response_model=List[ProductDTO])
def read_products(
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = None,
    low_stock: bool = False,
    db: Session = Depends(get_db),
    service: ProductService = Depends(get_service),
):
    if search:
        return service.search_products(db, search)
    if low_stock:
        return service.get_low_stock_products(db)
    return service.get_all_products(db, skip, limit)
