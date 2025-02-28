from typing import Optional, Dict, Literal
from fastapi import APIRouter, Query
from fastapi.encoders import jsonable_encoder
from app.backend.db_config import settings

from app.schemas import ReserveCreate
from app.utils.http_client import make_request


router = APIRouter(prefix='/restaurant', tags=['reserve'])


@router.get('/reserves', summary='Получение списка резервов')
async def get_reserves(
        updated_after_time: Optional[str] = Query(None,
                                                  description='Резервы, созданные/измененные после указанного времени в формате unix'),
        query: Optional[str] = Query(None, description='Поисковый запрос по полям резервов'),
        page: Optional[int] = Query(1, ge=1, description='Страница выводимых объектов (по умолчанию: 1)')
):
    api_url = 'https://api.restoplace.cc/reserves/'
    headers = {'X-API-Key': settings.RESTO_API_KEY}

    params: Dict[str, Optional[str]] = {
        'updatedAfterTime': updated_after_time,
        'query': query,
        'page': page
    }

    return await make_request('GET', api_url, headers=headers, params=params)


@router.get('/reserves/{reserve_id}',
            summary='Получение данных резерва по ID')
async def get_reserve_by_id(reserve_id: str):
    api_url = f'https://api.restoplace.cc/reserves/{reserve_id}'
    headers = {'X-API-Key': settings.RESTO_API_KEY}

    return await make_request('GET', api_url, headers=headers)


@router.post('/reserves',
             summary='Создание резерва')
async def create_reserve(reserve: ReserveCreate):
    api_url = 'https://api.restoplace.cc/reserves/'
    headers = {'X-API-Key': settings.RESTO_API_KEY}

    payload = jsonable_encoder(reserve)

    return await make_request('POST', api_url, headers=headers, json=payload)


@router.put('/reserves/{reserve_id}/status',
            summary='Обновление статуса резерва')
async def update_reserve_status(
        reserve_id: int,
        status: int = Query(..., description='Новый статус резерва')
):
    api_url = f'https://api.restoplace.cc/reserves/{reserve_id}/status'
    headers = {'X-API-Key': settings.RESTO_API_KEY}

    data = {'status': status}

    return await make_request('PUT', api_url, headers=headers, json=data)


@router.get('/times',
            summary='Получение доступных слотов времени')
async def get_time_slots(
        date: str = Query(..., regex='^\d{4}-\d{2}-\d{2}$',
                          description='Дата бронирования в формате YYYY-MM-DD'),
        length: int = Query(120,
                            description='Продолжительность слота в минутах'),
        shift: Optional[int] = Query(None, ge=30, le=1440,
                                     description='Сдвиг начала слота относительно предыдущего'),
        dateFormat: Literal['standart', 'RFC3339'] = Query('standart',
                                                           description='''Формат даты и времени в ответе:
                                                                        - standart: '2024-05-31 00:00:00'
                                                                        - RFC3339: '2024-12-02T14:12:43+00:00' ''')):
    api_url = 'https://api.restoplace.cc/times'
    headers = {'X-API-Key': settings.RESTO_API_KEY}

    params = {
        'date': date,
        'length': length,
        'shift': shift,
        'dateFormat': dateFormat
    }

    return await make_request('GET', api_url, headers=headers, params=params)
