# database.py
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

templates = Jinja2Templates(directory="templates")

# Define the database URL (PostgreSQL example)
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/hospital_management"

# DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost/hospital_management"
# Create the engine
engine = create_engine(DATABASE_URL)

# Create a session for querying the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class to define models
Base = declarative_base()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
