
from fastapi import FastAPI

from app.internal.database import Base
from app.routers import user, blog, authentication
from app.internal.database import engine


# Create all the tables in the database
Base.metadata.create_all(engine)

# Create the app
app = FastAPI()

# Add the routers
app.include_router(user.router)
app.include_router(blog.router)
app.include_router(authentication.router)