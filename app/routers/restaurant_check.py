from fastapi import APIRouter, HTTPException
from app.backend.db_config import settings
import httpx


router = APIRouter()


@router.get('/api_restaurant_health', summary='Проверка работы API Restoplace')
async def check_health_api_restaurant():
    api_url = 'https://api.restoplace.cc/reserves'
    headers = {"X-API-Key": settings.RESTO_API_KEY}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url, headers=headers)
            response.raise_for_status()
            response_data = response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f'API Restoplace error: {e.response.text}')
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail='Error connecting to API Restoplace')
    return {'status': response.status_code, 'message': response_data}
