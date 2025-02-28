from fastapi import FastAPI
from app.routers import db_check,reserves, restaurant_check


app = FastAPI(title='Restoplace API')

app.include_router(db_check.router)
app.include_router(reserves.router)
app.include_router(restaurant_check.router)


@app.get('/api_health', summary='Проверка работы API', tags=['check_api_status'])
async def get_health_check():
    return {'message': 'Api is working'}


