# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from .models import user as User, blog as Blog  # Import your database models
from .db.session import engine
from app.api.v1 import user, blog  # Import your route module


User.Base.metadata.create_all(bind=engine)  # Create tables in the database
Blog.Base.metadata.create_all(bind=engine)  # Create tables in the database

app = FastAPI(
    title="My FastAPI Project",
    version="1.0.0",
    description="A production-ready FastAPI application.",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ✅ Security best practice: Optional Trusted Host Middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1", "*.yourdomain.com"],
)

# ✅ CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Frontend dev client
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS", "PUT"],
    allow_headers=["*"],
)

# ✅ Register API routes
app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(blog.router, prefix="/api/v1/blogs", tags=["Blogs"])


# ✅ Health check route
@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to FastAPI!"}


# ✅ Optional root route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
