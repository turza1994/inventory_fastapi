from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base

from app.exceptions.handlers import add_exception_handlers
from app.models import Category, Product  # Ensure models are imported for metadata

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Global Exception Handlers
add_exception_handlers(app)

from app.router import router

# ...

# Include Router
app.include_router(router, prefix=settings.API_V1_STR)


@app.get("/")
def root():
    return {"message": "Welcome to Inventory Management System API"}
