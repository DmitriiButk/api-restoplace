from fastapi import APIRouter
from app.backend.db import check_db_connection, create_database


router = APIRouter()


@router.get('/db_health', summary='Проверка подключения к базе данных')
def db_health_check():
    if check_db_connection():
        return {'status': 'ok', 'message': 'Подключение к базе данных успешно'}
    return {'status': 'error', 'message': 'Ошибка подключения к базе данных'}


@router.get('/db_create', summary='Создание базы данных')
def database_create():
    return create_database()
