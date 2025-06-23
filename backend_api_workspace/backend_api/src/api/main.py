from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers to be defined for authentication and recipe management
from .routers import users, recipes, sharing

app = FastAPI(
    title="RecipeHub API",
    description=(
        "A backend REST API for recipe browsing, management, and sharing "
        "with user authentication."
    ),
    version="1.0.0",
    openapi_tags=[
        {"name": "auth", "description": "User registration and authentication"},
        {"name": "recipes", "description": "View, create, update, delete, search recipes"},
        {"name": "sharing", "description": "Recipe sharing between users"},
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers for all major functionalities
app.include_router(users.router, prefix="/api/auth", tags=["auth"])
app.include_router(recipes.router, prefix="/api/recipes", tags=["recipes"])
app.include_router(sharing.router, prefix="/api/share", tags=["sharing"])


@app.get("/", tags=["health"])
def health_check():
    """Health check endpoint."""
    return {"message": "Healthy"}
