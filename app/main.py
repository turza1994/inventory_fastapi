from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base
from app.api.v1.router import api_router
from app.exceptions.handlers import add_exception_handlers
from app.models import Category, Product # Ensure models are imported for metadata

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Global Exception Handlers
add_exception_handlers(app)

# Include Router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to Inventory Management System API"}
