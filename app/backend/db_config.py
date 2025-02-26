import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: int = int(os.getenv("DATABASE_PORT", 5432))
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "database")
    DATABASE_USER: str = os.getenv("DATABASE_USER", "user")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "password")
    RESTO_API_KEY: str = os.getenv("RESTO_API_KEY", "some_api_key")

    DATABASE_URL: str = (
        f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )


settings = Settings()
