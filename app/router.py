from fastapi import APIRouter
from app.controllers import category_controller, product_controller

router = APIRouter()

router.include_router(
    category_controller.router, prefix="/categories", tags=["Categories"]
)
router.include_router(product_controller.router, prefix="/products", tags=["Products"])
