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


def create_database():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT 1 FROM pg_database WHERE datname = :db_name'),
                              {'db_name': settings.DATABASE_NAME}).fetchone()

        if not result:
            conn.execute(f'CREATE DATABASE {settings.DATABASE_NAME}')
            return {'message': f'База данных {settings.DATABASE_NAME} создана'}
        else:
            return {'message': f'База данных {settings.DATABASE_NAME} уже существует'}
