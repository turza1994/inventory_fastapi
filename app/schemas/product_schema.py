from pydantic import BaseModel
from typing import Optional
from app.schemas.category_schema import CategoryDTO


class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int
    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category_id: Optional[int] = None


class ProductDTO(ProductBase):
    id: int
    category: Optional[CategoryDTO] = None

    class Config:
        from_attributes = True
