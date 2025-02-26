from fastapi import FastAPI
from app.routers import db_check, restaurant, restaurant_check


app = FastAPI(title='Restoplace API')

app.include_router(db_check.router)
app.include_router(restaurant.router)
app.include_router(restaurant_check.router)


@app.get('/api_health', summary='Проверка работы API')
async def get_health_check():
    return {"status": "Api is working"}
