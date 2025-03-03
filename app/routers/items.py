from typing import Optional, Dict
from fastapi import APIRouter, Query
from app.backend.db_config import settings
from app.utils.http_client import make_request


router = APIRouter(prefix='/restaurant', tags=['items'])


@router.get('/items', summary='Получение списка объектов бронирования')
async def get_items(
        query: Optional[str] = Query(None, description='Поисковый запрос по полям объектов бронирования'),
        page: Optional[int] = Query(1, ge=1, description='Страница выводимых объектов (по умолчанию: 1)')
):
    api_url = 'https://api.restoplace.cc/items/'
    headers = {'X-API-Key': settings.RESTO_API_KEY}

    params: Dict[str, Optional[str]] = {
        'query': query,
        'page': page
    }

    return await make_request('GET', api_url, headers=headers, params=params)


@router.get('/items/{item_id}', summary='Получение данных объекта бронирования по ID')
async def get_item_by_id(item_id: str):
    api_url = f'https://api.restoplace.cc/items/{item_id}'
    headers = {'X-API-Key': settings.RESTO_API_KEY}

    return await make_request('GET', api_url, headers=headers)
