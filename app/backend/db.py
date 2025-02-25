from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.backend.db_config import settings


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_db_connection():
    try:
        with engine.connect():
            return True
    except Exception:
        return False
