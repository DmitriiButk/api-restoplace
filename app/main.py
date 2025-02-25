from fastapi import FastAPI
from app.routers import db_check


app = FastAPI()

app.include_router(db_check.router)


@app.get('/api_health', summary='Проверка работы API')
def get_health_check():
    return {"status": "Api is working"}


