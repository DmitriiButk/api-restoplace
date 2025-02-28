from fastapi import APIRouter
from app.backend.db_config import settings

from app.utils.http_client import make_request


router = APIRouter(tags=['check_restoplace_api_connection'])


@router.get('/api_restaurant_health', summary='Проверка работы API Restoplace')
async def check_health_api_restaurant():
    api_url = 'https://api.restoplace.cc/reserves'
    headers = {"X-API-Key": settings.RESTO_API_KEY}

    if make_request('GET', api_url, headers=headers):
        return {'message': 'Restoplace API is working'}
