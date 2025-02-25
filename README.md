Простой микросервис на fastapi.
Проверка работы самой API,
также проверка работы базы данных.

Клонирование репозитория:

```share
https://github.com/DmitriiButk/uwai-rest-backend-booking.git
```

Установка зависимостей:

```share
pip install requirements.txt
```

Запуск API:

```share
uvicorn app.main:app --reload
```

Проверка работы API:

```share
http://127.0.0.1:8000/api_health
```

Проверка работы базы данных:

```share
http://127.0.0.1:8000/db_health
```

