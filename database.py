import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from urllib.parse import quote_plus


#load environment from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = quote_plus(os.getenv("POSTGRES_PASSWORD"))
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine= create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)
Base= declarative_base()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()