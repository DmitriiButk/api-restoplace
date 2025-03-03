from typing import Optional, Dict
from fastapi import APIRouter, Query
from app.backend.db_config import settings
from app.utils.http_client import make_request


router = APIRouter(prefix='/restaurant', tags=['halls'])


@router.get('/halls', summary='Получение списка залов')
async def get_halls(
        query: Optional[str] = Query(None, description='Поисковый запрос по полям залов'),
        page: Optional[int] = Query(1, ge=1, description='Страница выводимых объектов (по умолчанию: 1)')
):
    api_url = 'https://api.restoplace.cc/halls/'
    headers = {'X-API-Key': settings.RESTO_API_KEY}

    params: Dict[str, Optional[str]] = {
        'query': query,
        'page': page
    }

    return await make_request('GET', api_url, headers=headers, params=params)


@router.get('/halls/{hall_id}', summary='Получение данных зала по ID')
async def get_hall_by_id(hall_id: str):
    api_url = f'https://api.restoplace.cc/halls/{hall_id}'
    headers = {'X-API-Key': settings.RESTO_API_KEY}

    return await make_request('GET', api_url, headers=headers)
