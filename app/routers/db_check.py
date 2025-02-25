from fastapi import APIRouter
from app.backend.db import check_db_connection


router = APIRouter()


@router.get('/db_health', summary='Проверка подключения к базе данных')
def db_health_check():
    if check_db_connection():
        return {'status': 'ok', 'message': 'Подключение к базе данных успешно'}
    return {'status': 'error', 'message': 'Ошибка подключения к базе данных'}
