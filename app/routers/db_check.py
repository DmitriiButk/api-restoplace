from fastapi import APIRouter
from app.backend.db import check_db_connection


router = APIRouter(tags=['check_db_connection'])


@router.get('/db_health', summary='Проверка подключения к базе данных')
async def db_health_check():
    if await check_db_connection():
        return {'status': 'ok', 'message': 'Подключение к базе данных успешно'}
    return {'status': 'error', 'message': 'Ошибка подключения к базе данных'}
