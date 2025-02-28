# uwai-rest-backend-booking

Простой микросервис на FastAPI. Этот микросервис предназначен для проверки работы API и базы данных Restoplace.

## Установка и запуск

### Клонирование репозитория

Для клонирования репозитория используйте следующую команду:

```shell
git clone https://github.com/DmitriiButk/uwai-rest-backend-booking.git
```

### Установка зависимостей

Используйте следующую команду для установки необходимых зависимостей:

```shell
pip install -r requirements.txt
```

### Запуск API

Для запуска API используйте следующую команду:

```shell
uvicorn app.main:app --reload
```

## Проверка работы

### Проверка работы API

Для проверки работы API перейдите по следующему URL:

```shell
http://127.0.0.1:8000/api_health
```

### Проверка работы API Restoplace

Для проверки работы API Restoplace перейдите по следующему URL:

```shell
http://127.0.0.1:8000/api_restaurant_health
```

### Проверка работы базы данных

Для проверки работы базы данных перейдите по следующему URL:

```shell
http://127.0.0.1:8000/db_health
```

### Роутеры

#### Резервы (`app/routers/reserves.py`)

- `/reserves`: Получение списка резервов
- `/reserves/{reserve_id}`: Получение данных резерва по ID
- `/reserves`: Создание резерва
- `/reserves/{reserve_id}/status`: Обновление статуса резерва
- `/times`: Получение доступных слотов времени
