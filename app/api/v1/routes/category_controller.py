from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.category_dto import CategoryCreate, CategoryUpdate, CategoryDTO
from app.services.category_service import CategoryService

router = APIRouter()

# Dependency injection for Service
def get_service():
    return CategoryService()

@router.post("/", response_model=CategoryDTO)
def create_category(
    category_in: CategoryCreate,
    db: Session = Depends(get_db),
    service: CategoryService = Depends(get_service)
):
    return service.create_category(db, category_in)

@router.get("/{category_id}", response_model=CategoryDTO)
def read_category(
    category_id: int,
    db: Session = Depends(get_db),
    service: CategoryService = Depends(get_service)
):
    return service.get_category(db, category_id)

@router.get("/", response_model=List[CategoryDTO])
def read_categories(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    service: CategoryService = Depends(get_service)
):
    return service.get_all_categories(db, skip, limit)
