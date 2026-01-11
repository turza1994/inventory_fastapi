from fastapi import APIRouter
from app.api.v1.routes import category_controller, product_controller

api_router = APIRouter()

api_router.include_router(
    category_controller.router, prefix="/categories", tags=["categories"]
)
api_router.include_router(
    product_controller.router, prefix="/products", tags=["products"]
)
